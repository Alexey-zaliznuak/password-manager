from JsonStorage import JsonStorage
from datetime import datetime
def current_time():
    times = datetime.now()
    day = times.day
    hour = times.hour
    minute = times.minute
    year = times.year
    month = times.month
    
    if len(str(minute)) < 2:
        minute = f"0{minute}"

    if len(str(hour)) < 2:
        hour = f"0{hour}"

    mod_time = f"{year}/{month}/{day}/{hour}/{minute}"

    return mod_time
class DataBase_account(JsonStorage):
    def __init__(self, full_path):
        self.full_path = full_path
        JsonStorage.__init__(self, self.full_path)
    def create(self, service, email, password):
        old_data = self.get()
        id_of_password = self.find_id(old_data)

        data_new = {
            'service':f"{service}",
            'email':f"{email}",
            'password':f"{password}",
            'data_of_mod':f"{current_time()}",
            'data_of_create':f"{current_time()}",
            'id':f"{id_of_password}"
        }
        
        data = old_data + [data_new]
        self.write(data)
class DataBase_users(JsonStorage):
    def __init__(self, full_path):
        self.full_path = full_path
        JsonStorage.__init__(self, self.full_path)
    def create(self, username, email, password):
        old_data = self.get()
        id_of_user = self.find_id(old_data)

        data_new = {
            'username':f"{username}",
            'email':f"{email}",
            'password':f"{password}",
            'id':f"{id_of_user}"
        }
        
        data = old_data + [data_new]
        self.write(data)