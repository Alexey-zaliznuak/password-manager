from datetime import datetime
import json
import os

#[0]-->service
#[1]-->email
#[2]-->password
#[3]-->id
#[4]-->date_changes
#[5]-->UID

#1)see    +
#2)detail +
#3)delete -
#4)caugth -
#5)create +

def format_request_data(string):
    num = 0
    pars = False
    service = ""
    email = ""
    password = ""
    id_account = ""
    date_changes = ""
    UID = ""
    for i in string:
        if i == '"' or i == "'":
            num += 1
            continue
        if num == 3:
            service += i
            continue
        if num == 7:
            email += i
            continue
        if num == 11:
            password += i
            continue
        if  num == 15:
            id_account += i 
            continue
        if num == 19:
            date_changes += i
            continue
        if num == 22:
            if i == ":":
                pars = True
                continue
            if pars and i != " " and i !="}":
                UID += i
    return [service, email, password, id_account, date_changes, UID]
class JsonStorage():
    def __init__(self, full_path):
        self.full_path = full_path

        if not os.path.isfile(full_path):
            with open(full_path,'w') as f:
                f.write("[]")
        old_data = self.get()
        for index, data in enumerate(old_data):
            if len(data) == 0:
                del old_data[index]
        self.write(old_data)
    def create(self, email, service, password, UID):
        old_data = self.get()
        new_element = {
            'service': service,
            'email': email,
            'password': password,
            "id": str(self.found_min_id(UID)),
            "date_changes": self.current_time(),
            "UID": int(UID)
        }
        if self.found_min_id(int(UID)) > 0:
            old_data[int(UID)] += [new_element]
        else:
            print("вариант 2", new_element)
            old_data.append([new_element])
        self.write(old_data)

    def get(self):
        with open(f'{self.full_path}') as f:
            return json.load(f)
        
    def write(self,data):
        with open(f'{self.full_path}','w') as f:
            json.dump(data, f, indent = 4)

    def find_id(self, found_id):
        data = self.get()
        for index, dict_data in enumerate(data):
            if dict_data["id"] == str(found_id):
                return index
    
    def found_min_id(self, UID):
        data = self.get()
        min_id = 0
        if len(data) > int(UID):
            for index, dict_data in enumerate(data[int(UID)]):
                if int(dict_data["id"]) >= int(min_id):
                    min_id = int(dict_data["id"]) + 1
            return min_id 
        else:
            return 0

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

    def delete(self, UID, f_id):
        data = self.get()
        f_id = f_id
        for index, dict_data in enumerate(data[UID]):
            if int(dict_data["id"]) == int(f_id):
                del data[UID][index]
        self.write(data) 