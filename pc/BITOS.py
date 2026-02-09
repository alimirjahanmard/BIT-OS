#bitos it's os for run on esp32(micropython)
#this file it's kernel
import os
import time
import UI
#this importion fo app
import TIME
import FILEMANAGER
UI.wui()
UI.hui()
UI.csui()
while True:       
    bitq = input(UI.aui)
    #for run and processing input
    #(UI.csui()) it's for clear screen use this
    if bitq == "help" :
        UI.csui()
        UI.htui()
    elif bitq == "clock":
        UI.csui()
        TIME.ctime()
    elif bitq == "file manager":
        UI.csui()
        FILEMANAGER.fm()                
    else:
        UI.csui()
        UI.fceui()