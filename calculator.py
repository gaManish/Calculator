import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple - Calculator")
        self.equation = tk.StringVar()
        self.result = ""

        # create the equation label
        equation_label = tk.Label(master, textvariable=self.equation, font=("Arial", 20), anchor="e", bg="white", bd=5)
        equation_label.pack(fill="both")

        # create the buttons
        buttons_frame = tk.Frame(master)
        buttons_frame.pack()

        buttons_list = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", ".", "0", "=", "+"]
        for i, button_text in enumerate(buttons_list):
            button = tk.Button(buttons_frame, text=button_text, font=("Arial", 20), bg="white", bd=2, padx=10, pady=10, command=lambda x=button_text: self.button_click(x))
            button.grid(row=i//4, column=i%4)

        # create the clear button
        clear_button = tk.Button(master, text="Clear", font=("Arial", 20), bg="white", bd=2, padx=10, pady=10, command=self.clear)
        clear_button.pack(fill="both")

    def button_click(self, button_text):
        if button_text == "=":
            try:
                self.result = str(eval(self.equation.get()))
            except ZeroDivisionError:
                self.result = "Error: Division by zero"
            except:
                self.result = "Error: Invalid input"
            self.equation.set(self.result)
        else:
            self.equation.set(self.equation.get() + button_text)

    def clear(self):
        self.equation.set("")
        self.result = ""

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
