import tkinter as tk
from math import isnan

import src.menu
from src.format import format_pow, format_inverse, format_cos, format_sin, format_tan, format_log
from src.generate import generate_pow1, generate_pow2, generate_trigo, generate_log
from src.integrals import integral_pow1, integral_pow2, integral_trigo1, integral_trigo2, integral_trigo3, integral_log
from src.rand import randrange_exclude, randrange_step, START_VALUE, STOP_VALUE, STEP_VALUE
from src.utils import round_float

LARGE_FONT = ('Verdana', 12)


class Exercise2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bind("<<ShowFrame>>", self.generate_exercise)

        self.score = self.controller.shared_data["score"]
        self.max_score = self.controller.shared_data["max_score"]

        self.result: float

        self.weight1 = self.controller.shared_data["ex2_weight1"]
        self.weight2 = self.controller.shared_data["ex2_weight2"]
        self.weight3 = self.controller.shared_data["ex2_weight3"]

        label = tk.Label(self, text="Exercice sur les intégrales", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        self.integral_bounds_text = tk.StringVar()
        self.integral_bounds_label = tk.Label(self, textvar=self.integral_bounds_text)
        self.integral_bounds_label.pack()

        self.integral_function_text = tk.StringVar()
        self.integral_function_label = tk.Label(self, textvar=self.integral_function_text)
        self.integral_function_label.pack()

        self.answer_label = tk.Label(self, text='Résultat :')
        self.answer_label.pack()

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack()

        self.validate_answer = tk.Button(self, text='Valider',  command=self.validate)
        self.validate_answer.pack()

        back_button = tk.Button(self, text='Retour', command=lambda: controller.show_frame(src.menu.Menu))
        back_button.pack()

    def validate(self):

        self.result = round_float(self.result)

        try:
            given_result: float = float(self.answer_entry.get())

            if self.result == given_result:
                print('Bravo ! \n En effet, cette intégrale vaut {:0.2f}\n'.format(self.result))
                # TODO : add score

            else:
                print('Faux ! \n Cette intégrale vaut {:0.2f}\n'.format(self.result))

        except ValueError:
            pass

    def generate_exercise(self, event):

        random: float = randrange_step(0.0, 15.0, 1.0)
        res: float

        if random <= self.weight1:

            print('Fonction puissance\n')
            random: float = randrange_step(1.0, 2.0, 1.0)

            if random == 1:
                pass
                # self.result = self.pow1()

            else:
                self.result = self.pow2()

            print('{:0.2f}\n'.format(self.result))
            # score, max_score = check_exercise2_answers(round_float(res), score, max_score, HARD_EXERCISE)

        elif self.weight1 < random <= (self.weight1 + self.weight2):

            print('Fonction trigonométrique\n')

            random: int = randrange_step(1.0, 3.0, 1.0)

            if random == 1:
                self.result = self.trigo1()

            elif random == 2:
                self.result = self.trigo2()

            else:
                self.result = self.trigo3()

            print('{:0.2f}\n'.format(self.result))
            # score, max_score = check_exercise2_answers(round_float(res), score, max_score, NORMAL_EXERCISE)

        else:
            print('Fonction logarithmique\n')
            self.result = self.log1()

            print('{:0.2f}\n'.format(self.result))
            # score, max_score = check_exercise2_answers(round_float(res), score, max_score, NORMAL_EXERCISE)


    def check_exercise2_answers(self, rounded_res: float, score: float, max_score: float, difficulty: int) -> None:


        if rounded_res == answer:
            print('Bravo ! \n En effet, cette intégrale vaut {:0.2f}\n'.format(rounded_res))

            if difficulty == NORMAL_EXERCISE:
                score = score + 1.0
                max_score = max_score + 1.0

            elif difficulty == HARD_EXERCISE:
                score = score + 1.5
                max_score = max_score + 1.5

        else:
            print('Faux ! \n Cette intégrale vaut {:0.2f}\n'.format(rounded_res))

            if difficulty == NORMAL_EXERCISE:
                max_score = max_score + 1.0
            elif difficulty == HARD_EXERCISE:
                max_score = max_score + 1.5

        return score, max_score

    def pow1(self) -> float:
        a, b, c, d, alpha = generate_pow1()
        res = integral_pow1(a, b, c, d, alpha)
        while isnan(res):
            res = integral_pow1(a, b, c, d, alpha)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_bounds_label.pack()

        self.integral_function_text.set(format_pow(c, d, alpha))
        self.integral_function_label.pack()

        return res

    def pow2(self) -> float:
        a, b, c = generate_pow2()
        res = integral_pow2(a, b, c)
        while isnan(res):
            res = integral_pow2(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_bounds_label.pack()

        self.integral_function_text.set(format_inverse(c))
        self.integral_function_label.pack()

        return res

    def trigo1(self) -> float:
        a, b, c = generate_trigo()
        res = integral_trigo1(a, b, c)
        while isnan(res):
            res = integral_trigo1(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_bounds_label.pack()

        self.integral_function_text.set(format_cos(c))
        self.integral_function_label.pack()

        return res

    def trigo2(self) -> float:
        a, b, c = generate_trigo()
        res = integral_trigo2(a, b, c)
        while isnan(res):
            res = integral_trigo2(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_bounds_label.pack()

        self.integral_function_text.set(format_sin(c))
        self.integral_function_label.pack()

        return res

    def trigo3(self) -> float:
        a, b, c = generate_trigo()
        res = integral_trigo3(a, b, c)
        while isnan(res):
            res = integral_trigo3(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_bounds_label.pack()

        self.integral_function_text.set(format_tan(c))
        self.integral_function_label.pack()

        return res

    def log1(self) -> float:
        a, b, c = generate_log()
        res = integral_log(a, b, c)
        while isnan(res):
            res = integral_log(a, b, c)

        self.integral_bounds_text.set(self.header(a, b))
        self.integral_bounds_label.pack()

        self.integral_function_text.set(format_log(c))
        self.integral_function_label.pack()
        return res

    def header(self, a: float, b: float) -> str:
        return 'Calculez l\'intégrale f(x)dx allant de {:0.1f} à {:0.1f} avec :\n'.format(a, b)
