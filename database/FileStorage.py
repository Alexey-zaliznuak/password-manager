from database._utils import *
class FileStorage():
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
        CREATE TABLE files(
        path TEXT,
        name TEXT,
        UID INT,
        UUID PRIMARY KEY);
        """)
        connect.commit()
        connect.close()

    def get_folders_files(self, path:str, UID:int):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"""SELECT name FROM {self.table} WHERE path = {path} and UID = {UID}
        """).fetchall()

        connect.commit()
        connect.close()

    def delete_file(self, UUID):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"""
        DELETE * FROM {self.table} UUID = {UUID}
        """).fetchall()

        connect.commit()
        connect.close()

    def update_file(self, name:str, path:str, UUID):
        #update name and path, choose file by UUID

        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"""UPDATE {self.table} SET NAME = {name} AND PATH = {path} where UUID = {UUID}""")

        connect.commit()
        connect.close()
