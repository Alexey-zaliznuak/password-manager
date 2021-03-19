from database._utils import *
class AccountStorage():
    def __init__(self, file, table_name):
        init(self, file, table_name)

    def write(self, email, service, password, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        data = f"""INSERT INTO {self.table} (service, email, password, date_change, UID) VALUES ("{service}", "{email}", "{password}", "{current_time(self)}", "{UID}")"""

        cursor.execute(data)
        connect.commit()
        connect.close()

    def delete(self, ac_id, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"DELETE FROM {self.table} WHERE UID = {UID} AND ID = {ac_id}")
        connect.commit()
    
    
    def update(self, service, email, password, ac_id, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        exe = f"""UPDATE {self.table} SET service = '{service}', email = '{email}', password = '{password}', date_change = '{current_time(self)}' WHERE UID = {UID} AND id = {ac_id}"""
        cursor.execute(exe)
        connect.commit()

    def get_by_UID(self, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        return cursor.execute(f"select * from {self.table} WHERE UID = {UID}").fetchall()
        connect.close()