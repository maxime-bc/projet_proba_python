import tkinter as tk

import proba.exercise1
import proba.exercise2
import proba.config
from proba.rand import randrange_step

TITLE_FONT = ('Verdana', 14)

'''This module displays the menu.'''


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        self.title_label = tk.Label(self, text='Générateur d\'exercices', font=TITLE_FONT)
        self.title_label.pack(padx=10, pady=10)

        self.score_text = tk.StringVar()
        self.score_label = tk.Label(self, textvar=self.score_text)

        self.start_button = tk.Button(self, text='Commencer', command=self.start)
        self.start_button.pack()

        self.config_button = tk.Button(self, text='Configurer les poids des exercices', command=self.config)
        self.config_button.pack()

    def on_show_frame(self, event):
        # update the score

        print('Showed')

        self.start_button.pack_forget()
        self.config_button.pack_forget()

        self.score_text.set('Meilleur score : {}'.format(self.controller.shared_data["best_score"]))

        self.score_label.pack()
        self.start_button.pack()
        self.config_button.pack()

    def config(self):
        self.controller.show_frame(proba.config.Config)

    def start(self):

        print('SCORE :' + str(self.controller.shared_data["score"]) + ', MAX SCORE : '
              + str(self.controller.shared_data["max_score"]))

        print('WEIGHTS :'+str(self.controller.shared_data["weight_ex1"]) + ' '
              + str(self.controller.shared_data["weight_ex2"]))

        print('WEIGHTS EX 2 :'+str(self.controller.shared_data["ex2_weight1"]) + ' '
              + str(self.controller.shared_data["ex2_weight2"]) + ' ' + str(self.controller.shared_data["ex2_weight3"]))

        random: int = randrange_step(0, 100, 1)
        print(random)

        if random <= self.controller.shared_data["weight_ex1"]:
            self.controller.show_frame(proba.exercise1.Exercise1)

        else:
            self.controller.show_frame(proba.exercise2.Exercise2)
