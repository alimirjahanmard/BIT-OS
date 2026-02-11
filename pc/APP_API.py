import UI
import BITOS
import TIME
import FILEMANAGER
#print your app name here(in def apph)
def apph():
    print("(file manager) for run file manager")
    print("(clock) for run clock")
def apr():
    #it's app runer
    if UI.bitq == "help" :
        UI.csui()
        UI.htui()
    elif UI.bitq == "clock":
        UI.csui()
        TIME.ctime()
    elif UI.bitq == "file manager":
        UI.csui()
        FILEMANAGER.fm()
    else:
        UI.csui()
        UI.fceui()