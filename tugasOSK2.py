from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os


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
            inputHexa.set(value)
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
    if(int(ord(list(ascii)[0]))<=255):
        for i in list(ascii):
            value = value + bin(ord(i))[2:].zfill(8)
        inputBiner.set(value)
        value = ''
        for i in list(ascii):
            value = value + (hex(ord(i))[2:])
        inputHexa.set(value)
    else:
        messagebox.showwarning("Input Karakter/Huruf Salah", "Karakter tidak dikenal")
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

def logout():
    root.destroy()
    os.system('python3 tugasOSK.py')


root = Tk()
root.title("Program Konversi")

firstframe = ttk.Frame(root, padding='3 3 12 12')
firstframe.grid(column = 0, row=0, sticky=(N, W, E, S))
firstframe.columnconfigure(0, weight=1)
firstframe.rowconfigure(0, weight=1)

inputKalimat = StringVar()
inputBiner = StringVar()
inputHexa = StringVar()

#password textbox dan label
ttk.Label(firstframe, text="Kalimat").grid(row=6, sticky=(N))
kalimatBox = ttk.Entry(firstframe, width=25, textvariable = inputKalimat)
kalimatBox.grid(row=7, sticky=(N))
kalimatBox.pack()

#password textbox dan label
ttk.Label(firstframe, text="Biner").grid(row=8, sticky=(N))
binerBox = ttk.Entry(firstframe, width=25, textvariable = inputBiner)
binerBox.grid(row=9, sticky=(N))
binerBox.pack()

#password textbox dan label
ttk.Label(firstframe, text="Hexadesimal").grid(row=10, sticky=(N))
hexaBox = ttk.Entry(firstframe, width=25, textvariable = inputHexa)
hexaBox.grid(row=11, sticky=(N))
hexaBox.pack()

#button konversi
button1=ttk.Button(firstframe, text="Konversi", command=konversi).grid(row=12, sticky=(E))
#button clear
button1=ttk.Button(firstframe, text="Clear", command=clear).grid(row=12, sticky=(W))

button1=ttk.Button(firstframe, text="Logout", command=logout).grid(row=13, sticky=(E,W))

for child in firstframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
