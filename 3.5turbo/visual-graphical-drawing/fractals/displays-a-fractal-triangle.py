import turtle

def draw_fractal(length, depth):
    if depth == 0:
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
    else:
        draw_fractal(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_fractal(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_fractal(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

def main():
    turtle.speed(0)  # Set the turtle speed to the maximum
    length = 200     # Length of the initial triangle side
    depth = 4        # Recursive depth (increase for more detail)
    
    draw_fractal(length, depth)
    turtle.done()

if __name__ == "__main__":
    main()
