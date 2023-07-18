#calculette
import math
#import tkinter
from tkinter import *

def calcule(ev):
    print(ev)
    #print(input1.get())
    #label.configure(text="pouet")
    label.configure(text=str(eval(input1.get())))
    input1.configure(text="1")

win = Tk()
win.title('Calculette')

input1=Entry(win)
input1.bind('<Return>', calcule)
input1.pack()


label=Label(win)
label.pack()

#btnQuit=Button()
#btnQuit.pack()



win.mainloop()


