from flask import Flask, jsonify, request
from DataBase import DataBase # Наш класс базы данных
import os
app = Flask(__name__)
full_path = f"{os.path.dirname(os.path.abspath(__file__))}"
accounts_db = DataBase(f'{full_path}/data/accounts.json')

@app.route("/api/accounts", methods=['GET'])
def get_accounts():
    return jsonify({'accounts': accounts_db.get()})

@app.route('/api/accounts', methods=['POST'])
def create_account():
    if not request.json:
        abort(400)

    for key in ('service', 'email', 'password'): 
        if key not in request.json:
            abort(400)


    account = {
        'service': request.json['service'],
        'email': request.json['email'],
        'password': request.json['password'],
    }

    # метод create возвращает аккаунт со всеми полями 
    # в их числе id и дата создания записи
    account = accounts_db.create(account["service"],account["email"],account["password"])

    return jsonify({'account': account}), 201

@app.route('/api/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    if not request.json:
        abort(400)

    for key in ('service', 'email', 'password'): 
        if key not in request.json:
            abort(400)


    account = {
        'service': request.json['service'],
        'email': request.json['email'],
        'password': request.json['password'],
    }

    accounts_db.update(account)

@app.route('/api/accounts/<int:id>', methods=['DELETE'])
def delete_account(ac_id):
    accounts_db.delete(ac_id)
    
if __name__ == '__main__':
    app.run()