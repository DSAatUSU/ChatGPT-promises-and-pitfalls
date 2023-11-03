# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("1000x1000")

# Define a function to draw the line between two points
def draw_line(event):
    global click_num
    global x1, y1
    if click_num == 0:
        x1 = event.x
        y1 = event.y
        click_num = 1
        # Drop a temporary marker to show the first click
        canvas.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill="red")
    elif click_num == 1:
        x2 = event.x
        y2 = event.y
        # Draw the line in the given co-ordinates
        canvas.create_oval(x2 - 5, y2 - 5, x2 + 5, y2 + 5, fill="red")
        canvas.create_line(x1, y1, x2, y2, fill="green", width=2)
        click_num += 1
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
