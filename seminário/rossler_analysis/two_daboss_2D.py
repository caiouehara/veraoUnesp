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


def sol_rossler(t, a, b, c, init_cond):
    # a, b, c = 0.2, 0.2, 5.7
    # y0 = [0, -6.78, 0.02]
    cons = (a, b, c)

    t_span = [0, int(t)]
    # Obtain 1000 points in the approximation
    t_eval = np.linspace(*t_span, int(t) * 1000)

    sol = solve_ivp(
        rossler_system, t_span, init_cond, method="RK45", t_eval=t_eval, args=cons
    )
    print(sol)
    sol_values = sol.y
    sol_values_cut = cut_beggining(sol_values, 0.3)
    t_values = sol.t
    t = cut_beggining(t_values, 0.3)
    x = sol_values_cut[0]
    y = sol_values_cut[1]
    z = sol_values_cut[2]
    return t, x, y, z


init_t, init_a, init_b, init_c = 100, 0.1, 0.1, 4
init_x0, init_y0, init_z0 = 0.2, 0.7, 1.2
init_cond = [init_x0, init_y0, init_z0]

pert = 0
init_cond_pert = [init_x0 + pert, init_y0 + pert, init_z0 + pert]

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

t, x, y, z = sol_rossler(init_t, init_a, init_b, init_c, init_cond)
t_pert, x_pert, y_pert, z_pert = sol_rossler(
    init_t, init_a, init_b, init_c, init_cond_pert
)


ax1.plot(x, y, color="red")

if pert != 0:
    ax1.plot(x_pert, y_pert, color="#FFD500")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("xy")
# plt.tight_layout()

ax2.plot(x, z, color="green")

if pert != 0:
    ax2.plot(x_pert, z_pert, color="#FFD500")
ax2.set_xlabel("x")
ax2.set_ylabel("z")
ax2.set_title("xz")


ax3.plot(y, z, color="blue")

if pert != 0:
    ax3.plot(y_pert, z_pert, color="#FFD500")
ax3.set_xlabel("x")
ax3.set_ylabel("z")
ax3.set_title("xz")


if pert != 0:
    ax2.text(
        0.1,
        1,
        "sol. perturbada",
        color="#FFD500",
        transform=ax2.transAxes,
        fontsize=14,
        bbox=dict(facecolor="white", edgecolor="#FFD500"),
    )


fig.subplots_adjust(bottom=0.3)


ax_a = fig.add_axes([0.25, 0.2, 0.3, 0.03])
a_slider = Slider(
    ax=ax_a,
    label="a",
    valmin=0,
    valmax=0.38,
    valinit=init_a,
)

ax_b = fig.add_axes([0.25, 0.15, 0.3, 0.03])
b_slider = Slider(
    ax=ax_b,
    label="b",
    valmin=0,
    valmax=1,
    valinit=init_b,
)


ax_c = fig.add_axes([0.25, 0.1, 0.3, 0.03])
c_slider = Slider(
    ax=ax_c,
    label="c",
    valmin=0,
    valmax=20,
    valinit=init_c,
)
""" yoo """
ax_x0 = fig.add_axes([0.60, 0.2, 0.3, 0.03])
x0_slider = Slider(
    ax=ax_x0,
    label="x0",
    valmin=-10,
    valmax=10,
    valinit=init_x0,
)

ax_y0 = fig.add_axes([0.60, 0.15, 0.3, 0.03])
y0_slider = Slider(
    ax=ax_y0,
    label="y0",
    valmin=-10,
    valmax=10,
    valinit=init_y0,
)


ax_z0 = fig.add_axes([0.60, 0.1, 0.3, 0.03])
z0_slider = Slider(
    ax=ax_z0,
    label="z0",
    valmin=-10,
    valmax=10,
    valinit=init_z0,
)


ax_t = fig.add_axes([0.25, 0.05, 0.65, 0.03])
t_slider = Slider(
    ax=ax_t,
    label="t",
    valmin=0,
    valmax=800,
    valinit=init_t,
)

ax_pert = fig.add_axes([0.08, 0.1, 0.1, 0.03])
pert_slider = Slider(
    ax=ax_pert,
    label="perturbação",
    valmin=-1 / 10000,
    valmax=1 / 10000,
    valinit=pert,
)


def update(val):
    ax_a = a_slider.val
    ax_b = b_slider.val
    ax_c = c_slider.val
    ax_x0 = x0_slider.val
    ax_y0 = y0_slider.val
    ax_z0 = z0_slider.val
    ax_t = t_slider.val
    ax_pert = pert_slider.val
    init_cond = [ax_x0, ax_y0, ax_z0]
    init_cond_pert = [ax_x0 + ax_pert, ax_y0 + ax_pert, ax_z0 + ax_pert]
    ax1.clear()
    ax2.clear()
    ax3.clear()
    t, x, y, z = sol_rossler(ax_t, ax_a, ax_b, ax_c, init_cond)
    t, x_pert, y_pert, z_pert = sol_rossler(ax_t, ax_a, ax_b, ax_c, init_cond_pert)
    print("x", x)
    print("y", y)
    print("z", z)

    # testing
    ax1.plot(x, y, color="red")
    if ax_pert != 0:
        ax1.plot(x_pert, y_pert, color="#FFD500")
        ax2.text(
            0.1,
            1,
            "sol. perturbada",
            color="#FFD500",
            transform=ax2.transAxes,
            fontsize=14,
            bbox=dict(facecolor="white", edgecolor="#FFD500"),
        )
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("xy")
    # plt.tight_layout()

    ax2.plot(x, z, color="green")
    if ax_pert != 0:
        ax2.plot(x_pert, z_pert, color="#FFD500")
    ax2.set_xlabel("x")
    ax2.set_ylabel("z")
    ax2.set_title("xz")

    ax3.plot(y, z, color="blue")
    if ax_pert != 0:
        ax3.plot(y_pert, z_pert, color="#FFD500")
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
x0_slider.on_changed(update)
y0_slider.on_changed(update)
z0_slider.on_changed(update)
t_slider.on_changed(update)
pert_slider.on_changed(update)

resetax = fig.add_axes([0.08, 0.15, 0.1, 0.04])
button = Button(resetax, "Reset", hovercolor="0.975")


def reset(event):
    a_slider.reset()
    b_slider.reset()
    c_slider.reset()
    x0_slider.reset()
    y0_slider.reset()
    z0_slider.reset()
    t_slider.reset()
    pert_slider.reset()


button.on_clicked(reset)

plt.show()
