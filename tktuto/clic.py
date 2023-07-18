# Détection et positionnement d'un clic de souris dans une fenêtre :
 
from tkinter import *
 
def pointeur(event):
 chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
	     ", Y =" + str(event.y))
 
win = Tk()

cadre = Frame(win, width =800, height =600, bg="white")
cadre.bind("<Button-1>", pointeur)
cadre.pack()

chaine = Label(win)
chaine.pack()
 
win.mainloop()