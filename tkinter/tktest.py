#http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html#introduction
import tkinter as tk

root = tk.Tk()
root.title("PyDPainter Error")

b=tk.Button()
im = tk.PhotoImage(file="logo.png")
b.config(image=im)
b.pack()


#Put out a useful message if pygame is not installed
message = tk.Label(root, text="""
Bonjour et bienvenue chez Python Telethon.
On va bien s'amuser, ca sent la grosse bamboula.
Envoyez la thune
""")

message.pack()

label = tk.Label (text = "premier texte")
#changer le texte
#label.config (text = "second texte")
label.pack()


button = tk.Button (text = "Continuer")
button.pack()

# keep the window displaying
root.mainloop()

exit(0)