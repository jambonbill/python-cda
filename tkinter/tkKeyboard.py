#http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html#introduction

import tkinter as tk

root = tk.Tk()
root.title("Keyboard")


def affiche_touche_pressee (evt) :
    print("--------------------------- touche pressee")
    print("evt.char = ", evt.char)
    print("evt.keysym = ", evt.keysym)
    print("evt.num = ", evt.num)
    print("evt.x,evt.y = ", evt.x, ",", evt.y)
    print("evt.x_root,evt.y_root = ", evt.x_root, ",", evt.y_root)
    print("evt.widget = ", evt.widget)




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


#button.bind ("<Key>", affiche_touche_pressee)
#button.bind ("<Button-1>", affiche_touche_pressee)
#button.bind ("<Motion>", affiche_touche_pressee)
#button.focus_set ()

root.bind("<Key>", affiche_touche_pressee)

# keep the window displaying
root.mainloop()

exit(0)