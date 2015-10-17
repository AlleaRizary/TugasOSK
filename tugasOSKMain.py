from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def openLoginWindow():
    cabang = Toplevel(root)
    cabang.title("Halaman Login")
    cabang.geometry("800x600")


def exitProgram():
    exit()

root = Tk()
root.title("Program Konversi")
root.geometry("600x480")
root.option_add('*tearOff', FALSE)

win = Toplevel(root)
menubar = Menu(win)
win['menu'] = menubar

menu_file=Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')


menu_file.add_command(label="Program Konversi", command=openLoginWindow)
menu_file.add_command(label="Exit", command=exitProgram)


root.mainloop()
