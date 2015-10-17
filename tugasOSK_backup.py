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

def binertohexatoascii(num):
    hasil = inputKalimat(ubahOrdo(num, 7, 0, 7), 1)
    print("Hexanya adalah =")
    for i in list(hasil):
        print(hex(ord(i))[2:], end="")
    print()
    print("Kalimatnya adalah")
    print(hasil)
    print()

def hexatoasciitobiner(hexa):
    num = bin(int(hexa,16))
    hasil = inputKalimat(ubahOrdo(num, 2, 2, 9),0)
    kalimat = inputKalimat(ubahOrdo(hasil, 7, 0, 7), 1)
#    ubahString = []
#    depan = 2
#    belakang = 9
#    for i in range (int(len(hexa)/2)):
#        for j in range(1):
#            ubahString.insert(i, num[depan:belakang])
#        depan +=8
#        belakang +=8
#    biner1 =''
#    for i in range (len(ubahString)):
#        biner1 = biner1 + ubahString[i]
    print("Binernya adalah =",)
    print(hasil)
    print()

    print("Kalimatnya adalah=",)
    print(kalimat)
    print()
#    ubahKalimat = []
#    depan = 0
#    belakang = 7
#    for i in range (int(len(biner1)/7)):
#        for j in range (1):
#            ubahKalimat.insert(i,biner1[depan:belakang])
#        depan +=7
#        belakang +=7
#    kalimat =''
#    for i in range (len(ubahKalimat)):
#        kalimat=kalimat + chr(int(ubahKalimat[i],2))


def asciitobinertohexa(ascii):

    print("Binernya adalah =",)
    for i in list(ascii):
        print(bin(ord(i))[2:].zfill(7), end="")
    print()
    print("Hexanya adalah =",)
    for i in list(ascii):
        print(hex(ord(i))[2:], end="")
    print()

def menu():
    print ("Program konversi bilangan")
    print ("Pilih [1] untuk input bilangan biner")
    print ("Pilih [2] untuk input bilangan hexadesimal")
    print ("Pilih [3] untuk input bilangan desimal")
    i=int(input("Masukkan pilihan anda :"))
    if i==1:
        x=input("Masukkan bilangan biner :")
        binertohexatoascii(x)
    elif i==2:
        x=input("Masukkan bilangan hexadesimal :")
        hexatoasciitobiner(x)
    elif i==3:
        x=input("Masukkan bilangan desimal :")
        asciitobinertohexa(x)
    else:
        print ("Pilihan anda salah");

menu()
