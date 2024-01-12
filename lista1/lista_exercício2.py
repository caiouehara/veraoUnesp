import numpy as np

#Exercíco 2

#Declarando as matrizez
M1 = np.zeros((2,2), dtype=float)
M2 = np.zeros((3,3), dtype=float)
M3 = np.zeros((2,2), dtype=complex)

#Definindo os elementos das matrizes pelo termo geral
for m in range(0, 3):
    for n in range(0, 3):
        # Declarando a(i,j) = b(m+1, n+1)
        i = m + 1
        j = n + 1
        
        M2[m,n] = 2*n - 3*m
        
        if m < 2 and n < 2:
            M1[m,n] = (i+2)**j
            M3[m,n] = complex(i,j)

def estudo_matriz(A):
    det = np.linalg.det(A)
    trace = np.trace(A)
    print(A, "Determinante" + str(det),"Traço " + str(trace), "\n")
    
estudo_matriz(M1)
estudo_matriz(M2)
estudo_matriz(M3)