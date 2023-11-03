import turtle

call = 0


def make_sierpinski(levels=2):
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
        global call
        call += 1
        print("\ncall is", call)
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

    t = turtle.Turtle()
    t.speed()
    wn = turtle.Screen()
    wn.bgcolor("black")
    p = [[-500, -400], [0, 500], [500, -400]]
    sierpinski(t, levels, p)
    wn.exitonclick()


def main():
    make_sierpinski(2)


main()
