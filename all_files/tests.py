import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
initial_velocity = 50  # m/s
launch_angle_deg = 45  # degrees
gravity = 9.81         # m/s^2

# Convert launch angle to radians
launch_angle_rad = np.radians(launch_angle_deg)

# Calculate initial velocity components
vx0 = initial_velocity * np.cos(launch_angle_rad)
vy0 = initial_velocity * np.sin(launch_angle_rad)

# Time array
time = np.linspace(0, 10, 500)  # Simulate for 10 seconds with 500 steps

# Calculate horizontal and vertical positions over time
x_position = vx0 * time
y_position = (vy0 * time) - (0.5 * gravity * time**2)

# Filter out points where the projectile has hit the ground (y < 0)
valid_indices = y_position >= 0
x_position_valid = x_position[valid_indices]
y_position_valid = y_position[valid_indices]

# Plot the trajectory
plt.figure(figsize=(8, 6))
plt.plot(x_position_valid, y_position_valid)
plt.title("Projectile Motion Simulation")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.show()