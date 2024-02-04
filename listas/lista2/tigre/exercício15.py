import funcoes as mf
import math
from matplotlib import pyplot as plt
import numpy as np

#Caminho para a pasta de resultados
path = "./listas/lista2/tigre/results/exercicio15/"

print(""" 
###############################################################################
#Exercício 15
###############################################################################
      """)
      
#Função análise
def analiseFuncao(condicao_inicial, f, g, h, a, b):
      #Aplicação do método de Runge Kutta 4x4
      t, x_vec, y_vec = mf.rk4_sistemas_2por2(
            f, g, condicao_inicial, a, b, h
      )
      
      #Salvando arquivo
      atrator = np.zeros((len(t), 2), dtype=float)
      for i in range(len(t)):
            atrator[:, 0] = x_vec[i]
            atrator[:, 1] = y_vec[i]
      np.savetxt(path + f'resultado_exemplo15.txt', atrator)

      return atrator


#Definição das funções
def x_f(t, x, y):
      return y

mu = 0.02
def y_f(t, x, y):
      return mu*(1-x**(2))*y-x

#Aplicando a análise
condicao_inicial = (1, 1) #Solução inicial?
h = 5*10**(-3)
atrator = analiseFuncao(condicao_inicial, x_f, y_f, h, 25, 100)