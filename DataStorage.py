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
#3)delete +
#4)caugth -
#5)create +
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
    
        old_data = self.get()
        complete = False
        for index, dict_data in enumerate(old_data):
            for index_data, string_data in enumerate(dict_data):
                if int(string_data["UID"]) == int(UID): 
                    print("вариант 1")                       
                    old_data[index]+=[new_element]
                    complete = True
                    break
                    
        if not complete:
            print("вариант 2")
            old_data.append([new_element])
            print(old_data)
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
        for index, string in enumerate(data):
            for element in string:
                #print(element)
                if int(element["id"]) >= int(min_id):
                    min_id = int(element["id"]) + 1
        return min_id 

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
        for index, dict_data in enumerate(data):
            for index_data, string_data in enumerate(dict_data):
                print(string_data)
                if int(string_data["id"]) == int(f_id):
                    if int(string_data["UID"]) == int(UID):
                        print("delete\n",data,"\n","index=",index,"index_data=",index_data)
                        del data[index][index_data]
                else:
                    print(int(string_data["id"]),int(f_id))
        self.write(data) 
#ac = JsonStorage("./static/_data/data.json")
#ac.create("zaliznuak_new","goooooooogle", "qwertyuio", 3)