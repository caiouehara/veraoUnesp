import numpy as np
import cmath

print(""" 
###############################################################################
#Exercício 2 
###############################################################################
      """)

#Declarando matrizes vazias 
M1 = np.zeros((2,2), dtype=float) 
M2 = np.zeros((3,3), dtype=float)
M3 = np.zeros((2,2), dtype=complex)

#Definindo todas as matrizes do exercício
for m in range(0, 3):
    for n in range(0, 3):
        i , j = m + 1, n + 1 #mudança de variável 
        M2[m,n] = 2*i- 3*j
        if m < 2 and n < 2:
            M1[m,n] = (i+2)**j
            M3[m,n] = complex(i,j)

#retornando o determinante e traço das matrizes
def estudo_matrix(M):
    det_M = np.linalg.det(M)
    trace_M = np.trace(M)
    print("matriz: \n", M)
    print("determinante: \n ", det_M) 
    print("traço: \n", trace_M) 
    print("-"*79)
    return M, np.linalg.det(M), np.trace(M)

#Estudando as matrizes
E1, E2, E3 = estudo_matrix(M1), estudo_matrix(M2), estudo_matrix(M3), 


print(""" 
###############################################################################
#Exercício 4
###############################################################################
      """)

#Lendo a matriz input do usuário, elemento a elemento
def input_matriz():
    M = np.zeros((2,2), dtype=complex)
    for m in range(2):
        for n in range(2):
            M[m,n] = input(f"Selecione o elemento a{m+1,n+1}: ")
    return M            


#Cálculando o traço, determinante e, com a fórmula, os autovalores
def eigenvalue(A):
    trA, det = np.trace(A), np.linalg.det(A)
    delta = trA**2 + 4*det
    lambda1, lambda2 = (trA - cmath.sqrt(delta))/2, (trA - cmath.sqrt(delta))/2
    return trA, det, lambda1, lambda2

#Chamando as funções 
A = input_matriz()
eig = eigenvalue(A)

#Imprimindo o resultado
print(f'O traço é: {eig[0]} \nO determinante é: {eig[1]} \
\nO autovalor 1 é: {eig[2]} \nO autovalor 2 é: {eig[3]}')


print(""" 
###############################################################################
#Exercício 6
###############################################################################
      """)

#Definindo o estudo da PG
def estudo_pg(a1, q, n):
    approx_sum = 0

    for n in range(1, n+1):
        an = a1*(q**(n-1))
        approx_sum += an

    real_sum = a1/(1 - q)
    abs_error = abs(real_sum - approx_sum)
    return approx_sum, real_sum, abs_error

#Imprimindo o resultado
def print_estudo_pg(a1, q, N):
    for n in N:
        pg = estudo_pg(a1, q, n)
        print(f'O erro absoluto da pg com valor inicial {a1}, razao {q} \
                \n n = {n} é {pg[2]} \n')


#Declarando a PG e imprimindo o resultado
a1, q, N = 10, 1/2, [50, 250, 1000]
print_estudo_pg(a1, q, N)


print(""" 
###############################################################################
#Exercício 7
###############################################################################
      """)


#Análise do erro da PG
def pg_error_analysis(a1, q, error):
    n = 0

    while True:
        *_, abs_error = estudo_pg(a1, q, n)
        max_precision = np.finfo(np.float64).eps

        if abs_error < max_precision:
            print(f'precisão da máquina atingida {max_precision}')
            return n

        elif abs_error <= error:
            return n

        n += 1




#Declarando a PG e imprimindo o resultado
a1, q, error = 3, (1/4), [10**(-2), 10**(-5), 10**(-10)] 
for E in error:
    n = pg_error_analysis(a1, q, E)
    print(f'n = {n}')

