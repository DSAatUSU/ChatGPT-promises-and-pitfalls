import turtle

def draw_tree(branch_len, angle):
    """
    Recursive function to draw a tree fractal.

    Args:
        branch_len (int): Length of the branch.
        angle (int): Angle of rotation.

    Returns:
        None
    """
    if branch_len < 5: # Base case, stop recursion when branch length is small enough
        return
    else:
        # Draw the main branch
        turtle.forward(branch_len)
        turtle.right(angle)

        # Recursive call for the right sub-branch
        draw_tree(branch_len * 0.6, angle)

        # Recursive call for the left sub-branch
        turtle.left(2 * angle)
        draw_tree(branch_len * 0.6, angle)

        # Reset turtle position and angle
        turtle.right(angle)
        turtle.backward(branch_len)

def main():
    # Initialize turtle
    turtle.speed(0) # Set the drawing speed to the fastest
    turtle.left(90) # Start at the top of the tree

    # Draw the tree
    draw_tree(100, 30)

    # Hide the turtle
    turtle.hideturtle()

    # Keep the window open until it is manually closed
    turtle.mainloop()

if __name__ == "__main__":
    main()
