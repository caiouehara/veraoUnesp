import funcoes as mf
import math

print(""" 
###############################################################################
#Exercício 14
###############################################################################
      """)
      
#Função análise
def analiseFuncao(funcaoAproximada, funcaoExata, y0, h, a, b, methodName):
      #Aplicação do método de Euler
      tempo_vetor, solucao_vetor = mf.methods[methodName](funcaoAproximada, y0, h, a, b)

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

      print("Solução do t = 30 (aproximada): ", solucao_vetor[30-1])
      print("Solução do t = 30 (exata)", sol_exata_vetor[30-1])
      print("Erro quadrádico: ", erro_quad)
      
      return erro_quad
      
#Definição das funções
m = 100000
k = 2*10**-6
def funcao(t, y):
      return k*(m-y)*y

def funcaoExata(t):
      return (100000*math.exp(t/5))/(math.exp(t/5)+99)

print("Aplicação do Runge Kutta 4 \n")
analiseFuncao(funcao, funcaoExata, 1000, 5*10**(-4), 0, 90, "runge_kutta_4")