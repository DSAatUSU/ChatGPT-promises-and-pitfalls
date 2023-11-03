import math

def convert_radians_to_degrees(radians):
    """
    Convert radians to degrees.
    """
    degrees = math.degrees(radians)
    return degrees

if __name__ == '__main__':
    radians = float(input("Enter the value in radians: "))
    degrees = convert_radians_to_degrees(radians)
    print(f"{radians} radians is equal to {degrees} degrees.")
