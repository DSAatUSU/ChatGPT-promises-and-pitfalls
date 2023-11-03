import math
import sys

# Main menu
def main():
    choice = input("Which operation would you like?\n" "1) Area\n" "2) Volume\n")
    if choice == "1":
        area()
    elif choice == "2":
        volume()


# Menu to choose which area you'd like to calculate
def area():
    choice = input(
        "Please enter what you'd like to calculate\n"
        "1) Area of a sphere\n"
        "2) Area of a cube\n"
        "3) Area of a cone\n"
        "7) Quit\n"
        "8) Main Menu\n"
    )

    try:
        if choice == "1":
            area_of_sphere()

        elif choice == "2":
            area_of_cube()

        elif choice == "3":
            area_of_cone()

        elif choice == "7":
            sys.exit("Choice 8 selected.  Quitting...")

        elif choice == "8":
            main()

        else:
            print("I didn't understand your input!")
            main()
    except NameError:
        print("You forgot to define a function!")
        area()


# Volume main menu
def volume():
    choice = input(
        "Please enter what you'd like to calculate\n"
        "1) Volume of a cube\n"
        "2) Volume of a sphere\n"
        "3) Volume of a cone\n"
        "7) Quit\n"
        "8) Main menu\n"
    )
    try:
        if choice == "1":
            volume_of_cube()

        elif choice == "2":
            volume_of_sphere()

        elif choice == "3":
            volume_of_cone()

        elif choice == "7":
            sys.exit("Option 7 selected.  Quitting...")

        elif choice == "8":
            main()

        else:
            print("I didn't understand your input!")
            volume()

    except NameError:
        print("Programmer forgot to define a function!")
        volume()


def area_of_sphere():
    try:
        r = int(input("The area of your sphere is... "))
        area = 4 * math.pi * r**2
        print(area)
    except ValueError:
        print("You entered alphabetic characters!  Please enter integers only.")
        area_of_sphere()


def area_of_cube():
    try:
        a = int(input("Enter an edge of your cube... "))
        area = 6 * a**2
        print("The area of your cube is {0}".format(area))
    except ValueError:
        print("You entered alphabetic characters!  Please enter integers only.")
        area_of_cube()


def area_of_cone():
    try:
        r = int(input("Enter the radius... "))
        h = int(input("Enter the height... "))
        area = (math.pi * r) * (r + math.sqrt(h**2 + r**2))
        print("The area of your cone is {0}".format(area))
    except ValueError:
        print("You entered alphabetic characters!  Please enter integers only.")
        area_of_cone()


def volume_of_sphere():
    try:
        r = int(input("Enter the radius of your sphere... "))
        volume = 4 / 3 * math.pi * r**3
        print("The volume of your sphere is {0}".format(volume))
    except ValueError:
        print("You entered alphabetic characters!  Please enter integers only.")
        volume_of_sphere()


def volume_of_cube():
    try:
        a = int(input("Enter an edge of your cube... "))
        volume = a**3
        print("The volume of your cube is {0}".format(volume))
    except ValueError:
        print("You entered alphabetic characters!  Please enter integers only.")
        volume_of_cube()


def volume_of_cone():
    try:
        r = int(input("Enter the radius... "))
        h = int(input("Enter the height... "))
        volume = math.pi * r**2 * h / 3
        print("The volume of the cone is {0}".format(volume))
    except ValueError:
        print("You entered alphabetic characters!  Please enter integers only.")
        volume_of_cone()


if __name__ == "__main__":
    main()
