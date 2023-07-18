#cours de tkinter avec David
#import tkinter

from tkinter import *

def main():

    win=Tk()

    label=Label(win, text="Hello world",pady=10)
    #label.configure(text="Hahaha je suis tout reconfigure")
    label.pack()

    btn=Button(win, text="Clic moi la", command=win.destroy)
    btn.pack()

    btn=Button(win, text="Change le text", command=win.destroy)
    btn.pack()

    win.mainloop()



if __name__ == "__main__":
    main()


