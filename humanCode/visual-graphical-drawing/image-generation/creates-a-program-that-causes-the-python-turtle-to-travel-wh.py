import turtle


def move_to_mouseclick():
    turtle.speed(0)  # Set the turtle's speed to the fastest

    turtle.onscreenclick(turtle.goto)  # Call move_to function when the mouse is clicked

    turtle.mainloop()  # Start the turtle's main loop


if __name__ == "__main__":
    move_to_mouseclick()
