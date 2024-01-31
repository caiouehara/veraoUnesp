import funcoes as mf
import math

print(""" 
###############################################################################
#Exercício 4
###############################################################################
      """)

#Função análise
def analiseFuncao(funcaoAproximada, funcaoExata, y0):
      #Aplicação do método de Euler
      tempo_vetor, solucao_vetor = mf.euler(funcaoAproximada, y0, 10**(-3), 0, 15)

      #Cálculando a solução exata
      N = len(tempo_vetor)
      sol_exata_vetor = []
      for i in range(N):
            valor = funcaoExata(tempo_vetor[i])
            sol_exata_vetor.append(valor)

      #Cálculando o erro absoluto
      erro_abs_med = mf.erro_absoluto_medio(sol_exata_vetor, solucao_vetor)

      #Printando o resultado
      print("Solução caso (a)\n")

      print("Solução no último ponto mais próxima: ", solucao_vetor[-1])
      print("Solução no último ponto exata", sol_exata_vetor[-1])
      print("Erro absoluto médio do método: ", erro_abs_med)

      print("\n")

      #Aplicação do método de Euler
      tempo_vetor1, solucao_vetor1 = mf.euler(funcaoAproximada, y0, 10**(-4), 0, 15)

      #Cálculando o erro absoluto
      erro_abs_med1 = mf.erro_absoluto_medio(sol_exata_vetor, solucao_vetor1)

      #Printando o resultado
      print("Solução caso (b)\n")

      print("Solução no último ponto aproximado: ", solucao_vetor1[-1])
      print("Solução no último ponto exata", sol_exata_vetor[-1])
      print("Erro absoluto médio do método: ", erro_abs_med1)

#Definição da Função (a)
def funcaoA(t, y):
      return 3 + t - y

def funcaoA_exata(t):
      return t - math.e**-t+2

print("Função A\n")
analiseFuncao(funcaoA, funcaoA_exata, 1)

print("""
      ###############################################################################
""")

#Definição da Função (b)
def funcaoB(t, y):
      return 2*y - 1

def funcaoB_exata(t):
      return 1/2*(math.e**2*t+1)

print("Função B\n")
analiseFuncao(funcaoB, funcaoB_exata, 1)

print("""
      ###############################################################################
""")

#Definição da Função (b)
def funcaoC(t, y):
      return 3*math.cos(t)-2*y

def funcaoC_exata(t):
      return (3/5)*(-2*math.exp(-2*t)+math.sin(t)+2*math.cos(t))

print("Função C\n")
analiseFuncao(funcaoC, funcaoC_exata, 0)
