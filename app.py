import os
import re
import avatars
import sqlite3
import werkzeug

from time import sleep
from flask import render_template, Flask, request

from database.AccountStorage import AccountStorage
from database.UserStorage import UserStorage
from database.FolderStorage import FolderStorage
from database.FileStorage import FileStorage as fileStorage

app = Flask(__name__)
db_path = './database/_data/mydatabase.db'

#global account_manager
account_manager = AccountStorage(db_path, "accounts")

#global users_manager
users_manager = UserStorage(db_path, "users")

#global folders_manager
folders_manager = FolderStorage(db_path, "folders")

#global files_manager
file_manager = fileStorage(db_path, "files")

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/registration_permission")
def registration_permission():
    name = request.args['name']
    password = request.args['password']
    telephone = request.args['telephone']
    response = users_manager.get_registration_permission(name, password, telephone)

    if response == "Успешно":
        users_manager.write(name, password, telephone)
        avatars.generate(name, 12, 50, True, f"{name}.png")

        os.replace(f"{name}.png", f"./static/avatars/{name}.png")
    return response

@app.route("/passwords")
def main():
    UID = request.args['UID']
    if UID == "None":
        name = request.args['name']
        password = request.args['password']
        telephone = request.args['telephone']
        create = request.args["create"]
        UID = users_manager.get_by_data(str(name), str(password), str(telephone), bool(int(create)))

    try:
        UID = int(UID)
    except:
        return UID
    else:
        name = users_manager.get_name(UID)[0][0]
        data = account_manager.get_by_UID(int(UID))
        return render_template("passwords.html", pack_data = data, UID = UID, name = name)

@app.route("/find_account")
def find_account():
    name = request.args['name']
    password = request.args['password']
    telephone = request.args['telephone']
    create = request.args["create"]

    UID = users_manager.get_by_data(str(name), str(password), str(telephone), bool(int(create)))
    print("Ответ на поиск юзера ==>",UID)

    if type(UID) == str:
        return UID
    else:
        print("Тип ответа ==>",type(UID))
        return "Успешно"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/details", methods = ["GET"])
def details():
    UID = request.args['UID'] 
    name = users_manager.get_name(UID)[0][0]

    service = request.args['service'] 
    email = request.args['email'] 
    password = request.args['password'] 
    ac_id = request.args['id'] 
    date_changes = request.args['date_changes'] 

    #print(f"SERVICE={service}, EMAIL={email}, PASSWORD={password}, ID={ac_id},DATE = {date_changes}, {UID}")


    data = [service,email,password,ac_id,date_changes, UID]
    return render_template("password_see.html", data = data, name = name, UID = UID)

@app.route("/create_password", methods = ["GET"])
def create_page():
    user_id = request.args['UID'] 
    name = users_manager.get_name(user_id)[0][0]

    return render_template("create_page.html", UID = user_id, name = name)

@app.route('/choose_file')
def create_file():
    UID = request.args['UID'] 
    name = users_manager.get_name(UID)[0][0]

    return render_template("load_file.html", UID = UID, name = name)

@app.route('/load_file', methods = ["POST"])
def load_file():
    UID = request.args['UID'] 
    file = dict(request.files)["file"]
    pattern = r"'.{0,}\.[^/]{0,}\b'"  
    name = re.findall(pattern, str(file), flags=re.IGNORECASE)[0][1:-1]
    path = f"./data/users_files/{UID}"

    if os.path.isdir(path):
        f = open(f"{path}/{str(name)}", "w+")
        f.close()
    else:
        os.mkdir(path)
        f = open(f"{path}/{str(name)}", "w+")
        f.close()

    file.save(f"{path}/{name}")
    
    return "200"

@app.route("/create_account", methods = ["GET"])
def create_account():
    UID = request.args['UID'] 
    service = request.args['service'] 
    passsword = request.args['password'] 
    email = request.args['email'] 
    account_manager.write(email, service, passsword, UID)
    return "Создание аккаунта - успешно"

@app.route("/update_account_page", methods = ["GET"])
def update_account_page():
    UID = request.args['UID'] 
    name = request.args['name'] 
    id_ = request.args['id'] 
    return render_template("update_password.html", name = name, id_ = id_, UID = UID)

@app.route("/update_account", methods = ["GET"])
def update_account():
    UID = request.args['UID'] 
    ac_id = request.args['id'] 
    service = request.args['service'] 
    password = request.args['password'] 
    email = request.args['email'] 
    print(service, email, password, ac_id, UID)
    account_manager.update(service, email, password, ac_id, UID)
    return "обновлено - успешно"

@app.route("/del_account", methods = ["GET"])
def delete_account():
    account_id = request.args['ID'] 
    user_id = request.args['UID'] 
    account_manager.delete(account_id, user_id)

    return "succesful"

if __name__ == "__main__":
    app.run(debug = True)