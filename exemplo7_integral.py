from sympy import integrate, cos, symbols

x = symbols('x')
integral = integrate(cos(x), x)
print(integral)
