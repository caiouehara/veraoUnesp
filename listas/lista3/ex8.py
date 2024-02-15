from sympy import symbols, Function, Eq, dsolve, lambdify
from sympy.plotting import plot


t = symbols('t')
y = Function('y')(t)

eq = (t - 2)**2 * y.diff(t, t) + t * y + (t + 3) * y
ics = {y.subs(t, 1): 2, y.diff(t).subs(t, 1): 1}
solution = dsolve(Eq(eq, 0), y, ics=ics)


print('''
-------------------------------------------------------------------------------
Exercício 11
-------------------------------------------------------------------------------
''')
print("A solução exata é dada por")
print(solution)
print('-'*80)
print('''Como o problema é stiff para t>2, apareceram dificuldades na hora de resolver
o problema numericamente, o melhor que conseguimos fazer foi usar métodos prontos
para plotar a solução com acurácia entre para t < 2''')
plot(solution.rhs, (t, 0, 2))
