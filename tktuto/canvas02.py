#using class,
#Jeu du pendu vers 1
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

from random import random, randrange


#initalise vars
w=800
h=600



class Pendu():    
    

    def __init__(self,canvas) -> None:
        
        self.canvas=canvas
        
        self.step=0
        self.x0=0
        self.y0=0
        self.x1=0
        self.y1=0

        

    def next(self):                       
        
        self.step = self.step+1
        print('next')
        print(self.step)
        
        
        
        #self.randLetter()

        if self.step==1:
            line(0,500,100,500)
        
        if self.step==2:
            line(50,500,50,200)
        
        if self.step==3:
            line(50,500,50,200)
        
        if self.step==4:
            line(50,200,250,200)
        
        if self.step==5:#barre de renfort            
            line(50,250,100,200)
        
        if self.step==6:#corde            
            line(250,200,250,230)

        if self.step==7:#tete
            cercle(250,250,20)
        
        if self.step==8:#corp
            line(250,270,250,350)

        if self.step==9:#bras
            line(200,290,300,290)

        if self.step==10:#jambe1
            line(250,350,200,400)
        
        if self.step==11:#jambe2
            line(250,350,300,400)
            
        if self.step==12:#erection
            line(250,350,270,330)
            messagebox.showinfo("showinfo", "Pendu!!")

        if self.step>12:
            #Add image to the Canvas Items
            self.canvas.create_image(randrange(0,400),randrange(0,400),anchor=NW,image=png)
        
        


def cercle(x, y, r, coul ='black', width=5):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=coul, width=10)


def line(x0,y0,x1,y1):
    canvas.create_line(x0,y0,x1,y1,fill='black', width=10)


root = Tk()

#Load an image in the script
png= ImageTk.PhotoImage(Image.open("png/dab.png"))

#create canvas
canvas=Canvas(root, width=w, height=h)
canvas.pack(side=LEFT)

app = Pendu(canvas)

#trace line
btn1=Button(root,text="Next", command=app.next)
btn1.pack()



btn3=Button(root,text="Quitter", command=root.destroy)
btn3.pack(side=BOTTOM)



root.mainloop()

