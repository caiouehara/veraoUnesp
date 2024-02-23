import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
from scipy.integrate import solve_ivp
# from matplotlib import cm
# from mpl_toolkits.mplot3d.axes3d import get_test_data
# from mpl_toolkits.mplot3d import Axes3D


def cut_beggining(M, percent):
    if len(M.shape) > 1:
        return np.delete(M, np.arange(int(len(M[1]) * percent)), 1)
    else:
        return np.delete(M, np.arange(int(len(M) * percent)), 0)


def rossler_system(t, xyz, a, b, c):
    x, y, z = xyz
    return [-(y + z), x + a * y, b + z * (x - c)]


def sol_rossler(a, b, c):
    # a, b, c = 0.2, 0.2, 5.7
    y0 = [0, -6.78, 0.02]
    cons = (a, b, c)

    t_span = [0, 100]
    # Obtain 1000 points in the approximation
    t_eval = np.linspace(*t_span, 10000)

    sol = solve_ivp(rossler_system, t_span, y0, method="RK45", t_eval=t_eval, args=cons)
    print(sol)
    sol_values = sol.y
    sol_values_cut = cut_beggining(sol_values, 0.3)
    t_values = sol.t
    t = cut_beggining(t_values, 0.3)
    x = sol_values_cut[0]
    y = sol_values_cut[1]
    z = sol_values_cut[2]
    return t, x, y, z


init_a, init_b, init_c = 0.1, 0.1, 4


fig = plt.figure(figsize=plt.figaspect(0.5))
# ax = fig.add_subplot(1, 2, 2, projection="3d")
# ax = fig.add_subplot(projection="3d")

ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# textstr = "x -- red,\ny --green,\nz --blue"
# props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

"""
ax1.text(
    -0.4,
    0.9,
    "--x(t)",
    color="red",
    transform=ax.transAxes,
    fontsize=14,
    bbox=dict(facecolor="white", edgecolor="red"),
)
ax1.text(
    -0.4,
    0.85,
    "--y(t)",
    color="green",
    transform=ax.transAxes,
    fontsize=14,
    bbox=dict(facecolor="white", edgecolor="green"),
)
ax1.text(
    -0.4,
    0.8,
    "--z(t)",
    color="blue",
    transform=ax.transAxes,
    fontsize=14,
    bbox=dict(facecolor="white", edgecolor="blue"),
)
"""

t, x, y, z = sol_rossler(init_a, init_b, init_c)


ax1.plot(x, y, color="red")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("xy")
# plt.tight_layout()

ax2.plot(x, z, color="green")
ax2.set_xlabel("x")
ax2.set_ylabel("z")
ax2.set_title("xz")


ax3.plot(y, z, color="blue")
ax3.set_xlabel("x")
ax3.set_ylabel("z")
ax3.set_title("xz")


fig.subplots_adjust(bottom=0.25)


ax_a = fig.add_axes([0.25, 0.15, 0.65, 0.03])
a_slider = Slider(
    ax=ax_a,
    label="a",
    valmin=0,
    valmax=0.4,
    valinit=init_a,
)

ax_b = fig.add_axes([0.25, 0.1, 0.65, 0.03])
b_slider = Slider(
    ax=ax_b,
    label="b",
    valmin=0,
    valmax=1,
    valinit=init_b,
)


ax_c = fig.add_axes([0.25, 0.05, 0.65, 0.03])
c_slider = Slider(
    ax=ax_c,
    label="c",
    valmin=0,
    valmax=20,
    valinit=init_c,
)


def update(val):
    ax_a = a_slider.val
    ax_b = b_slider.val
    ax_c = c_slider.val
    ax1.clear()
    ax2.clear()
    ax3.clear()
    t, x, y, z = sol_rossler(ax_a, ax_b, ax_c)
    print("x", x)
    print("y", y)
    print("z", z)

    # testing
    ax1.plot(x, y, color="red")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("xy")
    # plt.tight_layout()

    ax2.plot(x, z, color="green")
    ax2.set_xlabel("x")
    ax2.set_ylabel("z")
    ax2.set_title("xz")

    ax3.plot(y, z, color="blue")
    ax3.set_xlabel("x")
    ax3.set_ylabel("z")
    ax3.set_title("xz")
    # text
    """
    ax1.text(
        -0.4,
        0.9,
        "--x(t)",
        color="red",
        transform=ax.transAxes,
        fontsize=14,
        bbox=dict(facecolor="white", edgecolor="red"),
    )
    ax1.text(
        -0.4,
        0.85,
        "--y(t)",
        color="green",
        transform=ax.transAxes,
        fontsize=14,
        bbox=dict(facecolor="white", edgecolor="green"),
    )
    ax1.text(
        -0.4,
        0.8,
        "--z(t)",
        color="blue",
        transform=ax.transAxes,
        fontsize=14,
        bbox=dict(facecolor="white", edgecolor="blue"),
    )
    """

    fig.canvas.draw_idle()
    print("after plot")


a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

resetax = fig.add_axes([0.1, 0.1, 0.1, 0.04])
button = Button(resetax, "Reset", hovercolor="0.975")


def reset(event):
    a_slider.reset()
    b_slider.reset()
    c_slider.reset()


button.on_clicked(reset)

plt.show()
