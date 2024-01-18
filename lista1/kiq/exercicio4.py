import cmath
import numpy as np

A = np.matrix([[1, -1], [1, 1]])


def eigenvalue(A):
    trA, det = np.trace(A), np.linalg.det(A)
    delta = trA**2 + 4*det
    lambda1, lambda2 = (trA - cmath.sqrt(delta))/2, (trA - cmath.sqrt(delta))/2
    return trA, det, lambda1, lambda2


eig = eigenvalue(A)


print(f'O traço é: {eig[0]} \nO determinante é: {eig[1]} \
\nO autovalor 1 é: {eig[2]} \nO autovalor 2 é: {eig[3]}')
