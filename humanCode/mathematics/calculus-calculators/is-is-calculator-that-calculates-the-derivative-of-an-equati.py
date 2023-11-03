import sympy

eq = input("Enter the right half of your equation in terms of x: f'(x) = ")
x = sympy.symbols('x')
eq = sympy.sympify(eq)

derivative = sympy.diff(eq, x)

sympy.init_printing()

print("f'(x) = ")
sympy.pprint(derivative, use_unicode=False)
