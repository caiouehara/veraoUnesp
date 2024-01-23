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

def rk4_passo(f, g, t, x, y, h):
    #PVI :: x' = f(t, x, y) e y' = g(t, x, y)
    #f e g são duas funções que definem o sistema
    #t é o tempo do instante anterior
    #x, y são as soluções no instante do tempo anterior
    #h é o tempo de integração
    
    k1_f = f(t, x, y)
    k1_g = g(t, x, y)
    
    k2_f = f(t+h/2, x+h/2*k1_f, y+h/2*k1_f)
    k2_g = g(t+h/2, x+h/2*k1_f, y+h/2*k1_g)
    
    k3_f = f(t+h/2, x+h/2*k1_f, y+h/2*k2_f)
    k3_g = g(t+h/2, x+h/2*k1_f, y+h/2*k2_g)
    
    k4_f = f(t+h, x+h*k3_f, y+h*k3_f)
    k4_g = g(t+h, x+h*k3_f, y+h*k3_g)
    
    x_novo = x+h*(k1_f+2*k2_f+2*k3_f+k4_f)/6
    y_novo = y+h*(k1_g+2*k2_g+2*k3_g+k4_g)/6
    
    return x_novo, y_novo
    

def rk4_sistemas2por2(f, g, condicao_inicial, a, b, h):
    # f e g são as duas funcoes que definem o sistema
    # condical inicial (x0, y0) para t = a
    # intervalo de integracao [a, b]
    # passo de integracao h
    
    #Passo 0: Iniciar o vetor de tempo e os vetores para x e y
    t_vetor = [a]
    x0, y0 = condicao_inicial
    x_vetor = [x0]
    y_vetor = [y0]
    
    #Passo 1:: Calcular N (número de repeticões)
    N = int((b-a)/h)
    
    #Passo 2 :: Executar N vezes i rk4_passo
    for i in range(N):
        t_novo = t_vetor[i] + h
        x_novo, y_novo = rk4_passo(f, g, t_vetor[i], x_vetor[i], y_vetor[i], h)
        
        t_vetor.append(t_novo)
        x_vetor.append(x_novo)
        y_vetor.append(y_novo)
        
        return t_vetor, x_vetor, y_vetor
    
def descarte_transiente(serie_numerica, porcentagem):
    N = len(serie_numerica)
    ponto_inicial = int(np.floor(N*porcentagem/100))
    serie_recortada = serie_numerica[ponto_inicial::]
    return serie_recortada
    