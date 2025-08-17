from sympy import diff, sin, symbols

x = symbols('x')
derivada = diff(sin(x), x)
print(derivada)
