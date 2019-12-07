import tkinter as tk
from tkinter import ttk

from src.rand import randrange_step

LARGE_FONT = ('Verdana', 12)


class App(tk.Tk):

    def __init__(self):

        super().__init__()
        self.geometry("720x480")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.shared_data = {
            "weight1": 5,
            "weight2": 5,
            "score": 0.0,
            "total_score": 0.0
        }

        self.frames = {}

        for f in (MainPage, Exercise1, Exercise2):

            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.score = self.controller.shared_data["score"]
        self.total_score = self.controller.shared_data["total_score"]
        self.weight1 = self.controller.shared_data["weight1"]
        self.weight2 = self.controller.shared_data["weight2"]

        weight1_bind = tk.IntVar()
        weight1_bind.set(self.weight1)

        label = tk.Label(self, text='MENU', font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        self.weight1_label = tk.Label(self, text='Poids exercice 1 : ')
        self.weight1_label.pack()
        self.weight_entry = tk.Entry(self, text=weight1_bind)
        self.weight_entry.pack()

        self.weight2_label = tk.Label(self, text='Poids exercice 2 : {}'.format(self.weight2))
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
        label = tk.Label(self, text="Exercise 1", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        back_button = tk.Button(self, text='Retour', command=lambda: controller.show_frame(MainPage))
        back_button.pack()


class Exercise2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Exercise 2", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        back_button = tk.Button(self, text='Retour', command=lambda: controller.show_frame(MainPage))
        back_button.pack()


app = App()
app.mainloop()
