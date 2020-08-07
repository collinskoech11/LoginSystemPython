from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root = Tk()
    app = SalesLogin(root)


class SalesLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Management Login System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='cadet blue')
        self.frame = Frame(self.master, bg='cadet blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text='Sales Management System', font=('arial', 60, 'bold'), bg='cadet blue', fg='Cornsilk')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

        def Login_System(self):
            user = (self.Username.get())
            pas = (self.Password.get())
            if(user == str(coko) and pas == str (1234567)):
                self.Login_window()
            else:
                tkinter.messagebox.askyesno("Sales Management Login System","Invalid Login Details")
                self.Username.set("")
                self.Password.set("")


        def Login_window(self ):
            self.SaleWindow = Toplevel(self.master)
            self.app = SalesManagement(self.saleWindow)


class SalesManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Management Login System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='cadet blue')
        self.frame = Frame(self.master, bg='cadet blue')
        self.frame.pack()


if __name__ == '__main__':
    main()
