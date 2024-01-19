import cmath
import numpy as np


def input_matriz():
    M = np.zeros((2,2), dtype=complex)
    for m in range(2):
        for n in range(2):
            M[m,n] = input(f"Selecione o elemento a{m+1,n+1}: ")
    return M            


def eigenvalue(A):
    trA, det = np.trace(A), np.linalg.det(A)
    delta = trA**2 + 4*det
    lambda1, lambda2 = (trA - cmath.sqrt(delta))/2, (trA - cmath.sqrt(delta))/2
    return trA, det, lambda1, lambda2


print('poe ae a matriz')
A = input_matriz()
eig = eigenvalue(A)

print(f'O traço é: {eig[0]} \nO determinante é: {eig[1]} \
\nO autovalor 1 é: {eig[2]} \nO autovalor 2 é: {eig[3]}')
