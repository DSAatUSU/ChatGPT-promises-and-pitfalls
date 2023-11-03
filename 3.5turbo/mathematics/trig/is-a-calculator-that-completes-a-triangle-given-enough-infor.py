import math

def calculate_triangle():
    # Get input from user
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    side_c = float(input("Enter the length of side c: "))
    angle_A = float(input("Enter the angle A in degrees: "))
    angle_B = float(input("Enter the angle B in degrees: "))
    angle_C = float(input("Enter the angle C in degrees: "))

    # Calculate missing angles
    if not angle_A:
        angle_A = 180 - angle_B - angle_C
    elif not angle_B:
        angle_B = 180 - angle_A - angle_C
    elif not angle_C:
        angle_C = 180 - angle_A - angle_B

    # Calculate missing side lengths
    if not side_a:
        side_a = math.sqrt(side_b**2 + side_c**2 - 2 * side_b * side_c * math.cos(math.radians(angle_A)))
    elif not side_b:
        side_b = math.sqrt(side_c**2 + side_a**2 - 2 * side_c * side_a * math.cos(math.radians(angle_B)))
    elif not side_c:
        side_c = math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(math.radians(angle_C)))

    # Calculate remaining angles
    if not angle_A:
        angle_A = math.degrees(math.acos((side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)))
    elif not angle_B:
        angle_B = math.degrees(math.acos((side_c**2 + side_a**2 - side_b**2) / (2 * side_c * side_a)))
    elif not angle_C:
        angle_C = math.degrees(math.acos((side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)))

    # Print the calculated values
    print(f"Side a: {side_a}")
    print(f"Side b: {side_b}")
    print(f"Side c: {side_c}")
    print(f"Angle A: {angle_A}")
    print(f"Angle B: {angle_B}")
    print(f"Angle C: {angle_C}")

# Call the main function
calculate_triangle()
