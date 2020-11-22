import json
import os
class UserStorage():
    def __init__(self, full_path):
        self.full_path = full_path
        if not os.path.isfile(full_path):
            with open(full_path,'w') as f:
                f.write("[]")

    def create(self, name, password):
        if not self.found_copy_acc(name):        
            print("no copy acc")
            old_data = self.get()
            UID = self.get_UID()
            new_element = {
                'name': name,
                'password': password,
                "UID": UID
            }
        
            old_data = self.get()
            old_data += [new_element]
            self.write(old_data)


            print(UID)
            return UID
        else:
            return "found_copy_account"

    def delete(self, UID):
        data = self.get()
        for index, user in enumerate(data):
            if user["UID"] == UID:
                del data[index]
        self.write(data)

    def get(self):
        with open(f'{self.full_path}') as f:
            return json.load(f)
        
    def write(self,data):
        with open(f'{self.full_path}','w') as f:
            json.dump(data, f, indent = 4)

    def return_UID(self, name, password):
        data = self.get()
        for index, user in enumerate(data):
            if user["name"] == str(name):
                if user["password"] == str(password):
                    return user["UID"]
                    break
                else:
                    return "Неверный пароль"
                    break
        else:
            UID = self.create(name, password)
            return UID
                

    def found_copy_acc(self, name):
        data = self.get()
        for index, user in enumerate(data):
            if user["name"] == str(name):
                return True
                break
        else:
            return False

    def get_UID(self):
        data = self.get()
        UID = 0
        for index, user in enumerate(data):
            if int(user["UID"]) >= int(UID):
                UID = int(user["UID"]) + 1
        return UID

#print(UserStorage("./static/_data/users.json").found_copy_acc("ololoev"))