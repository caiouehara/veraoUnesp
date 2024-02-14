from sympy import *
init_printing(use_unicode=True)

print(""" 
###############################################################################
#Exercício 4
###############################################################################
      """)

#Definindo a matriz
M = Matrix([[2, -5, 0], [0, 7, 5], [-1, 2, 4]])
N = Matrix([[3, -2, 1], [2, 3, -8], [2, 3, 5]])
O = Matrix([[4, 3, 1], [-3, 4, 6], [1, 1, 1]])

#Imprimindo as matrizes
def analisandoMatrizInversa(Matriz, nome):
    #Cálculando a inversa da matriz 
    MatrizInversa = Matriz.inv("LU")
    
    print(f"A inversa da matriz {nome} é: \n")
    pprint(MatrizInversa)
    print("\n")
    
    return MatrizInversa

print("\n-------------- As matrizes inversas (a) -------------\n")
analisandoMatrizInversa(M, "M")
analisandoMatrizInversa(N, "N")
analisandoMatrizInversa(O, "O")

#Cálculando a expressão (M*Mt + (N*O)t)
print("\n-------------- O cálculo da expressão (b) -------------\n")
print("A expressão cálculada é: \n")
resultado = M * Transpose(M) + Transpose((N*O))
pprint(resultado)

#Encontrando os autovalores de M*N
print("\n-------------- O cálculo dos autovalores (c) -------------\n")
eigenvalues, _, _ = (M*N).eigenvects()
print(eigenvalues)

#Encontrando a inversa da expressão:
# M*O + O*N + N*M + M^2 - 3*N^4
print("\n-------------- O cálculo da inversa da expressão (d) -------------\n")
resultado2 = (M*O+O*N+N*M+(M**2-3*N**4)).inv("LU")
pprint(resultado2)