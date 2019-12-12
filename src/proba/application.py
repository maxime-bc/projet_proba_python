import tkinter as tk

from proba.config import Config
from proba.exercise1 import Exercise1
from proba.exercise2 import Exercise2
from proba.menu import Menu


class Application(tk.Tk):

    def __init__(self):

        super().__init__()
        self.geometry("600x400")
        self.title('Générateur d\'exercices')

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # TODO : change weights
        self.shared_data = {
            "weight_ex1": 50,
            "weight_ex2": 50,
            "ex2_weight1": 5,
            "ex2_weight2": 5,
            "ex2_weight3": 5,
            "score": 0.0,
            "max_score": 0.0,
            "best_score": 0.0
        }

        self.frames = {}

        for f in (Menu, Exercise1, Exercise2, Config):

            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()





