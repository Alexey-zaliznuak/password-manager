from flask import *
from DataStorage import *
import os
from time import sleep
app = Flask(__name__)

global account_data,account_manager
account_manager = JsonStorage("./static/_data/data.json")
account_data = account_manager.get()

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/main")
def main():
    global account_data,account_manager
    account_manager = JsonStorage("./static/_data/data.json")
    account_data = account_manager.get()

    UID = int(request.args['UID'])
    if len(account_data) <=  UID:
        print("new_account")
        account_manager.create("new_email", "service_name", "0000000", UID)

    try:
        account_manager = JsonStorage("./static/_data/data.json")
        account_data = account_manager.get()

        data = found_account_UID(account_data, UID)
        return render_template("index.html", pack_data = account_data[UID])
    except:
        pass
@app.route("/details", methods = ["GET"])
def details():
    data = request.args['data'] 
    data.replace("'", '"')
    data = format_request_data(data)
    return render_template("password_see.html", data = data)

@app.route("/create", methods = ["GET"])
def create_page():
    user_id = request.args['UID'] 
    return render_template("create_page.html", UID = user_id)

@app.route("/create_account", methods = ["POST"])
def create_account():
    user_id = request.args['UID'] 
    service = request.args['service'] 
    passsword = request.args['password'] 
    email = request.args['email'] 

    account_manager = JsonStorage("./static/_data/data.json")
    account_manager.create(email, service, passsword, user_id)
    print(email, service, passsword, user_id)
    return "Создание аккаунта - успешно"

@app.route("/del", methods = ["GET"])
def delete_correction():
    print(request)
    account_id = request.args['id'] 
    user_id = request.args['UID'] 
    
    return render_template("delete.html",account_id=account_id,user_id=user_id)

@app.route("/del_account", methods = ["GET"])
def delete_account():
    account_id = request.args['id'] 
    user_id = request.args['UID'] 
    account_manager = JsonStorage("./static/_data/data.json")
    account_manager.delete(int(user_id),int(account_id))
    print(int(user_id),int(account_id))
    return "succesful"

def found_account_UID(data, UID):
    for index, string in enumerate(data):
        if string[0]["UID"] == UID:
            return data[index]
            break
        else:
            print(string[0]["UID"])
    else:
        print("WARNING")
        account_manager.create("new_email", "service_name", "0000000", UID)
        for index, string in enumerate(data):
            if string[0]["UID"] == UID:
                return data[index]

if __name__ == "__main__":
    app.run(debug = True)