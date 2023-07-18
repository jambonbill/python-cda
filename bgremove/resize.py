#Remove BG
from PIL import Image as PilImage

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Faux Tochope CM2')
        self.geometry("800x600")
        
        menubar = Menu(self)
        
        #File menu
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.new, accelerator= "Ctrl+N")
        file.add_command(label="Open", command=self.open, accelerator= "Ctrl+O")
        file.add_command(label="Save", command=self.test, accelerator= "Ctrl+S")
        file.add_separator()
        file.add_command(label="Exit", command=self.quit, accelerator= "Ctrl+Q")
        menubar.add_cascade(label="File", menu=file)

        file.bind_all("<Control-n>", self.new)
        file.bind_all("<Control-o>", self.open)


        #Edit menu
        edit = Menu(menubar, tearoff=0)
        edit.add_command(label="Resize", command=self.resize)
        menubar.add_cascade(label="Edit", menu=edit)

        #Help Menu
        help = Menu(menubar, tearoff=0)
        help.add_command(label="Help Index", command=self.test)
        help.add_command(label="About...", command=self.test)
        menubar.add_cascade(label="Help", menu=help)

        self.config(menu=menubar)
        

        self.filename=''#image path
        self.image=PhotoImage(file="png/default.png")
        #self.image=PilImage.open("png/default.png")

        self.canva=Canvas(self,width=800, height=600, bg='#ccc')
        self.canva.create_image(0,0,anchor=NW,image=self.image)
        #self.canva.create_bitmap(0,0,anchor=NW,image=self.image)#bitmap is a `1bit image`
        self.canva.pack(expand=True)

        input=Entry(self,text="coucou")
        input.pack()
    
    
    def resize(self):
        w = self.image.width()
        h = self.image.height()
        
        print(type(self.image))
        print(str(w)+"x"+str(h)+"[px]")
        #dimensions = "image size: %dx%d" % (image.width(), image.height())
        
        #punk resize 
        self.image = self.image.zoom(2,2)#zoom x2
        
        #self.image = self.image.subsample(32)#?
        self.reloadCanvas()
    


    def loadImage(self):
        #showinfo(title='Selected File', message=self.filename)
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
    

    def new(self, event=None):#init
        print("new()")
        pass

    def open(self, event=None):
        filetypes = (
            ('PNG files', '*.png'),
            ('JPG files', '*.jpg')
        )    
        self.filename = fd.askopenfilename(title="Open image file", filetypes=filetypes)
        self.loadImage()

    




if __name__ == '__main__':
    app = App()
    app.mainloop()