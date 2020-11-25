import sqlite3


#storage.create_table("accounts", "(service TEXT, email TEXT, password TEXT, id INT, date_change TEXT, uid INT)")
#storage.write("accounts", ('f','g','h','i','g','k'))
#storage.delete("accounts", "id" , "'i'")
#storage.get_all_data("accounts"))

class DataStorage():
    def __init__(self, file):
        self.file = file
        connect = sqlite3.connect(str(file))

    def create_table(self, table_name, args):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()
        cursor.execute(f"CREATE TABLE {table_name} {args}")
        
    def get_all_data(self, table_name):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        return cursor.execute(f"select * from {table_name}").fetchall()
        connect.close()
    
    def write(self, table_name, data):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"INSERT INTO accounts VALUES (?,?,?,?,?,?)", data)
        connect.commit()
    
    def delete(self, table_name, args, args_value):
        connect = sqlite3.connect(str(self.file))
        cursor = connect.cursor()

        cursor.execute(f"DELETE FROM {table_name} WHERE {args} = {args_value}")
        connect.commit()
    
storage = DataStorage("mydatabase.db")