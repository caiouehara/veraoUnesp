import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp


def cut_beggining(M, percent):
    if len(M.shape) > 1:
        return np.delete(M, np.arange(int(len(M[1]) * percent)), 1)
    else:
        return np.delete(M, np.arange(int(len(M) * percent)), 0)


def rossler_system(t, xyz, a, b, c):
    x, y, z = xyz
    return [-(y + z), x + a * y, b + z * (x - c)]


def lorenz_system(t, xyz, a, b, c):
    x, y, z = xyz
    return [a * (y - x), x * (b - z) - y, x * y - c * z]


def example_paper_1():
    a = 10
    b = 28
    c = 8 / 3
    cons = (a, b, c)

    y0 = [2.9, -1.3, 25]
    t_span = [0, 150]  # Adjust time span as needed

    # Obtain 1000 points in the approximation
    t_eval = np.linspace(*t_span, 10000)

    sol = solve_ivp(lorenz_system, t_span, y0, t_eval=t_eval, args=cons)

    sol_values = sol.y
    sol_values_cut = cut_beggining(sol_values, 0.3)
    x = sol_values_cut[0]
    y = sol_values_cut[1]
    z = sol_values_cut[2]

    plt.figure()
    ax = plt.axes(projection="3d")
    # ax.set(xlim=(-29, 29), ylim=(0, 58), zlim=(0, 58))
    ax.plot3D(x, y, z, "green")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Lorenz System Solution")
    return sol


def example_paper_2():
    """
    a, b, c = 0.1, 0.1, 14
    y0 = [0.0, 2.0, 0.0]
    """
    a, b, c = 0.2, 0.2, 5.7
    y0 = [0, -6.78, 0.02]
    cons = (a, b, c)

    t_span = [0, 340]
    # Obtain 1000 points in the approximation
    t_eval = np.linspace(*t_span, 10000)

    sol = solve_ivp(
        rossler_system, t_span, y0, method="LSODA", t_eval=t_eval, args=cons
    )
    print(sol)
    sol_values = sol.y
    sol_values_cut = cut_beggining(sol_values, 0.3)
    x = sol_values_cut[0]
    y = sol_values_cut[1]
    z = sol_values_cut[2]

    plt.figure()
    ax = plt.axes(projection="3d")
    # ax.set(xlim=(-29, 29), ylim=(0, 58), zlim=(0, 58))
    ax.plot3D(x, y, z, "green")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Rossler System Solution")
    return sol


def example_paper_2_figs(sol):
    sol_values = sol.y
    sol_values_cut = cut_beggining(sol_values, 0.3)
    t_values = sol.t
    t = cut_beggining(t_values, 0.3)
    x = sol_values_cut[0]
    y = sol_values_cut[1]
    z = sol_values_cut[2]

    plt.figure()
    plt.plot(t, x, label="x(t)")
    plt.plot(t, y, label="y(t)")
    plt.plot(t, z, label="z(t)")
    plt.xlabel("tempo")
    plt.title("Série Temporal do Sistema Rossler")
    plt.legend()

    plt.tight_layout()


def example_viana():
    """
    a, b, c = 0.1, 0.1, 14
    y0 = [0.0, 2.0, 0.0]
    """
    a, b = 0.2, 0.2
    cc = [2.3, 3.3, 4.3, 5.3]
    # cc = [(x + 0.3) for x in range(6, 14)]  # goes crazy
    # cc = np.arange(1.7, 0, -0.1)       #breaks at 1.2
    y0 = [0, -6.78, 0.02]

    t_span = [0, 1000]
    # Obtain 1000 points in the approximation
    t_eval = np.linspace(*t_span, 100000)

    for c in cc:
        sol = solve_ivp(rossler_system, t_span, y0, t_eval=t_eval, args=(a, b, c))
        print(sol)
        sol_values = sol.y
        sol_values_cut = cut_beggining(sol_values, 0.3)
        x = sol_values_cut[0]
        y = sol_values_cut[1]
        z = sol_values_cut[2]

        plt.figure()
        ax = plt.axes(projection="3d")
        # ax.set(xlim=(-29, 29), ylim=(0, 58), zlim=(0, 58))
        ax.plot3D(x, y, z, "green")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title(f"Rossler System Solution {c}")
        plt.show()


example_viana()
"""
example_paper_1()
ex2 = example_paper_2()
example_paper_2_figs(ex2)
plt.show()
"""
