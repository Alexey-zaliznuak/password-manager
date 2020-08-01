import json
import os

class DataBase():
    def __init__(self, full_path):
        self.full_path = full_path

        if not os.path.isfile(full_path):
            with open(full_path,'w') as f:
                f.write("[]")
        
    def get(self):
        with open(f'{self.full_path}') as f:
            return json.load(f)
        
    def write(self,data):
        with open(f'{self.full_path}','w') as f:
            json.dump(data,f,indent=4)
        
    def update(self, new_element = None):
        el_id = new_element["id"]
        data = self.get()
        for index,string in enumerate(data):
            if string["id"] == el_id:
                data[index] = new_element
        self.write(data)

    def delete(self, el_id):
        data = self.get()
        for index,string in enumerate(data):
            if string["id"] == el_id:
                del data[index]
        self.write(data)
    def create(self, data):
        old_data = self.get()
        max_element = max(old_data, default={'id': 0}, key=lambda element: int(element['id']))
        max_id = int(max_element["id"]) 
        id_of_password  = max_id + 1

        data_new = {
        'service':f"{Service}",
        'email':f"{Email}",
        'password':f"{Password}",
        'data_of_mod':f"{mod_time}",
        'id':f"{id_of_password}"
        }
        
        old_data += [data_new]
        data = old_data
        database.write(data)