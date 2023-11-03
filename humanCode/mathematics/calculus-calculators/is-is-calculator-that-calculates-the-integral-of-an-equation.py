import sympy

eq = input("Enter the right half of your equation in terms of x: f'(x) = ")
x = sympy.symbols('x')
eq = sympy.sympify(eq)

integral = sympy.integrate(eq, x)

sympy.init_printing()

print("f(x) = ")
sympy.pprint(integral, use_unicode=False)
