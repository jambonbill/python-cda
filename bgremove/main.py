#Remove BG
from PIL import Image as PilImage
from rembg import remove

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo



def openImage():
    
    filetypes = (
        ('PNG files', '*.png'),
        ('JPG files', '*.jpg')
    )
    
    app.filename = fd.askopenfilename(title="Open image file", filetypes=filetypes)
    app.loadImage()
    



def removeBg():
    print("removeBg()")
    
    input = PilImage.open(app.filename) # load image
    output = remove(input) # remove background
    output.save("/tmp/tmp.png") # save image
    #app.setImage(output)
    app.filename = "/tmp/tmp.png"
    app.loadImage()
    print("done")

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Faux Tochope')
        self.geometry("800x600")
        
        menubar = Menu(self)
        
        #File menu
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.test)
        file.add_command(label="Open", command=openImage)
        file.add_command(label="Save", command=self.test)
        file.add_separator()
        file.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file)
        
        #Help Menu
        help = Menu(menubar, tearoff=0)
        help.add_command(label="Help Index", command=self.test)
        help.add_command(label="About...", command=self.test)
        menubar.add_cascade(label="Help", menu=help)

        self.config(menu=menubar)

        #btn1=Button(self, text="Save")
        #btn1.pack()

        btn2=Button(self, text="Remove BG", command=removeBg)
        btn2.pack()

        self.filename=''#image path
        self.image=PhotoImage(file="png/default.png")

        self.canva=Canvas(self)
        self.canva.create_image(0,0,anchor=NW,image=self.image)

        self.canva.pack()
        
    def loadImage(self):
        showinfo(
            title='Selected File',
            message=self.filename
        )
        self.image = PhotoImage(file=self.filename)
        self.reloadCanvas()

    def setImage(self,img):
        print('setImage')
        self.image = img
        self.reloadCanvas()

    def reloadCanvas(self):
        self.canva.create_image(0,0,anchor=NW,image=self.image)

    def test(self):
        print('je suis un test')
    




if __name__ == '__main__':
    app = App()
    app.mainloop()