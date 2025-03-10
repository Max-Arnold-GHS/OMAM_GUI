import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Soledad Portal")
        self.geometry("275x200")

        self.label = tk.Label(self, text="Please click the buttons below:")
        self.label.grid(row=1, column=1, columnspan=5, padx=50, pady=30)

        self.button1 = tk.Button(self, text="1", command=lambda: print("1"))
        self.button1.grid(row=2, column=1, padx=5, pady=5)

        self.button2 = tk.Button(self, text="2", command=lambda: print("2"))
        self.button2.grid(row=2, column=3, padx=5, pady=5)

        self.button3 = tk.Button(self, text="3", command=lambda: print("3"))
        self.button3.grid(row=2, column=5, padx=5, pady=5)

if __name__ == "__main__":
    app = Main()
    app.mainloop()