import sympy

eq = input("Enter the right half of your equation in terms of x: y = ")
point = int(input("Enter the x value where you want the tangent line to be: "))

x = sympy.symbols('x')
eq = sympy.sympify(eq)

dx = sympy.diff(eq, x)

slope = dx.subs(x, point)

y = eq.subs(x, point)

b = y - (slope * point)

print("y = {}x + {}".format(slope, b))
