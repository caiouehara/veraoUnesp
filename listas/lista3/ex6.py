import sympy as sp


x = sp.symbols('x')


f = 1/x
f_diff = f.diff(x)
interval = (x, 1, sp.oo)
V = sp.pi*sp.integrate(f**2,interval)
A = 2*sp.pi*sp.integrate((f)*sp.sqrt(1 - f_diff**2),interval)

print(f'''
-------------------------------------------------------------------------------
Exercício 6
-------------------------------------------------------------------------------

O volume da Trombeta de Gabriel é dado por
V = {V}.

{'-'*80}

E sua área é dada por 
A = {A}

{'-'*80}
''')


