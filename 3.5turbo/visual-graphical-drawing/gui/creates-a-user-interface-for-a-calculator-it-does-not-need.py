import tkinter as tk

# Create the Calculator class
class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        
        # Create the display label
        self.display = tk.Label(master, width=20, height=2, font=("Arial", 20))
        self.display.pack()

# Create the root window
root = tk.Tk()

# Create an instance of the Calculator class
calc = Calculator(root)

# Run the event loop
root.mainloop()