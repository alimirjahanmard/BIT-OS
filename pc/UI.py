#it's UI
import keyboard
import time
import os
import APP_API
#it's for clear screen
def csui():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
#it's for BIT-OS shell input
def aui() :
    global bitq
    bitq = input("BITOS>>")
#it's for welcome text
def wui():
    print("BIT-OS v0.1")
    print("wlecome to BITOS")
#it's for wlecome helping text
def hui() : 
    print("you can use (help) for helping in any time")
#it's help text
def htui():
    APP_API.apph()
#it's false command error
def fceui() :
    print("this command it's false")