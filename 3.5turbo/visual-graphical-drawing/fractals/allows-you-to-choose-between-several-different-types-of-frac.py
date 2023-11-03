import turtle

def draw_fractal(x, y, length, angle, iterations, fractal_type):
    # Base case
    if iterations == 0:
        return

    # Different fractal patterns based on type
    if fractal_type == "koch":
        fractal_koch(x, y, length, angle, iterations)
    elif fractal_type == "tree":
        fractal_tree(x, y, length, angle, iterations)
    elif fractal_type == "sierpinski":
        fractal_sierpinski(x, y, length, iterations)
    else:
        print("Invalid fractal type")

def fractal_koch(x, y, length, angle, iterations):
    if iterations == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        fractal_koch(x, y, length, angle, iterations-1)
        turtle.left(angle)
        fractal_koch(x, y, length, angle, iterations-1)
        turtle.right(angle * 2)
        fractal_koch(x, y, length, angle, iterations-1)
        turtle.left(angle)
        fractal_koch(x, y, length, angle, iterations-1)

def fractal_tree(x, y, length, angle, iterations):
    if iterations == 0:
        return
    else:
        turtle.forward(length)
        turtle.left(angle)
        fractal_tree(x, y, length * 0.7, angle, iterations-1)
        turtle.right(angle * 2)
        fractal_tree(x, y, length * 0.7, angle, iterations-1)
        turtle.left(angle)
        turtle.backward(length)

def fractal_sierpinski(x, y, length, iterations):
    if iterations == 0:
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        fractal_sierpinski(x, y, length / 2, iterations-1)
        turtle.forward(length / 2)
        fractal_sierpinski(x, y, length / 2, iterations-1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        fractal_sierpinski(x, y, length / 2, iterations-1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

def main():
    turtle.speed(0)  # Set the turtle speed to the fastest
    turtle.hideturtle()
    x = y = -200  # Initial position of the turtle
    length = 200  # Length of the initial fractal line
    angle = 60  # Angle for fractal patterns
    
    fractal_type = input("Choose a fractal type(koch/tree/sierpinski): ")
    iterations = int(input("Enter the number of iterations: "))
    
    draw_fractal(x, y, length, angle, iterations, fractal_type)
    turtle.done()

if __name__ == "__main__":
    main()
