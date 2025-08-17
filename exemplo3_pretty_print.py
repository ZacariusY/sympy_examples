from sympy import init_printing, pprint, symbols

x, y = symbols('x y')
expr = x**2 + 2*x*y + y**2

init_printing()   # ativa formatação mais elegante
pprint(expr)      # mostra expressão bonitinha
