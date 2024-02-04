import funcoes as mf
import math
import numpy as np

#Caminho para a pasta de resultados
path = "./listas/lista2/tigre/results/exercicio9/"

print(""" 
###############################################################################
#Exercício 9
###############################################################################
      """)

#Função análise
def analiseFuncao(funcaoAproximada, funcaoExata, y0, h, a, b, nome):
      #Aplicação do método
      tempo_vetor, solucao_vetor = mf.runge_kutta4(funcaoAproximada, y0, h, a, b)

      #Cálculando a solução exata
      N = len(tempo_vetor)
      sol_exata_vetor = []
      for i in range(N):
            valor = funcaoExata(tempo_vetor[i])
            sol_exata_vetor.append(valor)

      #Cálculando o erro absoluto
      erro_quad = mf.erro_quadratico(sol_exata_vetor, solucao_vetor)

      #Printando o resultado
      print("\nSolução\n")

      print("Solução no último ponto mais próxima: ", solucao_vetor[-1])
      print("Solução no último ponto exata", sol_exata_vetor[-1])
      print("Erro quadrádico: ", erro_quad)
      
      #Salvando o resultado em arquivo
      matrix = np.zeros((len(tempo_vetor), 2), dtype=float)
      for i in range(len(tempo_vetor)):
            matrix[i, 0] = tempo_vetor[i]
            matrix[i, 1] = solucao_vetor[i]
      np.savetxt(path + f'resultado_exemplo09_{nome}.txt', matrix)
      
#Definição da Função
def funcaoA(t, y):
      return t*math.exp(3*t)-2*y

def funcaoA_exata(t):
      return (1/5)*t*math.exp(3*t)-(1/25)*math.exp(3*t)+(1/25)*math.exp(-2*t)

analiseFuncao(funcaoA, funcaoA_exata, 0, 10**(-4), 0, 1, "Função A")

def funcaoB(t, y):
      return 1 + (t-y)**2

def funcaoB_exata(t):
      return t + 1/(1-t)

analiseFuncao(funcaoB, funcaoB_exata, 1, 10**(-4), 2, 3, "Função B")

def funcaoC(t, y):
      return 1 + y/t

def funcaoC_exata(t):
      return t*math.log(t)+2*t

analiseFuncao(funcaoC, funcaoC_exata, 2, 10**(-4), 1, 2, "Função C")

def funcaoD(t, y):
      return math.cos(2*t) + math.sin(3*t)

def funcaoD_exata(t):
      return 1/2*math.sin(2*t)-(1/3)*math.cos(3*t)+(4/3)

analiseFuncao(funcaoD, funcaoD_exata, 1, 10**(-4), 0, 1, "Função D")

