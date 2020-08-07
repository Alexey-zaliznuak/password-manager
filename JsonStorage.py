import json
import os
from datetime import datetime
class JsonStorage():
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
    
    def delete(self, el_id):
        data = self.get()
        for index, string in enumerate(data):
            if string["id"] == el_id:
                del data[index]
        self.write(data)

    def found(self, id):
        data = self.get()
        for index,string in enumerate(data):
            if string["id"] == el_id:
                return data[index]

    def find_id(self,data):
        max_element = max(data, default={'id': 0}, key=lambda element: int(element['id']))
        max_id = int(max_element["id"]) 
        id  = max_id + 1
        return id

    def current_time(self):
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