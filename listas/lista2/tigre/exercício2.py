import funcoes as mf
import math
from matplotlib import pyplot as plt

print(""" 
###############################################################################
#Exercício 2
###############################################################################
      """)

print(""" 
------------------------------------------------------------------------------
#Exercício 2 (a)
------------------------------------------------------------------------------
      """)

def funcao(t, y):
    return 2*t*math.e**(2*t)+y

print("Solução caso (a)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 1, 10**(-1), 0, 15)

print("\nSolução caso (b)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 1, 10**(-2), 0, 15)

print("\nSolução caso (c)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 1, 10**(-4), 0, 15)

print(""" 
------------------------------------------------------------------------------
#Exercício 2 (b)
------------------------------------------------------------------------------
      """)

def funcao2(t, y):
    return 4+2*y-t

print("Solução caso (a)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao2, 2, 10**(-1), 0, 15)

print("\nSolução caso (b)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao2, 2, 10**(-2), 0, 15)