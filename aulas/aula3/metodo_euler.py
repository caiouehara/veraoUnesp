import numpy as np
import math

# Do que precisamos para usarmos o método de Euler?
# 1. A expressão da função f(y' = f(t,y))
# 2. Ponto inicial (Condição inicial) (y0)
# 3. O passo h
# 4. O intervalo onde se busca a solução [a, b]

#O que queremos obter?
#A solução aproximada
#O tempo discretizado
def euler(f, y0, h, a, b):
    # Passo 0 :: Iniciar os vetores que vão receber os valores de t e de y
    t_vetor = [a]
    y_vetor = [y0]
    
    #Passo 1 :: Encontrar o número N de vezes que o passo repetirá o método de Euler
    N = int( (b - a)/h )
    
    #Passo 2 :: Repetir N vezes o método de Euler
    #t_(n+1) = t_n + h
    # y_(n+1) = y_n + h*f(t_n, x_n)
    
    for m in range(N):
        t_discreto = t_vetor[m] + h
        y_discreto = y_vetor[m] + h * f(t_vetor[m], y_vetor[m])
        
        t_vetor.append(t_discreto)
        y_vetor.append(y_discreto)
        
    return t_vetor[-1], y_vetor[-1]

#Exemplo 01: PVI :: y' = y com y(0) = 1. Resolver no intervalo [0, 0.6]
def exemplo1(t, y): 
    #Coloque aqui o segundo membro da equação diferencial
    # y' = y (y' = f(t,y))
    return y

tempo, solucao_numerica = euler(exemplo1, 1, 10**(-3), 0, 0.6)

print(tempo, solucao_numerica)

valor_exato = math.exp(0.6)
erro = abs(solucao_numerica - valor_exato)

print(erro)