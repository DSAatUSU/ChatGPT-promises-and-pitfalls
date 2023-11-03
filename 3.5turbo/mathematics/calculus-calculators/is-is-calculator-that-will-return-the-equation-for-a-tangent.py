import sympy as sp

def tangent_line_equation():
    # Get the equation
    equation = input("Enter the equation: ")
    
    # Get the point
    x = float(input("Enter the x-coordinate of the point: "))
    y = float(input("Enter the y-coordinate of the point: "))
    
    # Define the variable
    sp.var('x')
    
    # Parse the equation and differentiate it
    expr = sp.sympify(equation)
    expr_diff = expr.diff(x)
    
    # Calculate the slope
    slope = expr_diff.evalf(subs={x: x})
    
    # Calculate the y-intercept
    y_intercept = y - slope * x
    
    # Build the equation of the tangent line
    tangent_line = sp.Function('f')(x) - slope * x - y_intercept
    
    return tangent_line

if __name__ == "__main__":
    tangent_line = tangent_line_equation()
    print("Equation of the tangent line:", tangent_line)
