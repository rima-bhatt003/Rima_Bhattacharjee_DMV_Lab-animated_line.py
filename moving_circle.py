import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create circle
circle = Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

# Update function
def update(frame):
    circle.center = (frame, 5)  # Move circle horizontally
    return circle,

# Animate
ani = animation.FuncAnimation(fig, update, frames=range(0, 11), interval=100)

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
