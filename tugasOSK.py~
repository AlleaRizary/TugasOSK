#import fungsi TkInter untu GUI programming

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys

#menghilangkan tampilan mainmenu
def hide_me():
    widget.grid_forget()



root = Tk()
root.title("Program Konversi")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

loginID = StringVar()
loginPW = StringVar()

#pop-up menu register ID untuk mendaftarkan user baru
def registerID():
    def insertID():
        print("Id didaftarkan")
    def backtoMain():
        regis.destroy()
        if(sys.platform=='darwin'):
            os.system('python3 tugasOSK.py')
        elif(sys.platform=='win32'):
            os.system('python tugasOSK.py')
        else:
            os.system('python tugasOSK.py')

    root.destroy()
    regis = Tk()
    regis.title("Daftar Baru")

    secondframe = ttk.Frame(regis, padding="3 3 12 12")
    secondframe.grid(column=0, row=0, sticky=(N, W, E, S))
    secondframe.columnconfigure(0, weight=1)
    secondframe.rowconfigure(0, weight=1)

    #login textbox dan label
    ttk.Label(secondframe, text="Login: ").grid(row=1, sticky=(N))
    loginBox = ttk.Entry(secondframe, width=25, textvariable = loginID)
    loginBox.grid(row=2, sticky=(N))
    #password textbox dan label
    ttk.Label(secondframe, text="Password: ").grid(row=3, sticky=(N))
    loginBox = ttk.Entry(secondframe, width=25, textvariable = loginPW, show ='*')
    loginBox.grid(row=4, sticky=(N))
    #button login
    button1=ttk.Button(secondframe, text="Daftarkan", command=insertID).grid(row=5, sticky=(E))

    #button daftar
    button2=ttk.Button(secondframe, text="Batal", command=backtoMain).grid(row=5, sticky=(W))
    #button2.bind('<Button-1>', registerID)


    for child in secondframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    regis.mainloop()
#verifikasi password yang diketik berdasarkan ID
def checkPassword():
    usrPass = loginPW.get()
    if(usrPass == 'admin'):
        root.destroy()
        if(sys.platform=='darwin'):
            os.system('python3 tugasOSK2.py')
        elif(sys.platform=='win32'):
            os.system('python tugasOSK2.py')
        else:
            os.system('python tugasOSK2.py')


    else:
        loginID.set('')
        loginPW.set('')
        messagebox.showwarning("Password Salah", "Harap memasukkan password yang benar")

#login textbox dan label
ttk.Label(mainframe, text="Login: ").grid(row=1, sticky=(N))
loginBox = ttk.Entry(mainframe, width=25, textvariable = loginID)
loginBox.grid(row=2, sticky=(N))
#password textbox dan label
ttk.Label(mainframe, text="Password: ").grid(row=3, sticky=(N))
loginBox = ttk.Entry(mainframe, width=25, textvariable = loginPW, show ='*')
loginBox.grid(row=4, sticky=(N))
#button login
button1=ttk.Button(mainframe, text="Login", command=checkPassword).grid(row=5, sticky=(E))

#button daftar
button2=ttk.Button(mainframe, text="Daftar", command=registerID).grid(row=5, sticky=(W))
#button2.bind('<Button-1>', registerID)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
