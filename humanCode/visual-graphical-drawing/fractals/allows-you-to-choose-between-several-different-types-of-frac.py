from turtle import *

def make_koch_fractal(length, levels=2):
    # function to create koch snowflake or koch curve
    def snowflake(lengthSide, levels):
        if levels == 0:
            forward(lengthSide)
            return
        lengthSide /= 3.0
        snowflake(lengthSide, levels - 1)
        left(60)
        snowflake(lengthSide, levels - 1)
        right(120)
        snowflake(lengthSide, levels - 1)
        left(60)
        snowflake(lengthSide, levels - 1)

    penup()

    backward(length / 2.0)

    # Pull the pen down – drawing when moving.
    pendown()
    for i in range(3):
        snowflake(length, levels)
        right(120)


def make_sierpinski_fractal(levels=2):
    def draw(t, color, p):
        t.fillcolor(color)
        t.up()
        t.goto(p[0][0], p[0][1])
        t.down()
        t.begin_fill()
        t.goto(p[1][0], p[1][1])
        t.goto(p[2][0], p[2][1])
        t.goto(p[0][0], p[0][1])
        t.end_fill()

    def mid(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def sierpinski(t, order, p):
   
        colormap = ["red", "orange", "yellow", "green", "blue", "violet"]
        print("  draw", colormap[order], "at", p)
        draw(t, colormap[order], p)
        print("     outer call done, order =", order)
        if order > 0:
            sierpinski(t, order - 1, [p[0], mid(p[0], p[1]), mid(p[0], p[2])])
            print("       1st recursive call done, order =", order)
            sierpinski(t, order - 1, [p[1], mid(p[0], p[1]), mid(p[1], p[2])])
            print("       2nd recursive call done, order =", order)
            sierpinski(t, order - 1, [p[2], mid(p[2], p[1]), mid(p[0], p[2])])
            print("       3rd recursive call done, order =", order)
    t = Turtle()
    t.speed()
    wn = Screen()
    wn.bgcolor("black")
    p = [[-500, -400], [0, 500], [500, -400]]
    sierpinski(t, levels, p)
    wn.exitonclick()


# function to plot a Y
def make_tree_fractal(sz, level=7):
    speed('fastest')
      
    # turning the turtle to face upwards
    rt(-90)
      
    # the acute angle between
    # the base and branch of the Y
    angle = 30
      
    # function to plot a Y
    def y(sz=80, level=7):   
      
        if level > 0:
            colormode(255)
              
            # splitting the rgb range for green
            # into equal intervals for each level
            # setting the colour according
            # to the current level
            pencolor(0, 255//level, 0)
              
            # drawing the base
            fd(sz)
      
            rt(angle)
      
            # recursive call for
            # the right subtree
            y(0.8 * sz, level-1)
              
            pencolor(0, 255//level, 0)
              
            lt( 2 * angle )
      
            # recursive call for
            # the left subtree
            y(0.8 * sz, level-1)
              
            pencolor(0, 255//level, 0)
              
            rt(angle)
            fd(-sz)
           
          
    # tree of size 80 and level 7
    y(sz, level)


speed("fastest")


if __name__ == "__main__":

    reset()
    type_of_fractal = input("What type of fractal would you like to draw? (koch, sierpinski, tree) ")
    itteration = int(input("How many itterations would you like to do? "))
    
    if type_of_fractal == "koch":
        make_koch_fractal(80, itteration)
    elif type_of_fractal == "sierpinski":
        make_sierpinski_fractal(itteration)
    elif type_of_fractal == "tree":
        make_tree_fractal(80, itteration)
    else:
        print("That is not a valid fractal type.")


    exitonclick()