from exercicio6 import *


def pg_error_analysis(a1, q, error):
    n = 0

    while True:
        *_, abs_error = estudo_pg(a1, q, n)
        max_precision = np.finfo(np.float64).eps
        if abs_error < max_precision:
            print(f'precisão da máquina atingida {max_precision}')
            return n
        elif abs_error <= error:
            return n

        n += 1


error = [10**(-2), 10**(-5), 10**(-10)]

for E in error:
    n = pg_error_analysis(a1, q, E)
    print(f'n = {n}')
