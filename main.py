from tkinter import *
from tkinter.ttk import Combobox
import DataBase

class Read():
    def __init__(self):
        #Window
        global window_reader
        window_reader = Tk()
        window_reader.title("Найти пароль")  
        window_reader.geometry('800x250')
        window_reader.resizable(width=False, height=False)

        #Combobox

        fontExample = ("Courier", 9, "bold")

        combo = Combobox(window_reader, font = fontExample, state = "readonly", width = 111)  
        combo['values'] = ("Секунду","Ненайдено")  
        combo.current(0)  # установите вариант по умолчанию  
        combo.pack()
        combo.place(x = 0,y = 0)
        values = []
        data_of_mod = []
        database = DataBase.DataBase(f'{os.path.dirname(os.path.abspath(__file__))}\\data.json')
        data = database.get()
        for elements in data:
            values += [elements]

        combo['values'] = tuple(values)
        combo.current(0)  # установите вариант по умолчанию  
        combo.pack()
        combo.place(x = 0,y = 0)
        window_reader.mainloop()


class Create():
    def __init__(self):
        #Window
        global window_creater
        window_creater = Tk()
        window_creater.title("Создать пароль")  
        window_creater.geometry('450x200')
        window_creater.resizable(width=False, height=False)

        #Label

        self.Email_label = Email_label = Label(window_creater, text = "Email:")
        self.Servise_label = Servise_label = Label(window_creater, text = "Servise:")
        self.Password_label = Password_label = Label(window_creater, text = "Password:")

        self.Email_label.pack()
        self.Servise_label.pack()
        self.Password_label.pack()

        self.Servise_label.place(x = 0, y = 0)
        self.Email_label.place(x = 0, y = 30)
        self.Password_label.place(x = 0, y = 60)

        #Entry

        self.Email_entry = Email_entry = Entry(window_creater,width=200) 
        self.Servise_entry = Servise_entry = Entry(window_creater,width=200) 
        self.Password_entry = Password_entry = Entry(window_creater,width=200, show = "*")

        self.Email_entry.pack()
        self.Servise_entry.pack()
        self.Password_entry.pack()
        
        self.Servise_entry.place(x = 60, y = 0)
        self.Email_entry.place(x = 60, y = 30)
        self.Password_entry.place(x = 60, y = 60)

            
        #Button 

        self.Create_button = Create_button = Button(window_creater, text="Create",font="Times=20",pady=8,padx=90,command=self.save)
        self.Cancel_button = Cancel_button = Button(window_creater, text="Cancel",font="Times=20",pady=8,padx=90,command=self.cancel)

        self.Create_button.pack()
        self.Cancel_button.pack()

        self.Create_button.place(x=0, y = 155)
        self.Cancel_button.place(x=220, y = 155)


        window_creater.mainloop()

    def save(self):
        Email = self.Email_entry.get()
        Service = self.Servise_entry.get()
        Password = self.Password_entry.get()

        database = DataBase.DataBase(f"{os.path.dirname(os.path.abspath(__file__))}\\data.json")
        database.create(Service, Email, Password)
        window_creater.destroy()

    def cancel(self):
        window_creater.destroy() 


class hello_Window():
    def __init__(self):
        global window, Create
        window = Tk()
        window.title("Тут типо крутое имя")  
        window.geometry('700x500')
        window.resizable(width=False, height=False)

        
        self.menu = Menu(window)  
        self.new_item = Menu(self.menu)  
        self.new_item.add_command(label='создать пароль' ,command=self.create)
        self.new_item.add_command(label='удалить пароль' ,command=self.delete)  
        self.new_item.add_command(label='найти пароль' ,command=self.see) 
        self.menu.add_cascade(label='Функции', menu=self.new_item) 
        window.config(menu=self.menu)
        self.new_item = Menu(self.menu, tearoff=0)

    
        self.now_label = now_label = Label(window, text=f"КУУУУ-КУУУУ", font="Times 20",fg="grey")  
        now_label.pack()
        now_label.place(x=0, y=40)

        #User{
        #google{"email":'qwertyuiop',"password":'qwertyuiop', "date_of_create":"data hz but data"}
        #}



        times = datetime.now()
        day = times.day
        hour = times.hour
        minute = times.minute

        if len(str(minute)) < 2:
            minute = f"0{minute}"

        if len(str(hour)) < 2:
            hour = f"0{hour}"

        weather = ""

        self.hello_label = hello_label = Label(window, text=f"{hour}:{minute}", font="Times 20", fg="grey")  
        hello_label.pack()
        hello_label.place(x=0, y=0)

        self.updates()
        
        window.mainloop()

    def create(self):    
        Create()

    def delete(self):
        pass

    def see(self):
        Read()

    def updates(self):
        global window
        times = datetime.now()
        hour = times.hour
        minute = times.minute

        if len(str(minute)) < 2:
            minute = f"0{minute}"

        if len(str(hour)) < 2:
            hour = f"0{hour}"

        #self.hello_label.config(text=f"{hour}:{minute}")
        window.after(1000, self.updates)

start = hello_Window()