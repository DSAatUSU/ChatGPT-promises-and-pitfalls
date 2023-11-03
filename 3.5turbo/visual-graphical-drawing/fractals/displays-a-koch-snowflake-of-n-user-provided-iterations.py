import turtle


def draw_koch_curve(t, initial_length, iteration):
    """
    Function to draw a koch curve recursively using turtle graphics

    :param t: turtle object
    :param initial_length: initial line length
    :param iteration: number of iterations
    :return: None
    """
    if iteration == 0:
        t.forward(initial_length)
    else:
        length = initial_length / 3
        draw_koch_curve(t, length, iteration-1)
        t.left(60)
        draw_koch_curve(t, length, iteration-1)
        t.right(120)
        draw_koch_curve(t, length, iteration-1)
        t.left(60)
        draw_koch_curve(t, length, iteration-1)


def draw_koch_snowflake(t, initial_length, iteration):
    """
    Function to draw a koch snowflake using turtle graphics

    :param t: turtle object
    :param initial_length: initial line length
    :param iteration: number of iterations
    :return: None
    """
    for _ in range(3):
        draw_koch_curve(t, initial_length, iteration)
        t.right(120)


def main():
    # Get user input
    iterations = int(input("Enter the number of iterations: "))
    
    # Set up turtle graphics
    screen = turtle.Screen()
    screen.setup(800, 800)
    turtle.speed(0)
    turtle.hideturtle()
    
    # Draw koch snowflake
    draw_koch_snowflake(turtle, 300, iterations)
    
    # Exit on screen click
    screen.exitonclick()


if __name__ == '__main__':
    main()