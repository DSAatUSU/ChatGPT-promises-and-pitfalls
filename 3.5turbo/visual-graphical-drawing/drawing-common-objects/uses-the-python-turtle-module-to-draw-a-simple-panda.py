import turtle

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x - width/2, y - height/2)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(0)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_panda():
    turtle.speed(2)
    turtle.bgcolor('white')

    # Draw head
    draw_circle(0, 100, 100, 'black')

    # Draw ears
    draw_circle(-40, 180, 30, 'black')
    draw_circle(40, 180, 30, 'black')

    # Draw eyes
    draw_circle(-35, 150, 10, 'white')
    draw_circle(45, 150, 10, 'white')
    draw_circle(-30, 140, 5, 'black')
    draw_circle(50, 140, 5, 'black')

    # Draw nose
    draw_circle(5, 120, 20, 'black')

    # Draw mouth
    draw_rectangle(-25, 120, 50, 20, 'black')

    # Draw body
    draw_circle(0, 0, 80, 'black')

    # Draw arms
    draw_rectangle(-70, -50, 20, 100, 'black')
    draw_rectangle(50, -50, 20, 100, 'black')

    # Draw legs
    draw_rectangle(-30, -150, 20, 80, 'black')
    draw_rectangle(10, -150, 20, 80, 'black')

    turtle.hideturtle()
    turtle.done()

# Call the draw_panda() function to draw the panda
draw_panda()
