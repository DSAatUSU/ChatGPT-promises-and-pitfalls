# This tkinter GUI destroys itself when clicked

import tkinter as tk

root = tk.Tk()

def on_click(event):
    root.destroy()

canvas = tk.Canvas(root, width=600, height=400)
canvas.bind("<Button-1>", on_click)
canvas.pack()

canvas.focus_set

root.mainloop()
