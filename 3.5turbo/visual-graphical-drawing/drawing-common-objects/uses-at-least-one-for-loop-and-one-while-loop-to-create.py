# Import necessary libraries
import random
import turtle

# Set up the turtle
window = turtle.Screen()
window.bgcolor("black")
turtle.speed(0)

# Function to generate a random color
def randcol():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    color = random.choice(colors)
    return color

# Loop to draw the abstract design
for _ in range(36):
    turtle.color(randcol())
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)

# Hide the turtle
turtle.hideturtle()

# Exit on click
window.exitonclick()
