import funcoes as mf
import math
import time
import numpy as np

#Caminho para a pasta de resultados
path = "./listas/lista2/tigre/results/exercicio10/"

print(""" 
###############################################################################
#Exercício 10
###############################################################################
      """)
      
#Função análise
def analiseFuncao(funcaoAproximada, funcaoExata, y0, h, a, b, methodName, nome):
      #Aplicação do método
      tempo_vetor, solucao_vetor = mf.methods[methodName](funcaoAproximada, y0, h, a, b)

      #Cálculando a solução exata
      N = len(tempo_vetor)
      sol_exata_vetor = []
      for i in range(N):
            valor = funcaoExata(tempo_vetor[i])
            sol_exata_vetor.append(valor)

      #Cálculando o erro absoluto
      start_time = time.time() #Medindo desempenho
      erro_quad = mf.erro_quadratico(sol_exata_vetor, solucao_vetor)
      end_time = time.time()
      elapsed_time = end_time - start_time
      
      #Printando o resultado
      print("\nSolução\n")

      print("Solução no último ponto mais próxima: ", solucao_vetor[-1])
      print("Solução no último ponto exata", sol_exata_vetor[-1])
      print("Erro quadrádico: ", erro_quad)
      print("Tempo de execução para cálculo do erro quadrático: ", elapsed_time)
      
      #Salvando o resultado em arquivo
      matrix = np.zeros((len(tempo_vetor), 2), dtype=float)
      for i in range(len(tempo_vetor)):
            matrix[i, 0] = tempo_vetor[i]
            matrix[i, 1] = solucao_vetor[i]
      np.savetxt(path + f'resultado_exemplo10_{nome}.txt', matrix)
      
      return erro_quad
      
#Definição das funções
def funcaoA(t, y):
      return t*math.exp(3*t)-2*y

def funcaoA_exata(t):
      return (1/5)*t*math.exp(3*t)-(1/25)*math.exp(3*t)+(1/25)*math.exp(-2*t)


def funcaoB(t, y):
      return 1 + (t-y)**2

def funcaoB_exata(t):
      return t + 1/(1-t)

def funcaoC(t, y):
      return 1 + y/t

def funcaoC_exata(t):
      return t*math.log(t)+2*t


def funcaoD(t, y):
      return math.cos(2*t) + math.sin(3*t)

def funcaoD_exata(t):
      return 1/2*math.sin(2*t)-(1/3)*math.cos(3*t)+(4/3)

resultado_RK = list()
resultado_euler = list()

print("Aplicação do Runge Kutta 4 \n")
resultado_RK.append(analiseFuncao(funcaoA, funcaoA_exata, 0, 10**(-4), 0, 1, "runge_kutta_4", "FunçãoA"))
resultado_RK.append(analiseFuncao(funcaoB, funcaoB_exata, 1, 10**(-4), 2, 3, "runge_kutta_4", "FunçãoB"))
resultado_RK.append(analiseFuncao(funcaoC, funcaoC_exata, 2, 10**(-4), 1, 2, "runge_kutta_4", "FunçãoC"))
resultado_RK.append(analiseFuncao(funcaoD, funcaoD_exata, 1, 10**(-4), 0, 1, "runge_kutta_4", "FunçãoD"))
      
print("Aplicação do Euler \n")
resultado_euler.append(analiseFuncao(funcaoA, funcaoA_exata, 0, 10**(-4), 0, 1, "euler", "FunçãoA"))
resultado_euler.append(analiseFuncao(funcaoB, funcaoB_exata, 1, 10**(-4), 2, 3, "euler", "FunçãoB"))
resultado_euler.append(analiseFuncao(funcaoC, funcaoC_exata, 2, 10**(-4), 1, 2, "euler", "FunçãoC"))
resultado_euler.append(analiseFuncao(funcaoD, funcaoD_exata, 1, 10**(-4), 0, 1, "euler", "FunçãoD"))

print("\n Comparação do resultado: ")
for i in range(4):
      print("Comparando resultado do método de Euler e Runge Kutta 4: ", abs(resultado_RK[i] - resultado_euler[i]))