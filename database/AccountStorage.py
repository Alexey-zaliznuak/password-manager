from database._utils import *
class AccountStorage():
    def __init__(self, file, table_name):
        init(self, file, table_name)

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

    def get_by_UID(self, UID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        return cursor.execute(f"select * from {self.table} WHERE UID = {UID}").fetchall()
        connect.close()