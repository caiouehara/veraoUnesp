#Definindo funções auxiliares para uso durante o curso

import numpy as np
import scipy as sc
import sympy as sym
import math

def bhaskara(a,b,c):
    delta = float(b) **2 - 4* float(a) *float(c)
    raiz1 = float( (-b + math.root(delta))/a )
    raiz2 = float ( (-b - math.root(delta))/a ) 
    return raiz1, raiz2

def estudo_matriz(A):
    traco = np.trace(A)
    det = np.linalg.det(A)
    autovalor, autovetor = np.linalg.eig(A)
    return traco, det, autovalor, autovetor

def soma_pa(a1, r, n):
    an = a1
    for i in range(n-1):
        an += float(r)
    soma = (a1+an)*n/2
    return soma 

def maior(a, b):
    if abs(a) > abs(b):
        return a
    else:
        return b
    
def maior_autovalor(A):
    autovalor, _ = np.linalg.eig(A)
    
def soma_inf_pg(a1, q):
    #convergente
    if q < 1 and q > 0:
        soma = float(a1)/(1-float(q))
        return soma
    else:
        print("Progressão geométrica divergente")