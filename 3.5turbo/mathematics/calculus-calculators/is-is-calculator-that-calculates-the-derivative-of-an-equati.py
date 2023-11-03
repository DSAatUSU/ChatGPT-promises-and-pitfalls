import sympy as sp

def derivative_calculator():
    # Ask the user for the equation
    equation = input("Enter the equation: ")

    # Convert the equation to a symbolic expression
    x = sp.Symbol('x')
    expr = sp.sympify(equation)

    # Calculate the derivative of the equation
    derivative = sp.diff(expr, x)

    # Print the result
    print("Derivative of the equation:", derivative)

# Run the derivative_calculator function
if __name__ == "__main__":
    derivative_calculator()
