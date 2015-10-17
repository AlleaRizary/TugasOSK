#import modul tkinter, tkinter.tk (menggantikan widgets lama

from tkinter import *
from tkinter.ttk import *

#-----------***---------------------------#
#    Class utama, tempat menjalankan      #
# program pertama kali untuk memunculkan  #
# frame aplikasi                          #
#-----------------------------***---------#

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.createMainWindow()

    def createMainWindow(self):
        self.master.title("Aplikasi Konversi Biner, Hexa dan Huruf")
        self.pack(fill=BOTH, expand=1)
        #membuat menu bar#
        mainMenu = Menu(self.master)
        self.master.config(menu=mainMenu)

        #membuat objek menu bar "File" dan menu lainnya #
        file = Menu(mainMenu)
        file.add_command(label="Program Konversi", command=self.openNewWindow)
        file.add_command(label="Exit", command=self.exitProgram)

        #menambahkan file ke dalam menu utama
        mainMenu.add_cascade(label="File", menu=file)

    def exitProgram(self):
        exit()

    def openNewWindow(self):
        branchPK = Toplevel(self)
        branchPK.wm_title("Program Konversi")
        branchPK.geometry("600x400")

# Membuat jendela utama.
if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    app=Application(root)
    root.mainloop()
