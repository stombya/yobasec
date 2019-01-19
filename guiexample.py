from tkinter import *
import subprocess
import threading
import os
import platform
import re


#------------------------------------

def addBox():
    print ("ADD")

    frame = Frame(root)
    frame.pack()

    Label(frame, text='User').grid(row=0, column=0)

    usr1 = Entry(frame)
    usr1.grid(row=1, column=0)

    Label(frame, text='Password').grid(row=0, column=1)

    paswd1 = Entry(frame)
    paswd1.grid(row=1, column=1)

    subprocess.call(r'net user ' + usr1 + " " + paswd1 + ' /add', shell = True)

    all_entries.append( (usr1, paswd1) )

#------------------------------------

def showEntries():

    for number, (usr1, paswd1) in enumerate(all_entries):
        print (number, usr1.get(), paswd1.get())

#------------------------------------

all_entries = []

root = Tk()

showButton = Button(root, text='Show all text', command=showEntries)
showButton.pack()

addboxButton = Button(root, text='Add Users', fg="Blue", command=addBox)
addboxButton.pack()

root.mainloop()

#------------------------------------
