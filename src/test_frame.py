import tkinter as tk
from src.format import format_quadratic_equation
from src.quadratic_equations import solve_quadratic_equation
from src.rand import randrange_step, randrange_exclude, START_VALUE, STOP_VALUE, STEP_VALUE
from src.utils import round_double

LARGE_FONT = ('Verdana', 12)


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

        for f in (MainPage, Exercise1, Exercise2):

            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()


class MainPage(tk.Frame):

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
                    self.controller.show_frame(Exercise1)

                else:
                    self.controller.show_frame(Exercise2)

        except ValueError:
            pass


class Exercise1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        self.score = self.controller.shared_data["score"]
        self.max_score = self.controller.shared_data["max_score"]

        self.res1: float
        self.res2: float
        self.sol_no: int

        frame_label = tk.Label(self, text="Equation du second degré", font=LARGE_FONT)
        frame_label.pack(padx=10, pady=10)

        self.entry_array = [None] * 2
        self.label_array = [None] * 2

        self.equation_str = tk.StringVar()
        self.equation_label = tk.Label(self, textvariable=self.equation_str, font=LARGE_FONT)
        self.equation_label.pack(padx=10, pady=10)

        sol_label = tk.Label(self, text="Nombre de solutions :", font=LARGE_FONT)
        sol_label.pack()

        self.previous_spinbox_value = 0
        self.sol_no_spinbox = tk.Spinbox(self, from_=0, to=2, command=self.on_spinbox_changed)
        self.sol_no_spinbox.pack()

        for index in range(0, 2):
            self.label_array[index] = tk.Label(self, text='Solution '+str(index+1))
            self.label_array[index].pack()
            self.hide_widget(self.label_array[index])

            self.entry_array[index] = tk.Entry(self)
            self.entry_array[index].pack()
            self.hide_widget(self.entry_array[index])

        # self.sol_button = tk.Button(self, text='', command=self.start)

        self.validate_button = tk.Button(self, text='Valider', command=self.check_answers)
        self.validate_button.pack()

        self.back_button = tk.Button(self, text='Retour', command=lambda: controller.show_frame(MainPage))
        self.back_button.pack()

    def on_show_frame(self, event):
        # Generate a new exercise
        print("I am being shown...")

        a: float = randrange_exclude(0.0, START_VALUE, STOP_VALUE, STEP_VALUE)
        b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
        c: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

        self.res1, self.res2, self.sol_no = solve_quadratic_equation(a, b, c)

        self.equation_str.set('Equation du 2nd degré générée : {}\nRésoudre f(x) = 0'.format(format_quadratic_equation(a, b, c)))
        self.equation_label.pack()

        # DEBUG ONLY
        print('NB SOL : '+str(self.sol_no))
        if self.sol_no == 1:
            print('SOL : {}'.format(self.res1))
        elif self.sol_no == 2:
            print('SOLS : {} {}'.format(self.res1, self.res2))

    @staticmethod
    def hide_widget(event):
        event.pack_forget()

    @staticmethod
    def show_widget(event):
        event.pack()

    def check_answers(self):
        print('Validating')

        if self.sol_no == int(self.sol_no_spinbox.get()):

            if self.sol_no == 0:
                print('OUI, pas de sol')

            if self.sol_no == 1:
                rounded_res1 = round_double(self.res1)

                try:
                    answer1 = float(self.entry_array[0].get())

                    if answer1 == rounded_res1:

                        print('OUI')
                        self.score = self.score + 1.0
                        self.max_score = self.max_score + 1.0

                    else:

                        print('NON')
                        self.max_score = self.max_score + 1.0

                except ValueError:
                    print('NOT AN INT !')

            elif self.sol_no == 2:
                rounded_res1 = round_double(self.res1)
                rounded_res2 = round_double(self.res2)

                try:
                    answer1 = float(self.entry_array[0].get())
                    answer2 = float(self.entry_array[1].get())

                    if answer1 == rounded_res1 and answer2 == rounded_res2:
                        print('Bravo ! \nEn effet, cette équation possède deux solutions : '
                              '{:0.2f} et {:0.2f}\n'.format(rounded_res1, rounded_res2))
                        self.score = self.score + 1.0
                        self.max_score = self.max_score + 1.0

                    else:

                        if answer1 == rounded_res1 and answer2 == rounded_res1:
                            print('Bravo ! \nEn effet, cette équation possède deux solutions : '
                                  '{:0.2f} et {:0.2f}\n'.format(rounded_res1, rounded_res2))
                            self.score = self.score + 1.0
                            self.max_score = self.max_score + 1.0

                        else:
                            print('Faux ! \nCette équation possède deux solutions : '
                                  '{:0.2f} et {:0.2f}\n'.format(rounded_res1, rounded_res2))
                            self.max_score = self.max_score + 1.0

                except ValueError:
                    print('NOT AN INT !')

        else:
            print('Erreur nb sol')

    def on_spinbox_changed(self):

        self.hide_widget(self.validate_button)
        self.hide_widget(self.back_button)

        actual_spinbox_value = int(self.sol_no_spinbox.get())
        print('Actual : '+str(actual_spinbox_value))
        print('Previous : ' + str(self.previous_spinbox_value))

        if actual_spinbox_value > self.previous_spinbox_value:
            self.show_widget(self.label_array[actual_spinbox_value - 1])
            self.show_widget(self.entry_array[actual_spinbox_value-1])
            self.previous_spinbox_value = actual_spinbox_value
            self.validate_button.pack()

        elif actual_spinbox_value < self.previous_spinbox_value:
            self.hide_widget(self.label_array[actual_spinbox_value - 1])
            self.hide_widget(self.entry_array[actual_spinbox_value-1])
            self.previous_spinbox_value = actual_spinbox_value
            self.validate_button.pack()

        self.show_widget(self.validate_button)
        self.show_widget(self.back_button)


class Exercise2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.score = self.controller.shared_data["score"]
        self.max_score = self.controller.shared_data["max_score"]

        label = tk.Label(self, text="Intégrales", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        back_button = tk.Button(self, text='Retour', command=lambda: controller.show_frame(MainPage))
        back_button.pack()

