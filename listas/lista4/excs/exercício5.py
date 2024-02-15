from sympy import *
init_printing(use_unicode=True)

print(""" 
###############################################################################
#Exercício 5
###############################################################################
      """)

#Definindo a matriz
print("A matriz Z é definda por: \n")
Z = zeros(5,5)
for m in range(0,5):
    for n in range(0, 5):
        Z[m, n] = -2*(m+1)+(n+1)**(-1)+(2/3)+4*(n)**(2)-(m+1)*(n+1)
pprint(Z)
print(Z)
print("\n")

#Cálculando a inversa da matriz
try:
    Zinv = Z.inv("LU")
    print("A matriz inversa de Z é: \n")
    pprint(Zinv)
except ValueError as error:
    print("A matriz não é invertível, porque det==0\n")

#Cálculando a matriz Z^3
Zpot3 = Z*Z*Z
#Apicando a decomposição LU do sympy
L, U, _ = Zpot3.LUdecomposition()

#Imprimindo as matrizes
print("A decomposição LU da matriz Z^3 resulta em: \n")
print("Matriz L\n")
pprint(pretty(L))
print("\n")
print("Matriz U\n")
pprint(pretty(U))
