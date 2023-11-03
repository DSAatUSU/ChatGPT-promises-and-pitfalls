import turtle

def move_to(x, y):
    turtle.goto(x, y)  # Move turtle to the clicked position
    turtle.stamp()  # Leave a stamp at the position

def main():
    turtle.speed(0)  # Set the turtle's speed to the fastest

    turtle.onscreenclick(move_to)  # Call move_to function when the mouse is clicked

    turtle.mainloop()  # Start the turtle's main loop

if __name__ == "__main__":
    main()
