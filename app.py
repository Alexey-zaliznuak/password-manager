import os
from flask import *
from time import sleep

from SQLDataStorage import *
app = Flask(__name__)

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

@app.route("/passwords")
def main():
    account_manager = AccountStorage("./static/_data/mydatabase.db", "accounts")
    account_data = account_manager.get()

    users_manager = UserStorage("./static/_data/mydatabase.db", "users")
    users_data = users_manager.get()

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
        data = account_manager.get_by_UID(int(UID))
        return render_template("passwords.html", pack_data = data, UID = UID)

@app.route("/find_account")
def find_account():
    name = request.args['name']
    password = request.args['password']
    telephone = request.args['telephone']
    create = request.args["create"]

    users_manager = UserStorage("./static/_data/mydatabase.db", "users")
    users_data = users_manager.get()

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
    service = request.args['service'] 
    email = request.args['email'] 
    password = request.args['password'] 
    ac_id = request.args['id'] 
    date_changes = request.args['date_changes'] 
    UID = request.args['UID'] 

    #print(f"SERVICE={service}, EMAIL={email}, PASSWORD={password}, ID={ac_id},DATE = {date_changes}, {UID}")


    data = [service,email,password,ac_id,date_changes,UID]
    return render_template("password_see.html", data = data)

@app.route("/create", methods = ["GET"])
def create_page():
    user_id = request.args['UID'] 
    return render_template("create_page.html", UID = user_id)

@app.route("/create_account", methods = ["GET"])
def create_account():
    UID = request.args['UID'] 
    service = request.args['service'] 
    passsword = request.args['password'] 
    email = request.args['email'] 

    updates_managers()
    account_manager.write(email, service, passsword, UID)

    print(email, service, passsword, UID)
    return "Создание аккаунта - успешно"

@app.route("/del_account", methods = ["GET"])
def delete_account():
    updates_managers()
    account_id = request.args['ID'] 
    user_id = request.args['UID'] 
    account_manager.delete(account_id, user_id)
    print(int(user_id),int(account_id))
    return "succesful"

def updates_managers():
    global account_data, account_manager
    account_manager = AccountStorage("./static/_data/mydatabase.db", "accounts")
    account_data = account_manager.get()

    global users_data, users_manager
    users_manager = UserStorage("./static/_data/mydatabase.db", "users")
    users_data = users_manager.get()


if __name__ == "__main__":
    updates_managers()
    app.run(debug = True)