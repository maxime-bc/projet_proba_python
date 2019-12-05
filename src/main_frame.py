import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.geometry("720x480")

        self.weight1: int = 5
        self.weight2: int = 5

        variable = tk.IntVar()
        variable.set(self.weight1)

        self.title = tk.Label(root, text="Exercices sur les polynomes du 2nd degré et les inétgrales",
                               bg="#E74C3C", fg="white")
        self.title.pack(fill='both', padx=10, expand=True)

        self.start_button = tk.Button(root, text="Commencer", bg="#2ECC71", fg="black", command=self.start)
        self.start_button.pack(fill='both', padx=10, expand=True)

        self.weight1_label = tk.Label(root, text='Poids exercice 1 : ')
        self.weight1_label.pack(side='left', padx=10)

        self.weight_entry = tk.Entry(root, text=variable)
        self.weight_entry.pack(side='left', padx=10)

        self.weight2_label = tk.Label(root, text='Poids exercice 2 : {}'.format(self.weight2))
        self.weight2_label.pack(side='left', padx=10)

    def create_window(self):
        window = tk.Toplevel(self.master)

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

                # https://stackoverflow.com/questions/35434654/closing-current-window-when-opening-another-window
                self.create_window()

                print('Nouveaux poids : \n '
                      'ex1 = {}\n '
                      'ex2 = {}\n'.format(self.weight1, self.weight2))

        except ValueError:
            pass


root = tk.Tk()
app = Application(master=root)
app.mainloop()
