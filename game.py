import random
import os, sys
# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";
print ""
print ""

print B+"Permainan : Batu Gunting Kertas"
print W+"Pembuat Permainan BY:"
print G+"=================================================="
print W+"///////////       //////          /////"
print W+"   ///    //  // //  // //////   // // /// // ///"
print W+"  ///    //  // ////// //  //   // // /// // ///"
print W+" ///    ////// //  // //  //   ///// //////////"
print G+"=================================================="
print W+"Contact:081335497168"
print G+"NB:-Program ilegal"
print G+"   -leh gae onggel+sue"
print G+"   -sebelum main baca doa dulu ya!!!"
print ""
print O+"Pilihan :"
print ""
print G+"1. Batu"
print R+"2. Gunting"
print O+"3. Kertas"

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)
def permainan ():
    kamu = int(input("masukan pilihanmu: "))
    kom = random.choice(["Batu", "Gunting", "Kertas"])
    if kamu == 1:
        print G+"kamu     : Batu"
        print("komputer :", kom)
        if kom == "Batu":
            print B+"\tDraw"
        if kom == "Gunting":
            print G+"\tLu menang"
        if kom == "Kertas":
            print R+"\tlu kalah"
    if kamu == 2:
        print W+"kamu     : Gunting"
        print("komputer :", kom)
        if kom == "Batu":
            print R+"\tKamu kalah"
        if kom == "Batu":
            print R+"\tKamu kalah"
        if kom == "Gunting":
            print B+"\tDraw"
        if kom == "Kertas":
            print G+"\tLu menang"
    if kamu == 3:
        print W+"Kamu    : Kertas"
        print("komputer :", kom)
        if kom == "Batu":
            print G+"\tLu menang"
        if kom == "Gunting":
            print R+"\tLu kalah"
        if kom == "Kertas":
            print B+"\tDraw"
    if kamu >=4:
        print R+"pilihanmu salah!!!"
        restart()
permainan()
restart()
try:
        permainan()
except KeyboardInterrupt:
        os.system('clear')
        restart()
