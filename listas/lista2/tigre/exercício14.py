import funcoes as mf
import math
from matplotlib import pyplot as plt
import numpy as np

#Caminho para a pasta de resultados
path = "./listas/lista2/tigre/results/exercicio15/"

print(""" 
###############################################################################
#Exercício 14
###############################################################################
      """)
      
#Função análise
def analiseFuncao(condicao_inicial, f, g, p, s, h, a, b):
      #Aplicação do método de Runge Kutta 4x4
      x0, y0, z0, w0 = condicao_inicial
      t, x_vec, y_vec, z_vec, w_vec = mf.rk4_sistemas_4por4(
            f, g, p, s, condicao_inicial, a, b, h
      )
      
      #Salvando arquivo
      atrator = np.zeros((len(t), 2), dtype=float)
      for i in range(len(t)):
            atrator[:, 0] = x_vec
            atrator[:, 1] = y_vec
      np.savetxt(path + f'resultado_exemplo15.txt', atrator)

      return atrator
      
#Definição das funções
def x_f(t, x, y, z, w):
      return 0.375*x+y+0.4*(z+1.7)

def y_f(t, x, y, z, w):
      return -x

def z_f(t, x, y, z, w):
      return (0.001)**(-1)*(w-z**(3)+3*z**(2)-x-0.15)

def w_f(t, x, y, z, w):
      return (0.002)**(-1)*(1-5*z**(2)-w)

#Aplicando a análise
condicao_inicial = (0.2, 0.2, 0.2, 1.66)
h = 5*10**(-5)
atrator = analiseFuncao(condicao_inicial, x_f, y_f, z_f, w_f, h, 0, 50)

#Plotagem
