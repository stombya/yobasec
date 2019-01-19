
#import the gui module tkinter
from tkinter import *
import tkinter as tk

#creates an instance
root = Tk()

#A title for out Gui
root.title( "CyPat")


def newuser():
    userentry = Entry(root)
    userentry2= Entry(root)
    
    userlabel= tk.Label(text="User")
    passwordlabel = tk.Label(text="Password")
    
    userentry.grid()
    userentry2.grid()
    userlabel.grid(row=2, column=1)
    passwordlabel.grid(row=3,column=1)

def usercreation():
    
    #creates label
    userlabel= tk.Label(root, text="User Creation")
   
    #creates Button,assigns string, binds a function to the button
    userbutton=tk.Button(root, text="Create User", height = 1, width = 15)
    #configs the button so a textbox can be pulled up
    userbutton.config(command=newuser*2,text="Users")
    
    #button to add text boxes
    addmoreusers=tk.Button(root,text="+",bg="blue")
    #butto to decrease the amount of text boxes
    lessusers=tk.Button(root,text="-",bg="red")
    
    #positions the label and button on the grid
    lessusers.grid(row=1,column=2)
    addmoreusers.grid(row=1,column=1)
    userlabel.grid(row=0,  column=0)
    userbutton.grid(row=1, column=0)


    #packs the label/button to be displayer on the gui

usercreation()



#starts the gui, creates a loop
root.mainloop()



