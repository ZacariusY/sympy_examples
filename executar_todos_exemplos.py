#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para executar todos os exemplos SymPy
"""

print("=" * 60)
print("EXECUTANDO TODOS OS EXEMPLOS SYMPY")
print("=" * 60)

print("\n" + "=" * 50)
print("EXEMPLO 1: Comparação Math vs SymPy (Raiz Quadrada)")
print("=" * 50)
import math
from sympy import sqrt
print(f"math.sqrt(10) = {math.sqrt(10)}")
print(f"sympy.sqrt(10) = {sqrt(10)}")

print("\n" + "=" * 50)
print("EXEMPLO 2: Definição de Símbolos")
print("=" * 50)
from sympy import symbols
x, y = symbols('x y')
expr = x**2 + 2*x*y + y**2
print(f"Expressão: {expr}")

print("\n" + "=" * 50)
print("EXEMPLO 3: Pretty Print (Formatação Elegante)")
print("=" * 50)
from sympy import init_printing, pprint
init_printing()
print("Expressão formatada:")
pprint(expr)

print("\n" + "=" * 50)
print("EXEMPLO 4: Resolução de Equações (solve + Eq)")
print("=" * 50)
from sympy import solve, Eq
equation = Eq(x**2 - 4, 0)
solutions = solve(equation, x)
print(f"Equação: {equation}")
print(f"Soluções: {solutions}")

print("\n" + "=" * 50)
print("EXEMPLO 5: Resolução com SolveSet")
print("=" * 50)
from sympy import solveset, S
equation2 = x**2 - 4
solutions2 = solveset(equation2, x, domain=S.Reals)
print(f"Equação: {equation2} = 0")
print(f"Soluções (conjunto): {solutions2}")

print("\n" + "=" * 50)
print("EXEMPLO 6: Cálculo de Derivadas")
print("=" * 50)
from sympy import diff, sin
derivada = diff(sin(x), x)
print(f"f(x) = sin(x)")
print(f"f'(x) = {derivada}")

print("\n" + "=" * 50)
print("EXEMPLO 7: Cálculo de Integrais")
print("=" * 50)
from sympy import integrate, cos
integral = integrate(cos(x), x)
print(f"∫ cos(x) dx = {integral}")

print("\n" + "=" * 50)
print("EXEMPLO 8: Cálculo de Limites")
print("=" * 50)
from sympy import limit
limite = limit(sin(x)/x, x, 0)
print(f"lim(x→0) sin(x)/x = {limite}")

print("\n" + "=" * 50)
print("EXEMPLO 9: Operações com Matrizes")
print("=" * 50)
from sympy import Matrix
M = Matrix([[1, 2], [2, 3]])
print(f"Matriz M:")
print(M)
print(f"\nDeterminante: {M.det()}")
print(f"Matriz Inversa:")
print(M.inv())
print(f"Autovalores: {M.eigenvals()}")

print("\n" + "=" * 50)
print("EXEMPLO 10: Derivada da Tangente Hiperbólica")
print("=" * 50)
from sympy import tanh
f = tanh(x)
df = diff(f, x)
print(f"f(x) = tanh(x)")
print(f"f'(x) = {df}")

print("\n" + "=" * 60)
print("TODOS OS EXEMPLOS EXECUTADOS COM SUCESSO!")
print("=" * 60) 