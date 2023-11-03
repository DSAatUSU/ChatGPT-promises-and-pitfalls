from turtle import *

speed("fastest")


# function to plot a Y
def tree_fractal(sz, level):
    # turning the turtle to face upwards
    rt(-90)

    # the acute angle between
    # the base and branch of the Y
    angle = 30
    if level > 0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255 // level, 0)

        # drawing the base
        fd(sz)

        rt(angle)

        # recursive call for
        # the right subtree
        tree_fractal(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        lt(2 * angle)

        # recursive call for
        # the left subtree
        tree_fractal(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)


# tree of size 80 and level 7
tree_fractal(80, 7)
