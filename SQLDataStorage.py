import sqlite3
from random import randint
from datetime import datetime

class DataStorage():
    def __init__(self, file, table_name):
        self.file = file
        self.table = table_name
        connect = sqlite3.connect(str(file))
        connect.close()

    def create_table(self, args):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        cursor.execute(f"CREATE TABLE {self.table} {args}")
        connect.commit()
        connect.close()
        
    def get(self):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        return cursor.execute(f"select * from {self.table}").fetchall()
        connect.close()

    def current_time(self):
        times = datetime.now()

        year = times.year
        month = times.month
        day = times.day

        hour = times.hour
        minute = times.minute
        second = times.second
        
        if len(str(minute)) < 2:
            minute = f"0{minute}"

        if len(str(hour)) < 2:
            hour = f"0{hour}"

        mod_time = f"{year}/{month}/{day}/{hour}/{minute}/{second}"
        return mod_time

class AccountStorage(DataStorage):
    def write(self, email, service, password, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        data = f"""INSERT INTO {self.table} (service, email, password, date_change, UID) VALUES ("{service}", "{email}", "{password}", "{self.current_time()}", "{UID}")"""

        cursor.execute(data)
        connect.commit()
        connect.close()

    def delete(self, ac_id, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"DELETE FROM {self.table} WHERE UID = {UID} AND ID = {ac_id}")
        connect.commit()

    def get_id(self):
        while True:
            number = randint(0, 1000000)    
            connect = sqlite3.connect(str(self.file))
            cursor = connect.cursor()

            data = cursor.execute(f"select * from {self.table} WHERE id = {number}").fetchall()
            connect.close()
            if len(data) == 0:
                break
        return number 

    def get_by_UID(self, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        return cursor.execute(f"select * from {self.table} WHERE UID = {UID}").fetchall()
        connect.close()

class UserStorage(DataStorage):
    def write(self, name, password, telephone):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        
        data = cursor.execute(f"""
        select UID from {self.table} WHERE name = '{name}'""").fetchall()
        if len(data) == 0:
            data = f"""INSERT INTO {self.table} (name, password, telephone, date_change) VALUES ("{name}", "{password}", "{telephone}", "{self.current_time()}")"""
            cursor.execute(data)
            connect.commit()
            connect.close()
            return "complete"
        else: 
            return "found account with this name"

    def delete(self, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"DELETE FROM {self.table} WHERE UID = {UID}")
        connect.commit()

    def get_by_UID(self, userID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        
        return cursor.execute(f"select * from {self.table} WHERE UID = {userID}").fetchall()
        connect.close()
    
    def get_name(self, userID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        
        return cursor.execute(f"select name from {self.table} WHERE UID = {userID}").fetchall()
        connect.close()

    def get_by_data(self, name, password, telephone, create):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        data = cursor.execute(f"""
        select UID from {self.table} WHERE name = '{name}'""").fetchall()

        verify_data = cursor.execute(f"""
        select UID from {self.table} WHERE name = '{name}' and password = '{password}' and telephone = '{telephone}'""").fetchall()

        connect.close()
        if create:
            if len(data) == 0:
                self.write(name, password, telephone)
                return self.get_by_data(name, password, telephone, True)
            elif len(data) != 0:
                return verify_data[0][0]
        else:
            if len(verify_data) != 0:
                return verify_data[0][0]
            else:
                if len(data) == 0:
                    return "Нет аккаунта с таким именем"
                else:
                    return "некорректные данные"

    def get_registration_permission(self, name, password, telephone):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        user_with_telephone = cursor.execute(f"""
        select UID from {self.table} WHERE telephone = '{telephone}'""").fetchall()

        user_with_name = cursor.execute(f"""
        select UID from {self.table} WHERE name = '{name}'""").fetchall()


        if len(user_with_name) != 0:
            return "Аккаунт с таким именем существует"
        
        if len(user_with_telephone) != 0:
            return "Аккаунт с таким номером телефона существует"

        if len(name) == 0 or len(telephone) == 0 or len(password) == 0:
            return "Не заполнены все данные"

        else:
            return "Успешно"

        connect.close()