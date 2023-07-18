
# Importing tkinter module
from tkinter import *       
 
# Creating a tkinter window
root = Tk()
 

# Initialize tkinter window
# with dimensions 300 x 250            
root.geometry('300x250')    
 
# Creating a Button
btn1 = Button(root, text = 'btn1 !',
              command = root.destroy)
btn1.grid(row = 0, column = 0)
 
# Creating a Button
btn2 = Button(root, text = 'btn2 !', command = root.destroy)
btn2.grid(row = 1, column = 1)
 
# Creating a Button
btn3 = Button(root, text = 'btn3 !', command = root.destroy)
btn3.grid(row = 2, column = 2)
 
# Creating a Button
btn3 = Button(root, text = 'btn4 !', command = root.destroy)
btn3.grid(row = 4, column = 4)
 
for y in range(0,8):
    for x in range(0,5):
        #str=str()
        btn = Button(root, text = 'btn '+str(x)+'x'+str(y), command = root.destroy)
        btn.grid(row = y, column = x)


root.mainloop()