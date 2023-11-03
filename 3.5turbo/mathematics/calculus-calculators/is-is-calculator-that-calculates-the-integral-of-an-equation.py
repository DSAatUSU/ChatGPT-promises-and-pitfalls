import sympy as sp

def calculate_integral():
    # Get the equation from the user
    equation = input("Enter an equation to calculate the integral: ")

    # Create a symbol for the variable used in the equation
    x = sp.symbols('x')

    try:
        # Parse the equation and calculate the integral
        integral = sp.integrate(equation, x)
        return integral
    
    except Exception as e:
        print("Error: ", e)
        return None

# Call the function to calculate the integral
result = calculate_integral()

# Print the result
if result:
    print("The integral is:", result)
else:
    print("Failed to calculate the integral.")
