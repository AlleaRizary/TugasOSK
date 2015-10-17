#import fungsi TkInter untu GUI programming

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *

import os
import sys
import time

#create root
root = Tk()
root.style = Style()
root.style.theme_use('clam')
root.title("Program Konversi")

#program_konversi.withdraw()
root.geometry("600x480+250+50")
root.option_add('*tearOff', FALSE)

def main():
    root.mainloop()

s = ttk.Style()
s.theme_use('clam')
s.configure('TButton', font='helvetica 8')
s.configure('Root.TLabel', font='helvetica 16', foreground='blue', justify='center')
s.configure('Isi.TLabel', font='helvetica 10', foreground='blue', justify='left')


menubar = Menu(root)
root.config(menu=menubar)
menu_file=Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')

loginID = StringVar()
loginPW = StringVar()
inputKalimat = StringVar()
inputBiner = StringVar()
inputHexa = StringVar()
idDaftar = StringVar()
passDaftar = StringVar()

#fungsi ubahDecimal berguna untuk melakukan konversi input Hexadesimal dan Biner kedalam Desimal
#untuk kemudian di cocokan dengan table ASCII
def ubahDecimal(nilaimasukan, ordo, depan, belakang):
    hasildesimaltemp = []
    hasildesimal = []
    awal = depan
    akhir = belakang
    if ordo == 16:
        for i in range(int(len(nilaimasukan)/2)):
            for j in range(1):
                hasildesimaltemp.insert(i, nilaimasukan[awal:akhir])
                if(int(hasildesimaltemp[i],16)<32):
                    messagebox.showwarning("Input Hexa salah", "Harap memasukkan Hexa dengan kelipatan 2 antara 20 sampai FF")
            awal +=2
            akhir +=2
        for i in range(len(hasildesimaltemp)):
            hasildesimal.insert(i, chr(int(hasildesimaltemp[i],ordo)))
        return hasildesimal
    if ordo == 2:
        for i in range(int(len(nilaimasukan)/8)):
            for j in range(1):
                hasildesimaltemp.insert(i, nilaimasukan[awal:akhir])
            awal +=8
            akhir +=8
        for i in range(len(hasildesimaltemp)):
            hasildesimal.insert(i, chr(int(hasildesimaltemp[i],ordo)))
        return hasildesimal

#Fungsi fromBinary adalah fungsi yang menerima masukan berupa bilangan
#biner dan mengubahnya ke dalam bentuk Hexa dan Huruf (gabungan Huruf)
def fromBinary(biner):
    try:
        if(len(biner) % 8 == 0):

            value = ''
            kalimatnya = ubahDecimal(biner,2,0,8)
            for i in range(len(kalimatnya)):
                value = value + kalimatnya[i]
            inputKalimat.set(value)

            value = ''
            for i in kalimatnya:
                value = value + (hex(ord(i))[2:])
            inputHexa.set(value.upper())
        else:
            messagebox.showwarning("Input Biner salah", "Harap hanya memasukkan angka 1 dan 0 sejumlah kelipatan 8 Biner (Tambahkan 0 didepan angka yang bukan kelipatannya 8)")
    except ValueError:
        messagebox.showwarning("Input Biner salah", "Harap memasukkan angka 1 atau 0 dalam kolom Biner")
#Fungsi fromHexadecimal adalah fungsi yang menerima masukan berupa bilangan
#hexadesimal dan mengubahnya ke dalam bentuk biner dan Huruf (gabungan Huruf)
def fromHexadecimal(hexa):
    if((len(hexa)%2 == 0) and (int(hexa,16)>=32)):
        value = ''
        kalimatnya = ubahDecimal(hexa,16,0,2)
        for i in range(len(kalimatnya)):
            value = value + kalimatnya[i]
        inputKalimat.set(value)

        value = ''
        for i in kalimatnya:
            value = value + bin(ord(i))[2:].zfill(8)
        inputBiner.set(value)
    else:
        messagebox.showwarning("Input Hexa salah", "Harap memasukkan Hexa dengan kelipatan 2 antara 20 sampai FF")


