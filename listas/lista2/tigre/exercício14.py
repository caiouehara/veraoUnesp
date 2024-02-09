import funcoes as mf
from matplotlib import pyplot as plt
import numpy as np

#Caminho para a pasta de resultados
path = "./listas/lista2/tigre/results/exercicio14/"

print(""" 
###############################################################################
#Exercício 14
###############################################################################
      """)
      
#Função análise
def analiseFuncao(condicao_inicial, f, g, p, s, h, a, b):
      #Aplicação do método de Runge Kutta 4x4
      t, x_vec, y_vec, z_vec, w_vec = mf.rk4_sistemas_4por4(
            f, g, p, s, condicao_inicial, a, b, h
      )
      
      #Salvando o resultado em arquivo
      matrix = np.zeros((len(t), 5), dtype=float)
      for i in range(len(t)):
            matrix[i, 0] = t[i]
            matrix[i, 1] = x_vec[i]
            matrix[i, 2] = y_vec[i]
            matrix[i, 3] = z_vec[i]
            matrix[i, 4] = w_vec[i]
      np.savetxt(path + f'resultado_exemplo14.txt', matrix)
      
      return t, x_vec, y_vec, z_vec, w_vec
      
#Definição das funções
def x_f(t, x, y, z, w):
      return 0.375*x+y+0.4*(z+1.7)

def y_f(t, x, y, z, w):
      return -x

def z_f(t, x, y, z, w):
      return (0.001)**(-1)*(w-z**(3))+3*z**(2)-x-0.15

def w_f(t, x, y, z, w):
      return (0.002)**(-1)*(1-5*z**(2)-w)

#Aplicando a análise
condicao_inicial = (0.2, 0.2, 0.2, 1.66)
h = 5*10**(-5)
t, x_vec, y_vec, z_vec, w_vec = analiseFuncao(condicao_inicial, x_f, y_f, z_f, w_f, h, 0, 50)

#Gráfico
plt.figure()
plt.plot(t, w_vec, color = "red")
plt.xlabel("Tempo (t)")
plt.ylabel("Resultado via Runge Kutta 4")
plt.show()
