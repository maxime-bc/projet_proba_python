import tkinter as tk
import src.menu

LARGE_FONT = ('Verdana', 12)


class Exercise2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.score = self.controller.shared_data["score"]
        self.max_score = self.controller.shared_data["max_score"]

        label = tk.Label(self, text="Intégrales", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        back_button = tk.Button(self, text='Retour', command=lambda: controller.show_frame(src.menu.Menu))
        back_button.pack()
