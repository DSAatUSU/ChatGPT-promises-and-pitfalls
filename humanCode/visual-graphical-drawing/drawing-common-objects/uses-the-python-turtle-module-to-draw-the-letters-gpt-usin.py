# python program for printing "GFG"
# importing turtle modules
import turtle

# setting up workscreen
ws = turtle.Screen()

# defining turtle instance
t = turtle.Turtle()

# turtle pen will be of "GREEN" color
t.color("Green")

# setting width of pen
t.width(3)


# for printing letter "G"
for x in range(180):
    t.backward(1)
    t.left(1)
t.right(90)
t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(50)

# for printing letter "P"
t.penup()
t.goto(45, 0)
t.pendown()
# t.right(90)
t.forward(115)
t.backward(55)
t.left(90)
t.circle(30, 180)


t.penup()
t.goto(120, 0)
t.pendown()
t.left(90)
t.forward(115)
t.backward(115)
t.right(90)
t.forward(30)
t.backward(60)

turtle.done()
turtle.bye()
