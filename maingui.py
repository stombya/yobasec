
#import the gui module tkinter
import tkinter as tk

#creates an instance
win = tk.Tk()

#A title for out Gui
win.title( "CyPat Windows LTHS")


def qf():
    print

def usercreation():
    
    #creates label
    userlabel= tk.Label(win, text="User Creation")
   
    #creates Button,assigns string, binds a function to the button
    userbutton=tk.Button(win, text="Create Users",command=qf())
    
    #positions the label and button on the grid
    userlabel.grid(row=0,  column=0)
    userbutton.grid(row=1, column=0)


    #packs the label/button to be displayer on the gui

usercreation()



#starts the gui, creates a loop
win.mainloop()



