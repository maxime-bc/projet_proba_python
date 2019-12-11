import tkinter as tk
import proba.menu

TITLE_FONT = ('Verdana', 14)


class Config(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.weight1 = self.controller.shared_data["weight1"]
        self.weight2 = self.controller.shared_data["weight2"]

        self.ex2_weight1 = self.controller.shared_data["ex2_weight1"]
        self.ex2_weight2 = self.controller.shared_data["ex2_weight2"]
        self.ex2_weight3 = self.controller.shared_data["ex2_weight3"]

        frame_label = tk.Label(self, text="Configuration des poids des exercices :", font=TITLE_FONT)
        frame_label.pack()

        # Exercises 1 and 2

        self.weight1_value = tk.IntVar()
        self.weight1_value.set(self.weight1)

        self.weight1_label = tk.Label(self, text='Poids des exercices sur les équations second degré : ')
        self.weight1_label.pack()
        self.weight1_entry = tk.Entry(self, text=self.weight1_value)
        self.weight1_entry.pack()

        self.weight2_text = tk.StringVar()
        self.weight2_text.set('Poids des exercices sur les intégrales : {}'.format(self.weight2))
        self.weight2_label = tk.Label(self, textvariable=self.weight2_text)
        self.weight2_label.pack()

        # 3 types of exercise 2

        self.ex2_weight1_value = tk.IntVar()
        self.ex2_weight1_value.set(self.ex2_weight1)

        self.ex2_weight2_value = tk.IntVar()
        self.ex2_weight2_value.set(self.ex2_weight2)

        self.ex2_weight1_label = \
            tk.Label(self, text='Poids 1 : intégrales de fonctions puissance (compris entre 1 et 15) :')
        self.ex2_weight1_label.pack()
        self.ex2_weight1_entry = tk.Entry(self, text=self.ex2_weight1_value)
        self.ex2_weight1_entry.pack()

        self.ex2_weight2_label = \
            tk.Label(self, text='Poids 2 : intégrales de fonctions trigonométriques (compris entre \'poids1\' et 15) :')
        self.ex2_weight2_label.pack()
        self.ex2_weight2_entry = tk.Entry(self, text=self.ex2_weight2_value)
        self.ex2_weight2_entry.pack()

        self.ex2_weight3_text = tk.StringVar()
        self.ex2_weight3_text.set('Poids 3 : intégrales de fonctions logarithmiques : {}'.format(self.ex2_weight3))
        self.weight2_label = tk.Label(self, textvariable=self.ex2_weight3_text)
        self.weight2_label.pack()

        self.validate_button = tk.Button(self, text='Valider', command=self.validate)
        self.validate_button.pack()

    def validate(self):

        try:
            weight1 = int(self.weight1_entry.get())
            ex2_weight1 = int(self.ex2_weight1_entry.get())
            ex2_weight2 = int(self.ex2_weight2_entry.get())

            # Exercises weights checks

            if 0 <= weight1 <= 10:

                weight2: int = 10 - weight1
                self.weight2_text.set('Poids des exercices sur les intégrales : {}'.format(weight2))
                self.weight2_label.pack()

                self.controller.shared_data["weight1"] = weight1
                self.controller.shared_data["weight2"] = weight2

                # Exercise 2 checks

                if 0 <= ex2_weight1 <= 15:

                    if 0 <= ex2_weight2 <= (15 - ex2_weight1):

                        ex2_weight3: int = 15 - (ex2_weight1 + ex2_weight2)
                        self.ex2_weight3_text.set('Poids 3 : intégrales de fonctions logarithmiques : {}'
                                                  .format(ex2_weight3))

                        self.controller.shared_data["ex2_weight1"] = ex2_weight1
                        self.controller.shared_data["ex2_weight2"] = ex2_weight2
                        self.controller.shared_data["ex2_weight3"] = ex2_weight3

                        self.controller.show_frame(proba.menu.Menu)

                    else:
                        print('Non3')

                else:
                    print('Non2')

            else:
                print('NON1')

        except ValueError:
            pass
