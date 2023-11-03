import math


def area_of_circle(radius):
    return math.pi * radius**2


def area_of_square(side_length):
    return side_length**2


if __name__ == "__main__":
    radius = float(input("Enter radius: "))
    side_length = float(input("Enter side length: "))

    print("Area of circle: ", area_of_circle(radius))
    print("Area of square: ", area_of_square(side_length))

    print(
        "Area of circle is greater than area of square: "
        if area_of_circle(radius) > area_of_square(side_length)
        else "Area of square is greater than area of a circle:"
    )
