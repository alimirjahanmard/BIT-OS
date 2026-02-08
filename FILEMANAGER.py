import os
def fm():
    print("welcome to file manager")
    print("can use (help) in any time")
    while True:
        fmq = input("file manager>>")
        if fmq == "help":
            print("(file list) for see file in this path")
            print("(open) for open file")
        elif fmq == "file list":
            print("\n".join (os.listdir()))
        elif fmq == "open":
             rfname = input("file name>>")
             rfread=open(rfname, "r")
             rfread.read
             print(rfread.read())
             rfread.close()
        elif fmq == "exit":
            break
        else:
            print("this command it's false")