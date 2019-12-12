import tkinter as tk
from typing import Tuple

import proba.menu

TITLE_FONT = ('Verdana', 14)


class Config(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame_label = tk.Label(self, text="Configuration des poids des exercices :", font=TITLE_FONT)
        frame_label.pack()

        self.exercises_weight_label = tk.Label(self, text='Poids entre l\'exercice 1 et 2 : ')
        self.exercises_weight_label.pack()

        self.ex1_weight_label = tk.Label(self, text='Poids ex 1 : ')
        self.ex1_weight_label.pack()
        self.weight1_value = tk.IntVar()
        self.weight1_value.set(self.controller.shared_data["weight_ex1"])
        self.ex1_weight_entry = tk.Entry(self, text=self.weight1_value)
        self.ex1_weight_entry.pack()

        self.ex2_weight_label = tk.Label(self, text='Poids ex 2 : ')
        self.ex2_weight_label.pack()
        self.weight2_value = tk.IntVar()
        self.weight2_value.set(self.controller.shared_data["weight_ex1"])
        self.ex2_weight_entry = tk.Entry(self, text=self.weight2_value)
        self.ex2_weight_entry.pack()

        # 3 types of exercise 2

        self.ex2_weight1_value = tk.IntVar()
        self.ex2_weight1_value.set(self.controller.shared_data["ex2_weight1"])

        self.ex2_weight2_value = tk.IntVar()
        self.ex2_weight2_value.set(self.controller.shared_data["ex2_weight2"])

        self.ex2_weight3_value = tk.IntVar()
        self.ex2_weight3_value.set(self.controller.shared_data["ex2_weight3"])

        self.exercises_weight_label = tk.Label(self, text='Poids des types d\'intégrales de l\'ex 2 : ')
        self.exercises_weight_label.pack()

        self.ex2_weight1_label = tk.Label(self, text='Poids des fonctions puissance :')
        self.ex2_weight1_label.pack()
        self.ex2_weight1_entry = tk.Entry(self, text=self.ex2_weight1_value)
        self.ex2_weight1_entry.pack()

        self.ex2_weight2_label = tk.Label(self, text='Poids des fonctions trigonométriques :')
        self.ex2_weight2_label.pack()
        self.ex2_weight2_entry = tk.Entry(self, text=self.ex2_weight2_value)
        self.ex2_weight2_entry.pack()

        self.ex2_weight3_label = tk.Label(self, text='Poids des fonctions logarithmiques :')
        self.ex2_weight3_label.pack()
        self.ex2_weight3_entry = tk.Entry(self, text=self.ex2_weight3_value)
        self.ex2_weight3_entry.pack()

        self.validate_button = tk.Button(self, text='Valider', command=self.validate)
        self.validate_button.pack()

    def validate(self):

        try:

            if not (int(self.ex1_weight_entry.get()) == 0) or not (int(self.ex2_weight_entry.get()) == 0):

                self.controller.shared_data["weight_ex1"], self.controller.shared_data["weight_ex2"] = \
                    self.generate_ratio_two_weights(int(self.ex1_weight_entry.get()), int(self.ex2_weight_entry.get()))

                self.controller.shared_data["ex2_weight1"] = int(self.ex2_weight1_entry.get())
                self.controller.shared_data["ex2_weight2"] = int(self.ex2_weight2_entry.get())
                self.controller.shared_data["ex2_weight3"] = int(self.ex2_weight3_entry.get())

                self.controller.show_frame(proba.menu.Menu)

        except ValueError:
            pass

    def generate_ratio_two_weights(self, w1: int, w2: int) -> Tuple[int, int]:

        w1, w2 = self.permute_bounds(w1, w2)
        weight_sum: int = w1 + w2

        percentage1: int = round((w1 / weight_sum) * 100)
        percentage2: int = round((w2 / weight_sum) * 100)

        return percentage1, percentage2

    def permute_bounds(self, a: int, b: int) -> Tuple[int, int]:
        tmp: int = a
        a = b
        b = tmp
        return a, b
