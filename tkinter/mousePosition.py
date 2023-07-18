#http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html#introduction
import tkinter as tk

root = tk.Tk()
root.title("Mouse Position")

root.geometry('800x600')


b=tk.Button()
im = tk.PhotoImage(file="png/logo.png")
b.config(image=im)
#b.pack()



button = tk.Button (text = "Clic");
button.grid(row = 12, column = 12)
#button.pack()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

#root.bind('<Motion>', motion)



# keep the window displaying
root.mainloop()

exit(0)