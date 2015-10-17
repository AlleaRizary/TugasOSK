#import fungsi TkInter untu GUI programming

from tkinter import *
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
def inputKalimat(ubahOrdo, a):
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
    hasil = inputKalimat(ubahOrdo(num, 7, 0, 7), 1)
    print("Hexanya adalah =")
    for i in list(hasil):
        print(hex(ord(i))[2:], end="")
    print()
    print("Kalimatnya adalah")
    print(hasil)
    print()

#Fungsi fromHexadecimal adalah fungsi yang menerima masukan berupa bilangan
#hexadesimal dan mengubahnya ke dalam bentuk biner dan Huruf (gabungan Huruf)
def fromHexadecimal(hexa):
    num = bin(int(hexa,16))
    hasil = inputKalimat(ubahOrdo(num, 2, 2, 9),0)
    kalimat = inputKalimat(ubahOrdo(hasil, 7, 0, 7), 1)
    print("Binernya adalah =",)
    print(hasil)
    print()

    print("Kalimatnya adalah=",)
    print(kalimat)
    print()

#Fungsi fromAscii adalah fungsi yang menerima masukan berupa Huruf
#(gabungan Huruf) dan mengubahnya ke dalam bentuk Hexa dan Biner
def fromAscii(ascii):
    print("Binernya adalah =",)
    for i in list(ascii):
        print(bin(ord(i))[2:].zfill(7), end="")
    print()
    print("Hexanya adalah =",)
    for i in list(ascii):
        print(hex(ord(i))[2:], end="")
    print()

#menghilangkan tampilan mainmenu
def hide_me():
    widget.grid_forget()
#verifikasi password yang diketik berdasarkan ID
def checkPassword(*args):
    print('Test')
#pop-up menu register ID untuk mendaftarkan user baru
def registerID():
    print("test")    
    #hide_me()
    #registerPage = Tk()
    #registerPage.title("Daftar User Baru")
    #registerPage.geometry("800x600")
    #registerPage.mainloop() 
#Fungsi menu digunakan untuk menampilkan layar pilihan program konversi
#def menu():
#    print ("Program konversi bilangan")
#    print ("Pilih [1] untuk input bilangan biner")
#    print ("Pilih [2] untuk input bilangan hexadesimal")
#    print ("Pilih [3] untuk input huruf (kalimat)")
#    i=int(input("Masukkan pilihan anda :"))
#    if i==1:
#        angka=input("Masukkan bilangan biner :")
#        fromBinary(angka)
#    elif i==2:
#        angka=input("Masukkan bilangan hexadesimal :")
#        fromHexadecimal(angka)
#    elif i==3:
#        angka=input("Masukkan huruf(kalimat) :")
#        fromAscii(angka)
#    else:
#        print ("Pilihan anda salah");
#menu()

#def loginMenu():
root = Tk()
root.title("Program Konversi")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

loginID = StringVar()
loginPW = StringVar()

#login textbox dan label
ttk.Label(mainframe, text="Login: ").grid(row=1, sticky=(N))
loginBox = ttk.Entry(mainframe, width=25, textvariable = loginID)
loginBox.grid(row=2, sticky=(N))
#password textbox dan label
ttk.Label(mainframe, text="Password: ").grid(row=3, sticky=(N))
loginBox = ttk.Entry(mainframe, width=25, textvariable = loginPW)
loginBox.grid(row=4, sticky=(N))
#button login
button1=ttk.Button(mainframe, text="Login", command=checkPassword).grid(row=5, sticky=(E))

#button daftar
button2=ttk.Button(mainframe, text="Daftar", command=registerID).grid(row=5, sticky=(W))
#button2.bind('<Button-1>', registerID)

#password textbox dan label
ttk.Label(mainframe, text="Kalimat").grid(row=6, sticky=(N))
kalimatBox = ttk.Entry(mainframe, width=25, textvariable = loginPW)
kalimatBox.grid(row=7, sticky=(N))

#password textbox dan label
ttk.Label(mainframe, text="Biner").grid(row=8, sticky=(N))
binerBox = ttk.Entry(mainframe, width=25, textvariable = loginPW)
binerBox.grid(row=9, sticky=(N))

#password textbox dan label
ttk.Label(mainframe, text="Hexadesimal").grid(row=10, sticky=(N))
hexaBox = ttk.Entry(mainframe, width=25, textvariable = loginPW)
hexaBox.grid(row=11, sticky=(N))

#button daftar
button3=ttk.Button(mainframe, text="Konversi", command=registerID).grid(row=12, sticky=(E,W))
#
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#def registerID(*args):
#    print("test")    
#    button2=button2.get()
#    if button2.bind('<Button-1>') == True:
#        button2.bind('<Button-1>',hide_me)
#    registerPage = Tk()
#    registerPage.title("Daftar User Baru")
#    registerPage.geometry("800x600")
#    registerPage.mainloop() 
#
#loginMenu()

root.mainloop()
