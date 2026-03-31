import matplotlib.pyplot as plt

speed = float(input("Enter step size (e.g., 0.5): "))

x, y = 5, 5

fig, ax = plt.subplots()

circle = plt.Circle((x, y), 0.5, color='blue')

ax.add_patch(circle)

ax.set_xlim(0, 10)

ax.set_ylim(0, 10)

ax.set_aspect('equal')

ax.set_title("Use Arrow Keys to Move the Circle")

def on_key(event):

global x, y

if event.key == 'up':

y += speed

elif event.key == 'down': y = speed

elif event.key == 'left': x -= speed

elif event.key 'right':

x += speed

# Keep inside bounds

x = max(0.5, min(x, 9.5))

y = max(0.5, min(y, 9.5))

# Update position

circle.center = (x, y)

fig.canvas.draw_idle()

fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()