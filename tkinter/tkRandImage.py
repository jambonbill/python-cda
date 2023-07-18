#http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html#introduction
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Randimage")


def do_alert () :
    print("do_alert")
    messagebox.showinfo("messagebox.showinfo", "Youpi tralala")#, **options


def do_something () :
    #global b
    #b.config (text = "nouvelle légende")
    print("do something")



b=tk.Button()
im = tk.PhotoImage(file="png/logo.png")
b.config(image=im, command=do_alert)
b.pack()


button = tk.Button (text = "Generer")
button.config (command = do_something)
button.pack()


# keep the window displaying
root.mainloop()

exit(0)