from database._utils import *
class UserStorage():
    def __init__(self, file, table_name):
        init(self, file, table_name)

    def write(self, name, password, telephone):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        
        data = cursor.execute(f"""
        select UID from {self.table} WHERE name = '{name}'""").fetchall()
        if len(data) == 0:
            data = f"""INSERT INTO {self.table} (name, password, telephone, date_change) VALUES ("{name}", "{password}", "{telephone}", "{current_time(self)}")"""
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


    def get(self):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        
        return cursor.execute(f"PRAGMA table_info(users)").fetchall(), cursor.execute(f"select * from users").fetchall()
        connect.close()

    def get_by_data(self, name, password, telephone, create):
        print(password)

        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        data = cursor.execute(f"""
        select UID from {self.table} WHERE name = '{name}'""").fetchall()

        #типо нет колонки с названием password :(
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
#m = UserStorage("./database/_data/mydatabase.db", "users").write("Admin", "65444", "00000000000")