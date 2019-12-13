import tkinter as tk
from math import isnan

import proba.menu
from proba.format import format_pow, format_inverse, format_cos, format_sin, format_tan, format_log
from proba.generate import generate_pow1, generate_pow2, generate_trigo, generate_log
from proba.integrals import integral_pow1, integral_pow2, integral_trigo1, integral_trigo2, integral_trigo3, integral_log
from proba.rand import randrange_step, round_float
import proba.exercise1

LARGE_FONT = ('Verdana', 12)
HARD_EXERCISE_POINTS: float = 1.5
NORMAL_EXERCISE_POINTS: float = 1.0


class Exercise2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bind("<<ShowFrame>>", self.on_show_frame)

        self.score = self.controller.shared_data["score"]
        self.max_score = self.controller.shared_data["max_score"]

        self.result = None
        self.exercise_points = None

        self.title_text = tk.StringVar()
        self.title_label = tk.Label(self, textvar=self.title_text, font=LARGE_FONT)

        self.integral_bounds_text = tk.StringVar()
        self.integral_bounds_label = tk.Label(self, textvar=self.integral_bounds_text)

        self.integral_function_text = tk.StringVar()
        self.integral_function_label = tk.Label(self, textvar=self.integral_function_text)

        self.message_text = tk.StringVar()
        self.message_label = tk.Label(self, textvar=self.message_text)

        self.score_text = tk.StringVar()
        self.score_label = tk.Label(self, textvar=self.score_text)

        self.answer_label = tk.Label(self, text='Résultat :')

        self.answer_text = tk.StringVar()
        self.answer_entry = tk.Entry(self, textvar=self.answer_text)

        self.validate_answer = tk.Button(self, text='Valider',  command=self.validate)
        self.next_button = tk.Button(self, text='Continuer ?', command=self.next)

        self.back_button = tk.Button(self, text='Retour', command=self.back)

    def back(self):
        self.controller.shared_data["score"] = 0.0
        self.controller.shared_data["max_score"] = 0.0
        self.controller.show_frame(proba.menu.Menu)

    def next(self):

        random: int = randrange_step(0, 100, 1)
        print(random)
        # TODO: if weight for ex1 is fixed at 10, it can sometimes launch ex 2

        if random < self.controller.shared_data["weight1"]:
            self.controller.show_frame(proba.exercise1.Exercise1)

        else:
            self.controller.show_frame(proba.exercise2.Exercise2)

    def validate(self):

        self.result = round_float(self.result)

        try:
            given_result: float = float(self.answer_entry.get())

            if self.result == given_result:
                self.validate_answer.pack_forget()
                self.back_button.pack_forget()

                self.controller.shared_data["score"] += self.exercise_points
                self.controller.shared_data["max_score"] += self.exercise_points

                self.message_text.set('Bravo ! En effet, cette intégrale vaut {:0.2f}.'.format(self.result))

                self.message_label.pack()

                if self.controller.shared_data["score"] > self.controller.shared_data["best_score"]:
                    self.score_text.set('+{} points, score : {}/{} [Record battu !]'
                                        .format(
                                                self.exercise_points,
                                                self.controller.shared_data["score"],
                                                self.controller.shared_data["max_score"]))
                    self.controller.shared_data["best_score"] = self.controller.shared_data["score"]

                else:
                    self.score_text.set('+{} points, score : {}/{}'
                                        .format(
                                                self.exercise_points,
                                                self.controller.shared_data["score"],
                                                self.controller.shared_data["max_score"]))

                self.score_label.pack()
                self.next_button.pack()
                self.back_button.pack()

            else:
                self.validate_answer.pack_forget()
                self.back_button.pack_forget()

                self.controller.shared_data["max_score"] += self.exercise_points

                self.message_text.set('Faux ! Cette intégrale vaut {:0.2f}.'.format(self.result))
                self.message_label.pack()

                self.score_text.set('Série de points annulée, score : {}/{}'
                                    .format(self.controller.shared_data["score"],
                                            self.controller.shared_data["max_score"]))
                self.controller.shared_data["score"] = 0.0
                self.controller.shared_data["max_score"] = 0.0

                self.score_label.pack()
                self.next_button.pack()
                self.back_button.pack()

        except ValueError:
            pass

    def on_show_frame(self, event):
        # Generate a new exercise

        self.message_label.pack_forget()
        self.score_label.pack_forget()
        self.validate_answer.pack_forget()
        self.next_button.pack_forget()
        self.back_button.pack_forget()
        self.answer_text.set('')

        weight1 = self.controller.shared_data["ex2_weight1"]
        weight2 = self.controller.shared_data["ex2_weight2"]
        weight3 = self.controller.shared_data["ex2_weight3"]

        # TODO: the same exercise can be repeated
        random: float = randrange_step(0, 100, 1)

        if random <= weight1:

            print('Fonction puissance\n')
            random: float = randrange_step(1.0, 2.0, 1.0)
            self.exercise_points = HARD_EXERCISE_POINTS
            self.title_text.set('Exercice sur les intégrales (+ {} points)'.format(self.exercise_points))

            if random == 1:
                pass
                # self.result = self.pow1()

            else:
                self.result = self.pow2()

            print('{:0.2f}\n'.format(self.result))

        elif weight1 < random <= (weight1 + weight2):

            print('Fonction trigonométrique\n')

            random: int = randrange_step(0, 2, 1.0)
            self.exercise_points = NORMAL_EXERCISE_POINTS
            self.title_text.set('Exercice sur les intégrales (+ {} points)'.format(self.exercise_points))

            if random == 0:
                self.result = self.trigo1()

            elif random == 1:
                self.result = self.trigo2()

            else:
                self.result = self.trigo3()

            print('{:0.2f}\n'.format(self.result))

        elif random > weight3:
            print('Fonction logarithmique\n')
            self.exercise_points = NORMAL_EXERCISE_POINTS
            self.title_text.set('Exercice sur les intégrales (+ {} point(s))'.format(self.exercise_points))
            self.result = self.log1()

            print('{:0.2f}\n'.format(self.result))

        self.title_label.pack(padx=10, pady=10)
        self.integral_bounds_label.pack()
        self.integral_function_label.pack()
        self.answer_entry.pack()

        self.validate_answer.pack()
        self.back_button.pack()

    def pow1(self) -> float:
        a, b, c, d, alpha = generate_pow1()
        res = integral_pow1(a, b, c, d, alpha)
        while isnan(res):
            res = integral_pow1(a, b, c, d, alpha)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_function_text.set(format_pow(c, d, alpha))

        return res

    def pow2(self) -> float:
        a, b, c = generate_pow2()
        res = integral_pow2(a, b, c)
        while isnan(res):
            res = integral_pow2(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_function_text.set(format_inverse(c))

        return res

    def trigo1(self) -> float:
        a, b, c = generate_trigo()
        res = integral_trigo1(a, b, c)
        while isnan(res):
            res = integral_trigo1(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_function_text.set(format_cos(c))

        return res

    def trigo2(self) -> float:
        a, b, c = generate_trigo()
        res = integral_trigo2(a, b, c)
        while isnan(res):
            res = integral_trigo2(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_function_text.set(format_sin(c))

        return res

    def trigo3(self) -> float:
        a, b, c = generate_trigo()
        res = integral_trigo3(a, b, c)
        while isnan(res):
            res = integral_trigo3(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_function_text.set(format_tan(c))

        return res

    def log1(self) -> float:
        a, b, c = generate_log()
        res = integral_log(a, b, c)
        while isnan(res):
            res = integral_log(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_function_text.set(format_log(c))
        return res

    @staticmethod
    def header(a: float, b: float) -> str:
        return 'Calculez l\'intégrale f(x)dx allant de {:0.1f} à {:0.1f} avec :\n'.format(a, b)
