import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Adobe Photoshop")
label.pack()

label = tk.Label(text="Cloud edition turbo")
label.pack()


# Voici les alertes possibles:

#showinfo()
#showwarning()
#showerror()
#askquestion()
#askokcancel()
#askyesno()
#askretrycancel()


# entrée
#value = StringVar() 
#value.set("texte par défaut")
#entree = tk.Entry(window, textvariable=string, width=30)
#entree.pack()


# canvas
canvas = tk.Canvas(window, width=320, height=200, background='grey')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="canvas", font="Arial 16 italic", fill="black")
canvas.pack()


# bouton de sortie
bouton=tk.Button(window, text="Fermer Adobe Photoshop", command=window.quit)
bouton.pack()




window.mainloop()
