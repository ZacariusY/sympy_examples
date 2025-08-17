from sympy import Matrix

M = Matrix([[1, 2], [2, 3]])
print("Matriz:")
print(M)

print("Determinante:", M.det())
print("Inversa:")
print(M.inv())
print("Autovalores:", M.eigenvals())
