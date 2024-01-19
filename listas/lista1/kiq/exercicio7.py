import numpy as np

# Função do exercício 6
def estudo_pg(a1, q, n):
    approx_sum = 0

    for n in range(1, n+1):
        an = a1*(q**(n-1))
        approx_sum += an

    real_sum = a1/(1 - q)
    abs_error = abs(real_sum - approx_sum)
    return approx_sum, real_sum, abs_error


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


a1, q, error = 3, (1/4), [10**(-2), 10**(-5), 10**(-10)] 

for E in error:
    n = pg_error_analysis(a1, q, E)
    print(f'n = {n}')
