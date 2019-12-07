import tkinter as tk

from src.exercise1 import Exercise1
from src.exercise2 import Exercise2
from src.menu import Menu


class Application(tk.Tk):

    def __init__(self):

        super().__init__()
        self.geometry("720x480")
        self.title('Projet Probabilités')

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.shared_data = {
            "weight1": 5,
            "weight2": 5,
            "score": 0.0,
            "max_score": 0.0
        }

        self.frames = {}

        for f in (Menu, Exercise1, Exercise2):

            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()





