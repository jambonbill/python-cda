#frame
#frame permet de grouper des elements, et aussi de creer de nouveaux widgets
import math
from tkinter import *


def showPosition(ev):
    label.config(text=str(ev))
    #print(ev)

win = Tk()
win.title('Frame')

frame=Frame(win, background='grey', width=640, height=480)
frame.bind('<Button-1>',showPosition)
frame.bind('<Button-2>',showPosition)
frame.bind('<Button-3>',showPosition)
frame.bind('<Motion>',showPosition)
frame.bind('<MouseWheel>',showPosition)
#frame.bind('<Key-a>',showPosition)
#frame.bind('<KeyPress>',showPosition)
frame.pack()



label=Label(win)
label.pack()

win.mainloop()
