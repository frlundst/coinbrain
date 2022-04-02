from tkinter import *
import data
import json

class Interface:
    def __init__(self, title, dimensions):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(dimensions)

        self.label = Label(self.root, text = title, font = ("Arial Bold", 50))
        self.button = Button(self.root, text="Quit", command=self.root.quit)
        self.label.pack()
        self.button.pack()

        self.data = Label(self.root, text = "loading...")
        self.data.pack()

    def run(self):
        self.root.mainloop()

    def set_data(self):
        response = data.get_data("https://api.kraken.com/0/public/Time")
        time = response['result']['rfc1123']
        self.data['text'] = time
        self.root.after(5000, self.set_data)