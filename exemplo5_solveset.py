from sympy import solveset, S, symbols

x = symbols('x')
equation = x**2 - 4
solutions = solveset(equation, x, domain=S.Reals)
print(solutions)
