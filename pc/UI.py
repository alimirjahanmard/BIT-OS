#it's UI
import keyboard
import time
import os
#it's for BIT-OS shell input
aui = "BITOS>>"
#it's for welcome text
def wui():
    print("wlecome to BITOS")
#it's for wlecome helping text
def hui() : 
    print("you can use (help) for helping in any time")
#it's help text
def htui():
    #add your app name in help
    print("(clock) for see time")
    print("(file manager) for run file manager")
#it's false command error
def fceui() :
    print("this command it's false")
#it's for clear screen
def csui():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")