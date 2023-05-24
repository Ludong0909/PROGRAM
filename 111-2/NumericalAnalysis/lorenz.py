from vpython import *

def lorenz(x, y, z, s=10, r=28.5, b=8/3):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

dt = 0.01
num_steps = 10000

x = 0.1
y = 20
z = 1.05

scene = canvas(title="Lorenz Model", width=800, height=600, background = color.white)
line = curve(color=color.red, radius=0.1)

# Variables to store mouse drag information
dragging = False
prev_x = None
prev_y = None

# Function to handle mouse drag events
def on_mouse_down(event):
    global dragging, prev_x, prev_y
    dragging = True
    prev_x = event.pos.x
    prev_y = event.pos.y

def on_mouse_move(event):
    global dragging, prev_x, prev_y
    if dragging:
        dx = (event.pos.x - prev_x) / scene.width
        dy = (event.pos.y - prev_y) / scene.height
        scene.camera.rotate(phi=4 * dx * pi, angle=4 * dy * pi)
        prev_x = event.pos.x
        prev_y = event.pos.y

def on_mouse_up(event):
    global dragging
    dragging = False

# Bind mouse events to handle dragging and rotation
scene.bind("mousedown", on_mouse_down)
scene.bind("mousemove", on_mouse_move)
scene.bind("mouseup", on_mouse_up)

# Create axes
x_axis = arrow(pos=vector(-20, 0, 0), axis=vector(80, 0, 0), color=color.white, shaftwidth=0.2)
y_axis = arrow(pos=vector(0, -30, 0), axis=vector(0, 120, 0), color=color.white, shaftwidth=0.2)
z_axis = arrow(pos=vector(0, 0, -30), axis=vector(0, 0, 120), color=color.white, shaftwidth=0.2)

for i in range(num_steps):
    rate(1000)

    x_dot, y_dot, z_dot = lorenz(x, y, z)
    x += x_dot * dt
    y += y_dot * dt
    z += z_dot * dt

    line.append(pos=vector(x, y, z))

