import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Pizza Order System Code
#önce tkinter ile bir arayüz tasarlanabilir
#pizza fiyatları ve sos fiyatları belirlenecek, her pizza için 1 sos hakkıyla toplanacak
#toplanan bütün para tek bir yere gönderilecek ve ödeme internetten yapılacak
#kullanıcı verisi çekilecek ve onaylamak için geri dönüş sağlanacak

root = tk.Tk()
root.title("Pizza Order System")
root.geometry("350x225")

nameLabel = Label(root, width=18, height=3, text="First name :", font="Times 10 bold")
nameLabel.place(x=2,y=6)

srNameLabel = Label(root, width=18, height=3, text="Last Name :", font="Times 10 bold")
srNameLabel.place(x=2,y=36)

phoneLabel = Label(root, width=18, height=3, text="Phone Number :", font="Times 10 bold")
phoneLabel.place(x=2,y=66)

nameEntry = Entry(root, width= 30)
nameEntry.place(x=120, y=25)

srNameEntry = Entry(root, width= 30)
srNameEntry.place(x=120, y=55)

phoneEntry = Entry(root, width= 30)
phoneEntry.place(x=120, y=85)

def userControl():
    if nameEntry.get() == "Firstname" and srNameEntry.get() == "Surname" and phoneEntry.get() == "01234567890":
        tk.messagebox.showinfo("Successful", "You are being redirected...")
        exit()
    else:
        tk.messagebox.showinfo("Failed!", "Login again...")    
ctrlButton = Button(root, text="Login", width="10", command=userControl)
ctrlButton.place(x=135, y=150)

root.mainloop()