import numpy as np

A = np.zeros((10,10), dtype="float")

for m in range(10):
    for n in range(10):
        A[m,n] = 5+3 * (m+1) * (n+1) **2

autovalores, autovetores = np.linalg.eig(A) 
det = np.linalg.det(A)

print(A)
print("\n")
print(autovalores[0])
print("\n")
print(autovetores[0])
print("\n")
print(det)