#Fungsi fromAscii adalah fungsi yang menerima masukan berupa Huruf
#(gabungan Huruf) dan mengubahnya ke dalam bentuk Hexa dan Biner
def fromAscii(ascii):
    value = ''
    try:
        if(int(ord(list(ascii)[0]))<=255):
            for i in list(ascii):
                value = value + bin(ord(i))[2:].zfill(8)
            inputBiner.set(value)
            value = ''
            for i in list(ascii):
                value = value + (hex(ord(i))[2:])
            inputHexa.set(value.upper())
        else:
            messagebox.showwarning("Input Karakter/Huruf Salah", "Karakter tidak dikenal")
    except IndexError:
        messagebox.showwarning("Input Karakter/Huruf Salah", "Text box tidak boleh kosong")
#tombol clear
def clear():
    inputKalimat.set('')
    inputBiner.set('')
    inputHexa.set('')

#tombol konversi
def konversi():
    nilaiKalimat = inputKalimat.get()
    nilaiBiner = inputBiner.get()
    nilaiHexa = inputHexa.get()
    if((nilaiBiner =='') and (nilaiHexa =='')):
        fromAscii(nilaiKalimat)
    elif((nilaiKalimat =='') and (nilaiHexa =='')):
        fromBinary(nilaiBiner)
    elif((nilaiKalimat =='') and (nilaiBiner =='')):
        fromHexadecimal(nilaiHexa)
    else:
        messagebox.showwarning("Input Satu Kolom Saja", "Harap mengisi 1 kolom saja")



def showProgramKonversi():
        inputKalimat.set('')
        inputBiner.set('')
        inputHexa.set('')
        program_konversi = Toplevel(root)
        program_konversi.geometry('+450+263')
        program_konversi.title("Program Konversi")
        firstframe = ttk.Frame(program_konversi, padding='3 3 12 12')
        firstframe.grid(column = 0, row=0, sticky=(N, W, E, S))
        firstframe.columnconfigure(0, weight=1)
        firstframe.rowconfigure(0, weight=1)
        def logout():
            program_konversi.destroy()
	#password textbox dan label
        ttk.Label(firstframe, text="Kalimat").grid(row=6, sticky=(N))
        kalimatBox = ttk.Entry(firstframe, width=25, textvariable = inputKalimat)
        kalimatBox.grid(row=7, sticky=(N))


	#password textbox dan label
        ttk.Label(firstframe, text="Biner").grid(row=8, sticky=(N))
        binerBox = ttk.Entry(firstframe, width=25, textvariable = inputBiner)
        binerBox.grid(row=9, sticky=(N))


	#password textbox dan label
        ttk.Label(firstframe, text="Hexadesimal").grid(row=10, sticky=(N))
        hexaBox = ttk.Entry(firstframe, width=25, textvariable = inputHexa)
        hexaBox.grid(row=11, sticky=(N))


	#button konversi
        button1=ttk.Button(firstframe, text="Konversi", command=konversi).grid(row=12, sticky=(E))
	#button clear
        button1=ttk.Button(firstframe, text="Clear", command=clear).grid(row=12, sticky=(W))

        button1=ttk.Button(firstframe, text="Logout", command=logout).grid(row=13, sticky=(E,W))

        for child in firstframe.winfo_children(): child.grid_configure(padx=5, pady=5)


	
def ambilIdPassDariFile(username, password):
	print('test')
	
	
