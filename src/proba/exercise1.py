import tkinter as tk

from proba.format import format_quadratic_equation
import proba.menu
from proba.quadratic_equations import solve_quadratic_equation
from proba.rand import randrange_step, randrange_exclude, START_VALUE, STOP_VALUE, STEP_VALUE
from proba.utils import round_float

LARGE_FONT = ('Verdana', 12)
HARD_EXERCISE_POINTS: float = 1.5
NORMAL_EXERCISE_POINTS: float = 1.0


class Exercise1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        self.score = self.controller.shared_data["score"]
        self.max_score = self.controller.shared_data["max_score"]

        self.res1 = None
        self.res2 = None
        self.sol_no = None
        self.entry_array = [None] * 2
        self.label_array = [None] * 2

        self.title_label = tk.Label(self, text="Exercice sur les équations du second degré", font=LARGE_FONT)

        self.equation_str = tk.StringVar()
        self.equation_label = tk.Label(self, textvariable=self.equation_str, font=LARGE_FONT)
        self.equation_label.pack(padx=10, pady=10)

        self.sol_label = tk.Label(self, text="Nombre de solutions :", font=LARGE_FONT)

        self.initial_spinbox_value = tk.IntVar(value=0)
        self.previous_spinbox_value = 0
        self.sol_no_spinbox = tk.Spinbox(self, from_=0, to=2, textvariable=self.initial_spinbox_value,
                                         command=self.on_spinbox_changed, state='readonly')

        for index in range(0, 2):
            self.label_array[index] = tk.Label(self, text='Solution '+str(index+1))
            self.entry_array[index] = tk.Entry(self)

        self.validate_button = tk.Button(self, text='Valider', command=self.check_answers)
        self.next_button = tk.Button(self, text='Continuer ?', command=self.next)
        self.back_button = tk.Button(self, text='Retour', command=lambda: controller.show_frame(proba.menu.Menu))

        self.answer_text = tk.StringVar()
        self.answer_label = tk.Label(self, textvariable=self.answer_text)

    def hide_entries(self):
        self.sol_label.pack_forget()
        self.sol_no_spinbox.pack_forget()
        self.back_button.pack_forget()
        self.validate_button.pack_forget()
        for index in range(0, int(self.sol_no_spinbox.get())):
            self.entry_array[index].pack_forget()
            self.label_array[index].pack_forget()

    def show_answers(self):
        self.answer_label.pack()
        self.next_button.pack()
        self.back_button.pack()

    @staticmethod
    def set_text(entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)

    def next(self):

        random: int = randrange_step(0, 10, 1)
        print(random)
        # TODO: if weight for ex1 is fixed at 10, it can sometimes launch ex 2

        if random < self.controller.shared_data["weight1"]:
            self.controller.show_frame(proba.exercise1.Exercise1)

        else:
            self.controller.show_frame(proba.exercise2.Exercise2)

    def on_show_frame(self, event):
        # Generate a new exercise

        a: float = randrange_exclude(0.0, START_VALUE, STOP_VALUE, STEP_VALUE)
        b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
        c: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

        self.res1, self.res2, self.sol_no = solve_quadratic_equation(a, b, c)

        self.equation_str.set('Equation du 2nd degré générée : {}\nRésoudre f(x) = 0'
                              .format(format_quadratic_equation(a, b, c)))

        # Build window
        self.title_label.pack()
        self.equation_label.pack()
        self.sol_label.pack()

        self.answer_text.set('')
        self.answer_label.pack_forget()

        self.entry_array[0].pack_forget()
        self.label_array[0].pack_forget()
        self.set_text(self.entry_array[0], '')

        self.entry_array[1].pack_forget()
        self.label_array[1].pack_forget()
        self.set_text(self.entry_array[1], '')

        self.initial_spinbox_value.set('0')
        self.previous_spinbox_value = 0
        self.sol_no_spinbox.pack()

        self.validate_button.pack_forget()
        self.validate_button.pack()
        self.next_button.pack_forget()
        self.back_button.pack_forget()
        self.back_button.pack()

        # DEBUG ONLY
        print('NB SOL : '+str(self.sol_no))
        if self.sol_no == 1:
            print('SOL : {}'.format(self.res1))
        elif self.sol_no == 2:
            print('SOLS : {} {}'.format(self.res1, self.res2))

    def check_answers(self):
        print('Validating')

        given_sol_no: float = int(self.sol_no_spinbox.get())

        if self.sol_no == given_sol_no:
            if self.sol_no == 0:

                self.answer_text.set('Bravo ! \nEn effet, cette équation n\'a pas de solutions.\n')
                self.score = self.score + 1.0
                self.max_score = self.max_score + 1.0
                self.hide_entries()
                self.show_answers()

            elif self.sol_no == 1:
                rounded_res1 = round_float(self.res1)

                try:
                    answer1 = float(self.entry_array[0].get())

                    if answer1 == rounded_res1:
                        self.answer_text.set('Bravo ! \nEn effet, cette équation possède une solution : '
                                             '{:0.2f}\n'.format(rounded_res1))
                        self.score = self.score + 1.0
                        self.max_score = self.max_score + 1.0

                    else:
                        self.answer_text.set('Faux ! \nCette équation possède une solution : '
                                             '{:0.2f}\n'.format(rounded_res1))
                        self.max_score = self.max_score + 1.0

                    self.hide_entries()
                    self.show_answers()

                except ValueError:
                    self.answer_text.set('Faux ! \nCette équation possède une solution : '
                                         '{:0.2f}\n'.format(rounded_res1))
                    self.max_score = self.max_score + 1.0

                    self.hide_entries()
                    self.show_answers()

            elif self.sol_no == 2:
                rounded_res1 = round_float(self.res1)
                rounded_res2 = round_float(self.res2)

                if self.sol_no >= given_sol_no:
                    try:
                        answer1 = float(self.entry_array[0].get())
                        answer2 = float(self.entry_array[1].get())

                        if answer1 == rounded_res1 and answer2 == rounded_res2:
                            self.answer_text.set('Bravo ! \nEn effet, cette équation possède deux solutions : '
                                                 '{:0.2f} et {:0.2f}\n'.format(rounded_res1, rounded_res2))
                            self.score = self.score + 1.0
                            self.max_score = self.max_score + 1.0

                        else:

                            if answer1 == rounded_res1 and answer2 == rounded_res1:
                                self.answer_text.set('Bravo ! \nEn effet, cette équation possède deux solutions : '
                                                     '{:0.2f} et {:0.2f}\n'.format(rounded_res1, rounded_res2))
                                self.score = self.score + 1.0
                                self.max_score = self.max_score + 1.0

                            else:
                                self.answer_text.set('Faux ! \nCette équation possède deux solutions : '
                                                     '{:0.2f} et {:0.2f}\n'.format(rounded_res1, rounded_res2))
                                self.max_score = self.max_score + 1.0

                        self.hide_entries()
                        self.show_answers()

                    except ValueError:
                        self.answer_text.set('Faux ! \nCette équation possède une solution : '
                                             '{:0.2f}\n'.format(rounded_res1))
                        self.max_score = self.max_score + 1.0

                        self.hide_entries()
                        self.show_answers()

                else:
                    self.answer_text.set('Faux ! \nCette équation possède deux solutions : '
                                         '{:0.2f} et {:0.2f}\n'.format(rounded_res1, rounded_res2))
                    self.max_score = self.max_score + 1.0
                    self.hide_entries()
                    self.show_answers()
        else:
            self.answer_text.set('Faux ! \nVous avez choisi {} solution(s), or cette équation possède {} solutions.\n'
                                 .format(given_sol_no, self.sol_no))
            self.max_score = self.max_score + 1.0

            self.hide_entries()
            self.show_answers()

    def on_spinbox_changed(self):

        self.answer_label.pack_forget()
        self.validate_button.pack_forget()
        self.back_button.pack_forget()

        actual_spinbox_value = int(self.sol_no_spinbox.get())

        if actual_spinbox_value > self.previous_spinbox_value:
            self.label_array[actual_spinbox_value - 1].pack()
            self.entry_array[actual_spinbox_value - 1].pack()
            self.previous_spinbox_value = actual_spinbox_value

        elif actual_spinbox_value < self.previous_spinbox_value:
            self.label_array[actual_spinbox_value].pack_forget()
            self.entry_array[actual_spinbox_value].pack_forget()
            self.previous_spinbox_value = actual_spinbox_value

        self.answer_label.pack()
        self.validate_button.pack()
        self.back_button.pack()
