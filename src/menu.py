import tkinter as tk

import src.exercise1
import src.exercise2
import src.config
from src.rand import randrange_step

TITLE_FONT = ('Verdana', 14)


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.weight1 = self.controller.shared_data["weight1"]
        self.weight1_bind = tk.IntVar()
        self.weight1_bind.set(self.weight1)

        self.title_label = tk.Label(self, text='Générateur d\'exercices', font=TITLE_FONT)
        self.title_label.pack(padx=10, pady=10)

        start_button = tk.Button(self, text='Commencer', command=self.start)
        start_button.pack()

        config_button = tk.Button(self, text='Configurer les poids des exercices', command=self.config)
        config_button.pack()

    def config(self):
        self.controller.show_frame(src.config.Config)

    def start(self):

        print('WEIGHTS :'+str(self.controller.shared_data["weight1"]) + ' ' + str(self.controller.shared_data["weight2"]))

        random: int = randrange_step(0, 10, 1)
        print(random)
        # TODO: if weight for ex1 is fixed at 10, it can sometimes launch ex 2

        if random < self.controller.shared_data["weight1"]:
            self.controller.show_frame(src.exercise1.Exercise1)

        else:
            self.controller.show_frame(src.exercise2.Exercise2)
