# Python program to print complete Koch Curve.
from turtle import *


def make_snowflake(length, levels):
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


# main function
if __name__ == "__main__":
    # defining the speed of the turtle
    speed(0)
    length = int(input("Input the length (size) of the snowflake: "))
    levels = int(input("Input number of levels (Itteration) of the snowflake: "))

    make_snowflake(length, levels)
