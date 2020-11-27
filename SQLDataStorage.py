import sqlite3
from random import randint
from datetime import datetime

#storage.create_table("accounts", "(service TEXT, email TEXT, password TEXT, id INT, date_change TEXT, uid INT)")
#storage.write("accounts", ('f','g','h','i','g','k'))
#storage.delete("accounts", "id" , "'i'")
#storage.get_all_data("accounts"))

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
    
    def write(self, email, service, password, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        ac_id = self.get_minimal_id()
        data = (service, email, password, ac_id, self.current_time(), UID)

        cursor.execute(f"INSERT INTO {self.table} VALUES (?,?,?,?,?,?)", data)
        connect.commit()
        connect.close()

    def delete(self, UID, id):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"DELETE FROM {self.table} WHERE UID = {UID} AND ID = {id}")
        connect.commit()

    def get_minimal_id(self):
        return randint(0, 100000)

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
