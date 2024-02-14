from sympy import *
init_printing(use_unicode=True)

print(""" 
###############################################################################
#Exercício 3
###############################################################################
      """)

#Definindo a matriz
A = Matrix([[2, -5], [0, 7]])

#Apicando a decomposição LU do sympy
L, U, _ = A.LUdecomposition()

#Imprimindo as matrizes
print("A decomposição LU da matriz resulta em: \n")
print("Matriz L\n")
pprint(pretty(L))
print(L)
print("\n")
print("Matriz U\n")
pprint(pretty(U))
print(U)