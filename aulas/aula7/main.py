#Importando TODAS as letras (variáveis) que pretende usar
from sympy.abc import x, y, Z
#Importando métodos do sympy
from sympy import expand, factor, diff, integrate, limit, Matrix
#Importando funções matemáticas
from sympy import sin, exp, tan, cos, oo

#Derivação Simbólica
funcao = sin(x)*exp(x)
derivada = diff(funcao, x)
print(derivada)

#Derivacao Simbolica
funcao = ((cos(3*x))*tan(x))/x**2
derivada = diff(funcao, x)
print(derivada)