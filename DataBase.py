import json
class DataBase():
    def __init__(self, full_path):
        self.full_path = full_path
    def get(self):
        with open(f'{self.full_path}') as f:
            return json.load(f)
    def write(self,data):
        with open(f'{self.full_path}','w') as f:
            json.dump(data,f,indent=4)
    def update(self, el_id, new_element = None):
        data = self.get()
        for element in data:
            if element["id"] == int(el_id):
                data[element] = new_element
        self.write(data)
    def delete(self, el_id):
        data = self.get()
        for index,string in enumerate(data):
            if string["id"] == el_id:
                del d[index]
        self.write(data)