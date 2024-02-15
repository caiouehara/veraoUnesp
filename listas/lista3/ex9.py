import sympy as sp

x, y, z = sp.symbols('x, y, z')

f = sp.cos(x * sp.sin(x/y))+ z**2


point = {x: sp.pi, y: 2, z: sp.Rational(-4, 7)}
f_point = f.subs(point)
f_value = sp.N(f_point)

print(f'''
-------------------------------------------------------------------------------
Exercício 9
-------------------------------------------------------------------------------

Seja f dada por: {f}
Temos que f aplicada em {tuple(point.values())} é igual a {f_point}
Aproximando numericamente este valor, nós temos {f_value}
''')


