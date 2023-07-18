from tkinter import *
from random import randrange

#initalise vars
w=800
h=600

x1,y1,x2,y2=0,0,100,100

colors=['purple','cyan','maroon','green','red','blue','orange','yellow']
color='blue'



def tracer():
    global w,h
    global x1,y1,x2,y2
    global colors
    global color
    
    color=colors[randrange(0,7)]
    
    canvas.create_line(x1,y1,x2,y2,fill=color, width=12)
    x1=x2
    y1=y2
    x2=randrange(0,w)
    y2=randrange(0,h)


root = Tk()

#create canvas
canvas=Canvas(root, width=w, height=h)
canvas.pack(side=LEFT)

#trace line
btn1=Button(root,text="Tracer", command=tracer)
btn1.pack()

btn2=Button(root,text="Changer")
btn2.pack(side=RIGHT)

btn3=Button(root,text="Quitter", command=root.destroy)
btn3.pack(side=BOTTOM)

for i in range(100):
    tracer()


root.mainloop()

