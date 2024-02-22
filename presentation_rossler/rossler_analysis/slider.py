import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib.widgets import Button, Slider
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


def sol_rossler(a, b, c):
    # a, b, c = 0.2, 0.2, 5.7
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
    return x, y, z


init_a, init_b, init_c = 0.1, 0.1, 4

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(projection="3d")


x, y, z = sol_rossler(init_a, init_b, init_c)
drawing = ax.plot3D(x, y, z)


ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Rossler System Solution")


fig.subplots_adjust(bottom=0.2)


# horizontal axes
ax_a = fig.add_axes([0.25, 0.15, 0.65, 0.03])
a_slider = Slider(
    ax=ax_a,
    label="a",
    valmin=0,
    valmax=30,
    valinit=init_a,
)

# ax_b = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
ax_b = fig.add_axes([0.25, 0.1, 0.65, 0.03])
b_slider = Slider(
    ax=ax_b,
    label="b",
    valmin=0,
    valmax=30,
    valinit=init_b,
)


# horizontal axes
ax_c = fig.add_axes([0.25, 0.05, 0.65, 0.03])
c_slider = Slider(
    ax=ax_c,
    label="c",
    valmin=2,
    valmax=30,
    valinit=init_c,
)


# The function to be called anytime a slider's value changes
def update(val):
    ax_a = a_slider.val
    ax_b = b_slider.val
    ax_c = c_slider.val
    ax.clear()
    x, y, z = sol_rossler(ax_a, ax_b, ax_c)
    print("x", x)
    print("y", y)
    print("z", z)
    ax.plot3D(x, y, z)
    fig.canvas.draw_idle()
    print("after plot")


# register the update function with each slider
a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, "Reset", hovercolor="0.975")


def reset(event):
    a_slider.reset()
    b_slider.reset()
    c_slider.reset()


button.on_clicked(reset)

plt.show()

####
####
####
####
####
####

"""
# The parametrized function to be plotted
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)


t = np.linspace(0, 1, 1000)

# Define initial parameters
init_amplitude = 5
init_frequency = 3

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
(line,) = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel("Time [s]")

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label="Frequency [Hz]",
    valmin=0.1,
    valmax=30,
    valinit=init_frequency,
)

# Make a vertically oriented slider to control the amplitude
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical",
)


# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
freq_slider.on_changed(update)
amp_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, "Reset", hovercolor="0.975")


def reset(event):
    freq_slider.reset()
    amp_slider.reset()


button.on_clicked(reset)

plt.show()
"""
