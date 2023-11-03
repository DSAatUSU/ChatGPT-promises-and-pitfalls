import math

def pythagorean_theorem():
    # Get the lengths of the two known sides from the user
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input("Enter the length of side B: "))
    
    # Calculate the length of the missing side (side C)
    side_c = math.sqrt(side_a**2 + side_b**2)
    
    # Print the result
    print(f"The length of side C is {side_c:.2f}")

# Run the function
pythagorean_theorem()
