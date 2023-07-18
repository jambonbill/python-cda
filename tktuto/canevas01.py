#using class
from tkinter import *
from random import randrange

#initalise vars
w=800
h=600

class App():    
    
    
    COLORS=['purple','cyan','maroon','green','red','blue','orange','yellow']

    x1,y1,x2,y2=0,0,0,0    

    def __init__(self,canvas) -> None:
        
        self.canvas=canvas
        
        self.x0=0
        self.y0=0
        self.x1=100
        self.y1=100
        
        self.changeColor()

    def changeColor(self):
        self.color=self.COLORS[randrange(0,7)]        
        #self.color-

    def tracer(self):                       
        canvas.create_line(self.x0,self.y0,self.x1,self.y1,fill=self.color, width=10)
        self.x0=self.x1
        self.y0=self.y1
        self.x1=randrange(0,w)
        self.y1=randrange(0,h)
        self.changeColor()



root = Tk()


#create canvas
canvas=Canvas(root, width=w, height=h)
canvas.pack(side=LEFT)

app = App(canvas)

#trace line
btn1=Button(root,text="Tracer", command=app.tracer)
btn1.pack()

btn2=Button(root,text="Changer")
btn2.pack(side=RIGHT)

btn3=Button(root,text="Quitter", command=root.destroy)
btn3.pack(side=BOTTOM)



root.mainloop()

