# Import necessary libraries
import random
import turtle
from turtle import *

# Set up the turtle
window = turtle.Screen()
turtle.speed(0)


def drawsquare50(size=50):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)


if __name__ == "__main__":
    colors = ["red", "green", "blue", "yellow", "purple", "pink", "orange"]
    while colors != []:
        set_color = random.choice(colors)
        for count in range(1, 8, 1):
            # Set the color
            color(set_color)
            random_size = random.randint(10, 100)
            drawsquare50(random_size)
            penup()
            # jump to a random location on the screen
            setx(random.randint(-200, 200))
            sety(random.randint(-200, 200))
            pendown()
        colors.remove(set_color)

    # Hide the turtle
    turtle.hideturtle()

    # Exit on click
    window.exitonclick()
