import turtle

# Create a turtle object
smiley = turtle.Turtle()

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set the turtle properties
smiley.shape("turtle")
smiley.speed(3)
smiley.color("black", "yellow")

# Draw the face
smiley.begin_fill()
smiley.circle(100)
smiley.end_fill()

# Draw the eyes
smiley.penup()
smiley.goto(-40, 120)
smiley.pendown()
smiley.color("black", "black")
smiley.begin_fill()
smiley.circle(15)
smiley.end_fill()

smiley.penup()
smiley.goto(40, 120)
smiley.pendown()
smiley.color("black", "black")
smiley.begin_fill()
smiley.circle(15)
smiley.end_fill()

# Draw the mouth
smiley.penup()
smiley.goto(-40, 85)
smiley.pendown()
smiley.color("black")
smiley.width(10)
smiley.setheading(-60)
smiley.circle(70, 120)
smiley.penup()

# Hide the turtle
smiley.hideturtle()

# Exit on click
turtle.done()