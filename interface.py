from tkinter import *
from datetime import datetime
import data

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

        self.time = Label(self.root, text = "loading...")
        self.time.pack()

    def run(self):
        self.root.mainloop()

    def set_data(self, ):
        try:
            response = data.get_data("https://api.kraken.com/0/public/Ticker?pair=XBTUSD")
            xbtusd = response['result']['XXBTZUSD']['a'][0]
            self.data['text'] = xbtusd
        except:
            self.data['text'] = "Error"
        self.root.after(60000, self.set_data)

    def set_time(self, ):
        self.time['text'] = datetime.now().strftime("%H:%M:%S")
        self.root.after(1000, self.set_time)