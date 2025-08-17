from sympy import tanh, diff, symbols

x = symbols('x')
f = tanh(x)
df = diff(f, x)
print(df)
