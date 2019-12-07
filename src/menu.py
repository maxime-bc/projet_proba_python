import tkinter as tk

import src.exercise1
import src.exercise2
from src.rand import randrange_step

LARGE_FONT = ('Verdana', 12)


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.score = self.controller.shared_data["score"]
        self.max_score = self.controller.shared_data["max_score"]
        self.weight1 = self.controller.shared_data["weight1"]
        self.weight2 = self.controller.shared_data["weight2"]

        self.weight1_bind = tk.IntVar()
        self.weight1_bind.set(self.weight1)

        self.frame_label = tk.Label(self, text='MENU', font=LARGE_FONT)
        self.frame_label.pack(padx=10, pady=10)

        self.weight1_label = tk.Label(self, text='Poids exercice Equations second degré : ')
        self.weight1_label.pack()
        self.weight_entry = tk.Entry(self, text=self.weight1_bind)
        self.weight_entry.pack()

        self.weight2_label = tk.Label(self, text='Poids exercice Intégrales : {}'.format(self.weight2))
        self.weight2_label.pack()

        start_button = tk.Button(self, text='Commencer', command=self.start)
        start_button.pack()

    def start(self):

        try:

            self.weight1 = int(self.weight_entry.get())
            print('{} {}'.format(type(self.weight1), self.weight1))

            if self.weight1 < 0 or self.weight1 > 10:
                print('Le poids doit être compris entre 0 et 10 : \n')

            else:

                self.weight2 = 10 - self.weight1
                self.weight2_label['text'] = 'Poids exercice 2 : {}'.format(self.weight2)
                self.weight2_label.pack()

                random: int = randrange_step(0, 10, 1)
                print(random)
                # TODO: if weight for ex1 is fixed at 10, it can sometimes launch ex 2

                if random < self.weight1:
                    self.controller.show_frame(src.exercise1.Exercise1)

                else:
                    self.controller.show_frame(src.exercise2.Exercise2)

        except ValueError:
            pass
