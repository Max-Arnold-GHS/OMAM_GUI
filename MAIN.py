import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main")

        self.button = tk.Button(self, text="Open", command=self.open_window)
        self.button.pack()