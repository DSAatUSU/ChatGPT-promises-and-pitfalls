# Import the required libraries
from tkinter import *
from tkinter import ttk
import random

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("1000x1000")

# Define a function to draw the line between two points
def draw_line(event):
    global click_num
    global x1, y1
    if click_num == 0:
        size = random.randint(50, 100)
        x1 = event.x
        y1 = event.y
        click_num += 1
        random_color = "#%06x" % random.randint(0, 0xFFFFFF)
        # Drop a temporary marker to show the first click
        canvas.create_oval(
            x1 - size,
            y1 - size,
            x1 + size,
            y1 + size,
            fill=random_color,
            outline=str(random_color),
        )

    else:
        # Clear the line after 2 seconds
        win.after(1, canvas.delete, "all")
        click_num = 0


# Create a canvas widget
canvas = Canvas(win, width=1000, height=1000, background="white")
canvas.grid(row=0, column=0)
canvas.bind("<Button-1>", draw_line)
click_num = 0

win.mainloop()
