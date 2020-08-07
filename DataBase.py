from JsonStorage import JsonStorage
class DataBase_account(JsonStorage):
    def __init__(self, full_path):
        self.full_path = full_path
        JsonStorage.__init__(self.full_path)
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
        JsonStorage.__init__(self.full_path)
    def create(self, username, email, password):
        old_data = self.get()
        id_of_account = self.find_id(old_data)

        data_new = {
            'username':f"{service}",
            'email':f"{email}",
            'password':f"{password}",
            'id':f"{id_of_password}"
        }
        
        data = old_data + [data_new]
        self.write(data)