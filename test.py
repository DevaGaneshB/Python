from Tkinter import *
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
top1 = Tkinter.Tk()
# Code to add widgets will go here...


L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)




def helloCallBack():
    
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top1, text ="Hello", command = helloCallBack)
B.pack()


top.mainloop()



