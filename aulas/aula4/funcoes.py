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
    t_vetor = [float(a)]
    y_vetor = [float(y0)]
    
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
        
    return t_vetor, y_vetor

#Erro Absoluto
#Entradas: sol_exata e sol_numerica
def erro_absoluto(sol_exata, sol_numerica):
    N = len(sol_exata)
    erro_abs = 0
    for i in range(N):
        erro_abs = erro_abs + abs(sol_exata[i] - sol_numerica[i])
    return erro_abs

#Erro Absoluto Médio
#Entradas: sol_exata e sol_numerica
def erro_absoluto_medio(sol_exata, sol_numerica):
    N = len(sol_exata)
    erro_abs = 0
    for i in range(N):
        erro_abs = erro_abs + abs(sol_exata[i] - sol_numerica[i])
    return erro_abs

#Erro Quadrático 
#Entradas: sol_exata e sol_numerica
def erro_quadratico(sol_exata, sol_numerica):
    N = len(sol_exata)
    erro_quadratico = 0
    for i in range(N):
        erro_quadratico = erro_quadratico + abs(sol_exata[i] - sol_numerica[i])**2
    return erro_quadratico

#Erro Quadrático Médio
#Entradas: sol_exata e sol_numerica
def erro_quadratico_medio(sol_exata, sol_numerica):
    N = len(sol_exata)
    erro_quadratico = 0
    for i in range(N):
        erro_quadratico = erro_quadratico + abs(sol_exata[i] - sol_numerica[i])**2
    erro_medio = erro_quadratico/N
    return erro_medio

# Do que precisamos para usarmos o método de Runge-Kutta?
# 1. A expressão da função f(y' = f(t,y))
# 2. Ponto inicial (Condição inicial) (y0)
# 3. O passo h
# 4. O intervalo onde se busca a solução [a, b]

# 1- Iniciar os vetores t e y
# 2- Encontrar o numero de pontos discretos de [a, b]
# 3- Calcular os Ks
# 4- Aplicar o método

#Implementação do RK de quarta ordem
#Entradas: y' = f(t, y),
#          intervalo numério [a,b], 
#          ponto de pardida (y0)
#          O passo h

def runge_kutta4(f, y0, h, a, b):
    #Passo 0: Iniciar os vetores t_vetor, y_vetor
    t_vetor = [a]
    y_vetor = [y0]
    
    ##Passo 1: Cálcular o número N de repetições
    N = int((b-a)/h)
    
    ##Passo 2: Cálcular K (depende de k1,k2,k3,k4)
    for m in range(N):
        t_discreto = t_vetor[m] + h
        k1 = f(t_vetor[m], y_vetor[m])
        k2 = f(t_vetor[m] + h/2, y_vetor[m] + h/2*k1)
        k3 = f(t_vetor[m] + h/2, y_vetor[m] + h/2*k2)
        k4 = f(t_vetor[m] +h, y_vetor[m] + h*k3)
        
        k = (k1 + 2*k2 + 2*k3 + k4)/6
        
        #Método de Passo Único :: y_(n+1) = y_n + h*k
        y_discreto = y_vetor[m] + h*k
        
        y_vetor.append(y_discreto)
        t_vetor.append(t_discreto)
    return t_vetor, y_vetor