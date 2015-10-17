#import fungsi TkInter untu GUI programming

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Fungsi ubahOrdo berguna untuk merubah input dalam bentuk string
#menjadi bentuk array yang sudah dibagi-bagi sesuai dengan jenisnya
#yaitu biner atau hexadesimal.
def ubahOrdo(num, ordo, depan, belakang):
    ubahString = []
    for i in range (int(len(num)/ordo)):
        for j in range (1):
            ubahString.insert(i,num[depan:belakang])
        if ordo ==7:
            depan +=7
            belakang +=7
        else:
            depan +=8
            belakang +=8
    return ubahString

#Fungsi inputKalimat berguna untuk menggabungkan elemen-elemen data
#yang terdapat dalam nilai kembalian dari fungsi ubahOrdo
def inputanKalimat(ubahOrdo, a):
    kalimat = ''
    for i in range (len(ubahOrdo)):
        if a == 0:
            kalimat = kalimat + ubahOrdo[i]
        else:
            kalimat = kalimat + chr(int(ubahOrdo[i],2))
    return kalimat

#Fungsi fromBinary adalah fungsi yang menerima masukan berupa bilangan
#biner dan mengubahnya ke dalam bentuk Hexa dan Huruf (gabungan Huruf)
def fromBinary(num):
    try:
        if(len(num)>=7):
            if((int(num[0:1])==1) or (int(num[0:1])==0)):
                kalimat = inputanKalimat(ubahOrdo(num, 7, 0, 7), 1)
                value = ''
                for i in list(kalimat):
                    value = value + (hex(ord(i))[2:])
                inputHexa.set(value)
                inputKalimat.set(kalimat)
            else:
                messagebox.showwarning("Input Biner salah", "Harap memasukkan angka 1 atau 0 kedalam kotak Biner")
        else:
            messagebox.showwarning("Input Biner salah", "Harap memasukkan 7 angka Biner (Tambahkan 0 didepan angka yang jumlahnya dibawah 7)")
    except ValueError:
        messagebox.showwarning("Input Biner salah", "Harap memasukkan angka 1 atau 0 dalam kolom Biner")
#Fungsi fromHexadecimal adalah fungsi yang menerima masukan berupa bilangan
#hexadesimal dan mengubahnya ke dalam bentuk biner dan Huruf (gabungan Huruf)
def fromHexadecimal(hexa):
    value = ''
    for i in range(int(len(hexa)/2)):
        for j in range(1):
            value = value + int()
    binernya = inputanKalimat(ubahOrdo(hexa, 2, 2, 9),0)
    kalimat = inputanKalimat(ubahOrdo(hexa, 7, 0, 7), 1)
    inputBiner.set(binernya)
    inputKalimat.set(kalimat)

#Fungsi fromAscii adalah fungsi yang menerima masukan berupa Huruf
#(gabungan Huruf) dan mengubahnya ke dalam bentuk Hexa dan Biner
def fromAscii(ascii):
    value = ''
    for i in list(ascii):
        value = value + bin(ord(i))[2:].zfill(8)
    inputBiner.set(value)
    value = ''
    for i in list(ascii):
        value = value + (hex(ord(i))[2:])
    inputHexa.set(value)

#menghilangkan tampilan mainmenu
def hide_me():
    widget.grid_forget()

#verifikasi password yang diketik berdasarkan ID
def checkPassword(*args):
    print('Test')

#pop-up menu register ID untuk mendaftarkan user baru
def registerID():
    print("test")

def clear():
    inputKalimat.set('')
    inputBiner.set('')
    inputHexa.set('')

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
root = Tk()
root.title("Program Konversi")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


loginID = StringVar()
loginPW = StringVar()
inputKalimat = StringVar()
inputBiner = StringVar()
inputHexa = StringVar()


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

#password textbox dan label
ttk.Label(mainframe, text="Kalimat").grid(row=6, sticky=(N))
kalimatBox = ttk.Entry(mainframe, width=25, textvariable = inputKalimat)
kalimatBox.grid(row=7, sticky=(N))

#password textbox dan label
ttk.Label(mainframe, text="Biner").grid(row=8, sticky=(N))
binerBox = ttk.Entry(mainframe, width=25, textvariable = inputBiner)
binerBox.grid(row=9, sticky=(N))
binerBox.pack()

#password textbox dan label
ttk.Label(mainframe, text="Hexadesimal").grid(row=10, sticky=(N))
hexaBox = ttk.Entry(mainframe, width=25, textvariable = inputHexa)
hexaBox.grid(row=11, sticky=(N))
hexaBox.pack()

#button konversi
button3=ttk.Button(mainframe, text="Konversi", command=konversi).grid(row=12, sticky=(E))
#button clear
button3=ttk.Button(mainframe, text="Clear", command=clear).grid(row=12, sticky=(W))
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()
