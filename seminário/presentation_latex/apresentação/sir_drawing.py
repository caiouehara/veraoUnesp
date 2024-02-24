
import numpy as np
from scipy.integrate import odeint
import pandas as pd

# SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Set the initial conditions and parameters
N = 1000  # Total population
I0 = 1    # Initial number of infected individuals
R0 = 0    # Initial number of recovered individuals
S0 = N - I0 - R0  # Initial number of susceptible individuals
beta = 0.3  # Infection rate
gamma = 0.1  # Recovery rate

# Set the time grid (in days)
t = np.linspace(0, 200, 200)

# Integrate the SIR equations over the time grid
y = odeint(deriv, (S0, I0, R0), t, args=(N, beta, gamma))

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame({'t': t, 'S': y[:, 0], 'I': y[:, 1], 'R': y[:, 2]})
df.to_csv('data.csv', index=False)
