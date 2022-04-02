from tkinter import *

class Interface:
    def __init__(self, title, dimensions):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(dimensions)
        self.label = Label(self.root, text = "Hello World")
        self.button = Button(self.root, text="Quit", command=self.root.quit)
        
    def run(self):
        self.label.pack()
        self.button.pack()
        self.root.mainloop()
