import turtle

# Constants for the size of each square on the chessboard
SQUARE_SIZE = 50
BOARD_SIZE = 8

def draw_chessboard():
    # Set up the turtle
    screen = turtle.Screen()
    screen.title("Chessboard")
    turtle.setup(BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE)
    turtle.penup()
    
    # Start drawing the chessboard
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Determine the position of the current square
            x = col * SQUARE_SIZE - (BOARD_SIZE * SQUARE_SIZE) / 2
            y = row * SQUARE_SIZE - (BOARD_SIZE * SQUARE_SIZE) / 2
            
            # Move the turtle to the current square's position
            turtle.goto(x, y)
            
            # Determine the color of the current square
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "black"
            
            # Draw the current square
            turtle.fillcolor(color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(SQUARE_SIZE)
                turtle.right(90)
            turtle.end_fill()

    # Hide the turtle
    turtle.hideturtle()

    # Keep the turtle window open until it is closed
    turtle.done()

# Call the function to draw the chessboard
draw_chessboard()
