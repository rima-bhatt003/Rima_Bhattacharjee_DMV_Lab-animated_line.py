import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

def get_float(prompt, default):

val = input(prompt)

try:

return float(val) if val.strip() != else default

except:

return default

get_float("Enter initial X position (0-18): ", 5) y get_float("Enter initial Y position (8-10): ", 5)

speed get_float("Enter speed: ", 0.2)

dx, dy = 8 e

fig, ax = plt.subplots()

circle = plt.Circle((x, y), 0.5, color='blue')

ax.add_patch(circle)

ax.set_xlim(0, 15)

ax.set ylim(0, 15)

ax.set_aspect('equal')

ax.set_xticks (range(0, 16))

ax.set_yticks (range(0, 16))

ax.set_xlabel("X-axis")

ax.set_ylabel("Y-axis") ylabel("Y-a

plt.grid(True)

def on_key(event):

global dx, dy

if event.key == 'up':

dx, dy = theta speed

elif event.key 'down': dx, dy = 0 -speed

elif event.key == 'left': dx, dyspeed, 0

elif event.key == 'right': dx, dy speed, 0

def update(frame):

global x, y

x+= dx

y+= dy

x= max ( theta.5 , min(x, 14.5))

y= max ( theta.5) min(y, 14.5))

circle.center = (x, y)

return circle,

fig.canvas.mp1 connect('key press event', on_key) ani FuncAnimation(fig, update, interval=30)

plt.show()