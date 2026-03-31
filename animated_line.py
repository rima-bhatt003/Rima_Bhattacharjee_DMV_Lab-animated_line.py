import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot([], [], color='blue')

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function
def update(frame):
    y = np.sin(x + frame)
    line.set_data(x, y)
    return line,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=np.linspace(0, 2*np.pi, 100),
    init_func=init, interval=50
)

plt.title("Animated Sine Wave")
plt.show()
