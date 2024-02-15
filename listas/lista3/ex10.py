import math 
import random
import numpy as np
import sympy as sp
from pprint import pformat


a = random.random()
print(a)

M = np.zeros((10,10))

def random_real_square_matrix(size, span):
    M = sp.zeros(size,size)
    for i in range(size):
        for j in range(size):
            M[i, j] = random.randint(span[0], span[1])
    return M



size = 10
span = (-314, 314)
M = sp.Matrix(random_real_square_matrix(10, span))
M_inv = M.inv()
MM_inv = M*M_inv

print(f'''
-------------------------------------------------------------------------------
Exercício 10
-------------------------------------------------------------------------------
Matriz aleatória com coeficientes inteiros de -314 a 314: 
{pformat(M)}
{'-'*80}
Sua inversa é dada por: 
{pformat(M_inv)}
{'-'*80}
E a multiplicação M*M_inv é dada por: 
{pformat(MM_inv)}
{'-'*80}
''')


