# -*- coding: utf-8 -*-
import sys
import codecs
import csv
import time
from tkinter import *
from tkinter import messagebox
if sys.stdout.encoding != 'cp850':
  sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')

pencere = Tk()
pencere.title("AKYUVARYUM")
pencere.geometry("400x500")

#ZAMAN AYARI
zaman = Frame(pencere)
zaman.grid()
# Ay Basamak Kontrolu
if(int(time.localtime()[1])<=9):
    bugun="Bugünün Tarihi: "+str(time.localtime()[2])+".0"+str(time.localtime()[1])+"."+str(time.localtime()[0])
    gun = str(time.localtime()[2]) + ".0" + str(time.localtime()[1]) + "." + str(time.localtime()[0])
else:
    bugun = "Bugünün Tarihi: " + str(time.localtime()[2]) + "." + str(time.localtime()[1]) + "." + str(time.localtime()[0])
    gun = str(time.localtime()[2]) + "." + str(time.localtime()[1]) + "." + str(time.localtime()[0])

etiket = Label(zaman,text=bugun,fg="green",font=("GARAMOND",12))
etiket.grid(padx=110, pady=10,columnspan=1)

# Tarih Kutucugu
tarih = Frame(pencere)
tarih.grid()

L1 = Label(tarih, text="Tarihi Giriniz")
L1.grid(padx=110, pady=10)
# Kutucuk içi tarihi
v = StringVar(pencere, value=gun)
E1 = Entry(tarih, bd=4,bg="#FFFFE0", fg="green",font=("Fixedysy",12),textvariable=v)
E1.grid(padx=110, pady=3)

tarih = Frame(pencere)
tarih.grid()

# TÜR Kutucugu
tur=Frame(pencere)
tur.grid()

label_4 = Label(pencere, text="Tür:",width=20,font=("bold", 10))
label_4.grid(padx=110, pady=3)

list1 = ['Yerli','Red Grass','Blue Grass','Half Blue','Koi',"Fil Kulak Mozaik","Full Red",'Vatoz','Çöpçü','Yeni'];
E2=StringVar()
droplist=OptionMenu(pencere,E2, *list1)
droplist.config(width=15,bg="#99ff00",fg="dark blue")
E2.set('Balık Türleri')
droplist.grid(padx=110, pady=3)

# SAYI Kutucugu
sayi=Frame(pencere)
sayi.grid()

L3 = Label(sayi, text="Sayıyı Giriniz")
L3.grid(padx=1, pady=1)

E3 = Entry(sayi, bd=4,font=("helvetica",12),bg="#FFFFE0",fg="dark blue")
E3.grid(padx=110, pady=3)

kayıt = Frame(pencere)
kayıt.grid()

