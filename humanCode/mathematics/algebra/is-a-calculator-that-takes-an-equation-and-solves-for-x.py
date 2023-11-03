import sympy
from sympy.solvers import solve

expression = input("Enter the equation to solve for x. Assume that the expression = 0: ")

x = sympy.Symbol('x')

print(solve(sympy.parsing.sympy_parser.parse_expr(expression), x))
