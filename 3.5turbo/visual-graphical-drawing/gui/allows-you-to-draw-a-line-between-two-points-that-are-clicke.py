import tkinter as tk

def draw_line(event):
    global start_x, start_y
    if start_x is None:
        start_x = event.x
        start_y = event.y
    else:
        canvas.create_line(start_x, start_y, event.x, event.y)
        start_x = None
        start_y = None

def clear_canvas():
    canvas.delete("all")

def main():
    global canvas, start_x, start_y
    start_x = None
    start_y = None

    root = tk.Tk()
    root.title("Draw Line")
    
    # Create Canvas
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    # Bind mouse click event to draw_line function
    canvas.bind("<Button-1>", draw_line)

    # Create Clear Button
    clear_button = tk.Button(root, text="Clear", command=clear_canvas)
    clear_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
