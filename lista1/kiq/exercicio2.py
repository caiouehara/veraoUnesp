import numpy as np

#Declarando as matrizes
M1 = np.zeros((2,2), dtype=float) 
M2 = np.zeros((3,3), dtype=float)
M3 = np.zeros((2,2), dtype=complex)

#Definindo as matrizes
for m in range(0, 3):
    for n in range(0, 3):
        i , j = m + 1, n + 1 #mudança de variável 
        M2[m,n] = 2*i- 3*j
        if m < 2 and n < 2:
            M1[m,n] = (i+2)**j
            M3[m,n] = complex(i,j)


def estudo_matrix(M):
    det_M = np.linalg.det(M)
    trace_M = np.trace(M)
    print("matriz: \n", M)
    print("determinante: \n ", det_M) 
    print("traço: \n", trace_M) 
    print("-"*79)
    return M, np.linalg.det(M), np.trace(M)


E1, E2, E3 = estudo_matrix(M1), estudo_matrix(M2), estudo_matrix(M3), 