def dialog():
    tarih = E1.get()
    tur   = E2.get()
    sayi  = E3.get()
    if (len(tarih) < 9):
        var = messagebox.showerror("Uyarı!", "Geçerli Tarih Giriniz.")
    elif ((tur) == "Balık Türleri"):
        var = messagebox.showwarning("Uyarı!", "Balık Türünü Seçiniz.")
    elif(len(sayi)== 0):
        var = messagebox.showwarning("Uyarı!", "Balık Sayısını Giriniz.")
    else:
        var = messagebox.askquestion("Kaydedilmek Üzere...","Girdiğiniz Veriler Kaydedilecek, Devam edilsin mi?")


    dizi = []
    if(var=="yes"):
        var = messagebox.showinfo("Kayıt","Kayıt Başarılı...")
        if ((tur) == "Red Grass"):
            with open('Red Grass.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Yerli"):
            with open('Yerli.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Blue Grass"):
            with open('Blue Grass.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Koi"):
            with open('Koi.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Half Blue"):
            with open('Half Blue.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Fil Kulak Mozaik"):
            with open('Fil Kulak Mozaik.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Full Red"):
            with open('Full Red.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Yeni"):
            with open('Yeni.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Vatoz"):
            with open('Vatoz.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
        if ((tur) == "Çöpçü"):
            with open('Çöpçü.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih: " + tarih +"  ",sayi," Adet "+tur ])
    elif(var=="no"):
        var = messagebox.showinfo("Kayıt", "Kayıt Başarısız...")

button1 = Button(kayıt, text=" Kaydet ",font=("bold",11), width=15, command=dialog, fg="black",bg="#F0E68C")
button1.grid(padx=110, pady=40)

kayıt = Frame(pencere)
kayıt.grid()

sayi_yrl = 0
with open('Yerli.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        sayi_yrl = int(row[1]) + sayi_yrl
    L4 = Label(sayi, text="Karışık: " + str(sayi_yrl))

sayi_hb=0
with open('Half Blue.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        sayi_hb=int(row[1])+sayi_hb
    L4 = Label(sayi,text="Half Blue: "+str(sayi_hb))

sayi_bg = 0
with open('Blue Grass.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        sayi_bg = int(row[1]) + sayi_bg
    L4 = Label(sayi, text="Blue Grass: " + str(sayi_bg))


pencere1 = Tk()
pencere1.title("Balıklarım")
pencere1.geometry("300x400")

sayi_yrl = 0
with open('Yerli.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        sayi_yrl = int(row[1]) + sayi_yrl
    L4 = Label(pencere1, text="Yerli:             " + str(sayi_yrl), font=("gothic", 12))
    L4.grid(padx=0, pady=0)

sayi_rg = 0
with open('Red Grass.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        sayi_rg = int(row[1]) + sayi_rg
    L4 = Label(pencere1, text="Red Grass:         " + str(sayi_rg), font=("gothic", 12))
    L4.grid(padx=1, pady=1)

sayi_bg = 0
with open('Blue Grass.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_bg = int(row[1]) + sayi_hb
        L4 = Label(pencere1, text="Blue Grass:        " + str(sayi_hb), font=("gothic", 12))
        L4.grid(padx=1, pady=1)

sayi_hb = 0
with open('Half Blue.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_hb = int(row[1]) + sayi_hb
        L4 = Label(pencere1, text="Half Blue:        " + str(sayi_hb), font=("gothic",12))
        L4.grid(padx=1, pady=1)

sayi_koi = 0
with open('Koi.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_koi = int(row[1]) + sayi_koi
        L4 = Label(pencere1, text="Koi:              " + str(sayi_koi), font=("gothic", 12))
        L4.grid(padx=1, pady=1)

sayi_fkm = 0
with open('Fil Kulak Mozaik.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_fkm = int(row[1]) + sayi_fkm
        L4 = Label(pencere1, text="Fil Kulak Mozaik:   " + str(sayi_hb), font=("gothic", 12))
        L4.grid(padx=1, pady=1)

sayi_fr = 0
with open('Full Red.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_fr = int(row[1]) + sayi_fr
        L4 = Label(pencere1, text="Full Red:          " + str(sayi_fr), font=("gothic", 12))
        L4.grid(padx=1, pady=1)

sayi_vtz = 0
with open('Vatoz.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_vtz = int(row[1]) + sayi_vtz
        L4 = Label(pencere1, text="Vatoz:              " + str(sayi_vtz), font=("gothic", 12))
        L4.grid(padx=1, pady=1)

sayi_cp = 0
with open('Çöpçü.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_cp = int(row[1]) + sayi_cp
        L4 = Label(pencere1, text="Çöpçü:             " + str(sayi_cp), font=("gothic", 12))
        L4.grid(padx=1, pady=1)

sayi_yeni = 0
with open('Yeni.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sayi_yeni = int(row[1]) + sayi_yeni
        L4 = Label(pencere1, text="Yeni:              " + str(sayi_yeni), font=("gothic", 12))
        L4.grid(padx=1, pady=1)

# formu çizme
pencere.mainloop()
pencere1.mainloop()