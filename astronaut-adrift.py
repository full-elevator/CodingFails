## I attempted to make the classic Windows XP screensaver,
## "The astronaut adrift" with matplotlib animations.
## Glad I decided to abandon this project.

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def generate(axis):
    rand = (np.random.random() - 1) * 4 * np.pi
    if axis == "x": return 960 + np.cos(rand) * 50
    elif axis == "y": return 540 + np.sin(rand) * 50
    else: raise ValueError

def init():
    ax.set_xlim(0, 1920)
    ax.set_ylim(0, 1080)
    return line,    #comma needed, returns a line 2D object

def update(frame):
    for i in range(len(pos_x)):
        deltaX = pos_x[i] - 960
        deltaY = pos_y[i] - 540
        pos_x[i] = pos_x[i] + deltaX / 5
        pos_y[i] = pos_y[i] + deltaY / 5
        if pos_x[i] <= 0 or pos_x[i] >= 1920 or pos_y[i] <= 0 or pos_y[i] >= 1080:
            pos_x[i] = generate("x")
            pos_y[i] = generate("y")
    line.set_data(pos_x, pos_y)
    return line,

n = int(input("number of stars > "))
pos = np.zeros((2, n), dtype = np.float16)
fig = plt.figure(figsize = (7, 7))
ax = fig.add_subplot(1, 1, 1)
pos_x = [generate("x") for i in range(n)]
pos_y = [generate("y") for i in range(n)]
line, = ax.plot([], [], "ro")
anim = FuncAnimation(fig, update, interval = 50, frames = np.linspace(0, 2, 50), init_func = init, blit = True)
plt.show()
