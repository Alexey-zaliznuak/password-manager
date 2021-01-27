from database._utils import *
class FolderStorage():
    def __init__(self, file, table_name):
        init(self, file, table_name)

    def write(self, path:str, name:str, UID:int):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        data = f"""INSERT INTO {self.table} (path, name, UID, UUID) VALUES 
        ("{path}", "{name}", "{UID}", "{uuid1()}")
        """
        connect.commit()
        connect.close()

    def create_table(self):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        
        cursor.execute(f"""
        CREATE TABLE folders(
        path TEXT,
        name TEXT,
        UID INT,
        UUID PRIMARY KEY);
        """)
        connect.commit()
        connect.close()

    def get_folders_name(self, path:str, UID:int):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"""SELECT name FROM {self.table} WHERE path = {path} and UID = {UID}
        """).fetchall()

        connect.commit()
        connect.close()

    def delete_folder(self, UUID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"""
        DELETE * FROM {self.table} WHERE UUID = {UUID}
        """).fetchall()

        connect.commit()
        connect.close()

    def update_folder(self, name:str, path:str, UUID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"""UPDATE {self.table} SET NAME = {name} AND PATH = {path} where UUID = {UUID}""")

        connect.commit()
        connect.close()