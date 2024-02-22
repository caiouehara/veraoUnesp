import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons


fig = plt.figure()
plt.subplots_adjust(bottom=0.25)
X = np.arange(-50, 50, 2)
Y = np.arange(-50, 50, 2)
X, Y = np.meshgrid(X, Y)

Z = np.sqrt((X**2 + Y**2) / (np.tan(np.pi / 120)))
plt.axis("scaled")

h0 = 0

ax2 = fig.add_subplot(projection="3d")
Z2 = 0 * X + 0 * Y + h0

l = ax2.plot_surface(X, Y, Z2, color="red", rstride=2, cstride=2)

axhauteur = plt.axes([0.2, 0.1, 0.65, 0.03])
shauteur = Slider(axhauteur, "Hauteur", 0.5, 10.0, valinit=h0)


def update(val):
    h = shauteur.val
    ax2.clear()
    l = ax2.plot_surface(X, Y, 0 * X + 0 * Y + h)
    ax2.set_zlim(0, 10)
    fig.canvas.draw_idle()


shauteur.on_changed(update)
ax2.set_zlim(0, 10)

plt.show()
