# Importing tkinter module
from tkinter import *
from tkinter import messagebox


# Creating a tkinter window
root = Tk()
 
root.title("Random Position")

# Initialize tkinter window with dimensions 
root.geometry('600x450')

def test():
    print("test")
    messagebox.showwarning("title","texte youpi")

# Creating a Button
btn1 = Button(root, text = 'btn1 !', command=test)
btn1.pack()

root.mainloop()

print("??")
exit(0)
