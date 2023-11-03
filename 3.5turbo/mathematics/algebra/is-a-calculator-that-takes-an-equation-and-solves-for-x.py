import sympy

def solve_equation(equation):
    x = sympy.symbols('x')
    equation = sympy.sympify(equation)
    solution = sympy.solve(equation, x)
    return solution

if __name__ == "__main__":
    equation = input("Enter an equation: ")
    solution = solve_equation(equation)
    print("Solution for x:")
    print(solution)
