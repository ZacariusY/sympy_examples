from sympy import solve, Eq, symbols

x = symbols('x')
equation = Eq(x**2 - 4, 0)
solutions = solve(equation, x)
print(solutions)
