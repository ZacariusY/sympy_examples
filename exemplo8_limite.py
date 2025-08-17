from sympy import limit, sin, symbols

x = symbols('x')
limite = limit(sin(x)/x, x, 0)
print(limite)
