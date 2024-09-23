from tkinter import *

class EntryWithLabel:
    def __init__(self,window, text, x,y, distance=80, data_type = "str"):
        Label(window, text=text).place(x=x, y=y)

        match data_type:
            case "str":
                self.variable = StringVar()
            case "int":
                self.variable = IntVar()
            case "float":
                self.variable = DoubleVar()
            case "bool":
                self.variable = BooleanVar()

        Entry(window, textvariable=self.variable).place(x=x + distance, y=y)

    def get(self):
        return self.variable.get()

    def set(self):
        self.variable.set(self.get())