#pop-up menu register ID untuk mendaftarkan user baru
def registerID():
    

    regis = Toplevel(root)
    regis.title("Daftar Baru")
    regis.geometry('+450+320')
    def insertID():
        iduser = idDaftar.get()
        passuser = passDaftar.get()
        passuserbin = ''
        for i in list(passuser):
                passuserbin = passuserbin + bin(ord(i))[2:].zfill(8)
        try:
            dbId = open('credentials.txt', 'a')
            dbId.write(iduser + '\t' + passuserbin +'\n')
            dbId.close()
        except IOError:
            dbId = open('credentials.txt', 'w')
        idDaftar.set('')
        passDaftar.set('')
        messagebox.showinfo('Pendaftaran Berhasil', 'Selamat anda telah terdaftar dengan username : ' + iduser)
    def backtoMain():
        regis.withdraw()
    
    secondframe = ttk.Frame(regis, padding="3 3 12 12")
    secondframe.grid(column=0, row=0, sticky=(N, W, E, S))
    secondframe.columnconfigure(0, weight=1)
    secondframe.rowconfigure(0, weight=1)

    #login textbox dan label
    ttk.Label(secondframe, text="Username yang diinginkan: ").grid(row=1, sticky=(N))
    loginBox = ttk.Entry(secondframe, width=25, textvariable = idDaftar)
    loginBox.grid(row=2, sticky=(N))
    #password textbox dan label
    ttk.Label(secondframe, text="Password yang diinginkan: ").grid(row=3, sticky=(N))
    loginBox = ttk.Entry(secondframe, width=25, textvariable = passDaftar, show ='*')
    loginBox.grid(row=4, sticky=(N))
    #button login
    button1=ttk.Button(secondframe, text="Daftarkan", command=insertID).grid(row=5, sticky=(E))

    #button daftar
    button2=ttk.Button(secondframe, text="Batal", command=backtoMain).grid(row=5, sticky=(W))
    #button2.bind('<Button-1>', registerID)


    for child in secondframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	
#verifikasi password yang diketik berdasarkan ID
def checkPassword():
    usrPass = loginPW.get()
    if(usrPass == 'admin'):        
        loginID.set('')
        loginPW.set('')
        showProgramKonversi()

    else:
        loginID.set('')
        loginPW.set('')
        messagebox.showwarning("Password Salah", "Harap memasukkan password yang benar")

def openLoginWindow():
        login_konversi = Toplevel(root)
        login_konversi.geometry('+450+350')
        login_konversi.title("Halaman Login")
        mainframe = ttk.Frame(login_konversi, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
	
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
        #button2=ttk.Button(mainframe, text="Daftar", command=registerID).grid(row=5, sticky=(W))

	
def exitProgram():
    exit()

def tampilanDepan():
    rootframe = ttk.Frame(root)
    judul = ttk.Label(rootframe, text='Selamat Datang di Program Konversi Biner\n', style='Root.TLabel', padding='0 60 0 0')
    isi = ttk.Label(rootframe, text='1. Untuk masuk kedalam program konversi, anda harus login terlebih dahulu.\n2. Login details ID = Admin, Pass = Admin\n \
        ', style='Isi.TLabel', padding='0 0 0 0')
    judul.pack()
    isi.pack()
    panedtime = ttk.Panedwindow(rootframe, orient=VERTICAL)
    noteDesimal = ttk.Labelframe(panedtime, text='Desimal', width=150, height=150)
    noteBiner = ttk.Labelframe(panedtime, text='Biner', width=150, height=150)
    noteHexa = ttk.Labelframe(panedtime, text='Hexa', width=150, height=150)
    panedtime.add(noteDesimal)
    panedtime.add(noteBiner)
    panedtime.add(noteHexa)
    panedtime.pack()
    def updateTimeText():
        jam = bin(int(time.strftime("%H")))[2:].zfill(6)
        menit = bin(int(time.strftime("%M")))[2:].zfill(6)
        detik = bin(int(time.strftime("%S")))[2:].zfill(6)
        current = time.strftime("%H:%M:%S")
        current2 = "{}:{}:{}".format(jam,menit,detik)
        current3 = "{}:{}:{}".format(hex(int(jam,2))[2:],hex(int(menit,2))[2:],hex(int(detik,2))[2:]).upper()
        timeText.configure(text=current)
        timeBiner.configure(text=current2)
        timeHexa.configure(text=current3)
        root.after(1000, updateTimeText)
    timeText = ttk.Label(noteDesimal, text='', font=("Helvetica",25))
    timeBiner = ttk.Label(noteBiner, text='', font=("Helvetica",25))
    timeHexa = ttk.Label(noteHexa, text='', font=("Helvetica",25))
    timeText.pack()
    timeBiner.pack()
    timeHexa.pack()
    updateTimeText()
    rootframe.pack(fill=BOTH, expand=YES)
    

menu_file.add_command(label="Program Konversi", command=openLoginWindow)
menu_file.add_command(label="Exit", command=exitProgram)

tampilanDepan()
main()
