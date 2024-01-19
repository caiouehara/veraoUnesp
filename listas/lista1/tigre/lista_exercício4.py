import numpy as np
import cmath

#Exercício 4

#Leitura da matriz (a)
def input_matriz():
    M = np.zeros((2,2), dtype=complex)
    for m in range(2):
        for n in range(2):
            M[m,n] = input(f"Selecione o elemento a{m+1,n+1}: ")
    return M            

A = input_matriz()

#Computação do autovalor
def eigenvalue(A):
    tr, det = np.trace(A), np.linalg.det(A)
    delta = tr**2 - 4*det
    lambda1 =(tr + cmath.sqrt(delta))/2
    lambda2 =(tr - cmath.sqrt(delta))/2
    print("Autovalor (1): ", lambda1)
    print("Autovalor (2): ", lambda2)
    
eigenvalue(A)