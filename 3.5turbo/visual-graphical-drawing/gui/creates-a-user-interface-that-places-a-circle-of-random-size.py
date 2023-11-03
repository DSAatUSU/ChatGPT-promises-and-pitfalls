import tkinter as tk
import random

def create_circle(event):
    size = random.randint(10, 50)
    color = generate_random_color()
    
    x = event.x
    y = event.y
    
    canvas.create_oval(x-size, y-size, x+size, y+size, fill=color)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return '#%02x%02x%02x' % (r, g, b)

# Create the main window
window = tk.Tk()
window.title("Random Circle Generator")

# Create the canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Bind the mouse click event to the canvas
canvas.bind("<Button-1>", create_circle)

# Start the main event loop
window.mainloop()
