#bitos it's os for run on esp32(micropython)
#this file it's kernel
import os
import time
#this importion fo app
import esp32.TIME as TIME
import esp32.FILEMANAGER as FILEMANAGER
print("wlecome to BITOS")
print("can use (help) in any time")
while True:       
    bitq = input("BITOS>>")
    if bitq == "help" :
        print("(clock) for see time")
        print("(file manager) for run file manager")
    elif bitq == "clock":
        print(TIME.CTIME)
    elif bitq == "file manager":
        FILEMANAGER.fm()                
    else:
        print("this command it's false")