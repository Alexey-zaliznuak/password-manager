import json
import os
from datetime import datetime

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
        new_element['data_of_create'] = current_time()
        data = self.get()
        for index,string in enumerate(data):
            if string["id"] == el_id:
                data[index] = new_element
        self.write(data)

    def delete(self, el_id):
        data = self.get()
        for index, string in enumerate(data):
            if string["id"] == el_id:
                del data[index]
        self.write(data)

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

    def find_id(self, data):
        max_element = max(data, default={'id': 0}, key=lambda element: int(element['id']))
        max_id = int(max_element["id"]) 
        id  = max_id + 1
        return id

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