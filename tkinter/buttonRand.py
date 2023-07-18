# Importing tkinter module
from tkinter import *
# Importing random module
import random
from random import shuffle
 
# Creating a tkinter window
root = Tk()
root.title("Random Position")

# Initialize tkinter window with dimensions 
root.geometry('600x450')


#set window color
root.configure(bg='blue')


 
# Creating a Button
btn = Button(root, text = 'Click me !')
btn.pack()
 
#colors
colorlist = ["red", "green", "blue", "grey","violet","brown","cyan"]

# Defining method on click
def Clicked(event):
    x = random.randint(0,250)
    y = random.randint(0,200)
    btn.place(x=x, y=y)
    shuffle(colorlist)
    root.configure(bg=colorlist[0])
     
     
# bind button
btn.bind("<Button-1>" ,Clicked)
btn.pack()
 
root.mainloop()