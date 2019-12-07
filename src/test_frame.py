import tkinter as tk

LARGE_FONT = ('Verdana', 12)


class App(tk.Tk):

    def __init__(self):

        super().__init__()
        self.geometry("720x480")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, PageOne, PageTwo):

            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text='Visit page 1', command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text='Visit page 2', command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text='Back to home', command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        label = tk.Label(self, text='random text')
        label.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text='Back to home', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text='Page One', command=lambda: controller.show_frame(PageOne))
        button2.pack()

        label = tk.Label(self, text='random text')
        label.pack()



app = App()
app.mainloop()
