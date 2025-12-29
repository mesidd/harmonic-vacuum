import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0, j1

# 1. The Data: The Driving Frequencies (Riemann Zeros)
riemann_zeros = [
    14.1347, 21.0220, 25.0108, 30.4248, 32.9350, 37.5861, 40.9187, 43.3270, 48.0051, 49.7738,
    52.9703, 56.4462, 59.3470, 60.8317, 65.1125, 67.0798, 69.5464, 72.0671, 75.7046, 77.1448,
    79.3373, 82.9103, 84.7354, 87.4252, 88.8091, 92.4918, 94.6513, 95.8706, 98.8311, 101.3178
]

# 2. Setup the Particles (Chaos)
num_particles = 2000
# Random positions in a box from -1 to 1
positions = np.random.uniform(-1, 1, (num_particles, 2))
velocities = np.zeros_like(positions)

# Simulation Parameters
dt = 0.005       # Time step
friction = 0.90  # Damping (Particles lose energy and settle)
steps = 200      # How long to run the simulation

print(f"Dropping {num_particles} particles into the Riemann Field...")

# 3. The Physics Engine
for step in range(steps):
    # Get distance from center (r) for all particles
    r = np.sqrt(positions[:, 0]**2 + positions[:, 1]**2)
    
    # Avoid division by zero at the exact center
    r[r == 0] = 0.0001
    
    # Calculate the Field Intensity (Amplitude) and Gradient (Force) at current positions
    # We sum the contribution of ALL Riemann waves
    amplitude = np.zeros(num_particles)
    gradient = np.zeros(num_particles)
    
    for k in riemann_zeros:
        # Bessel function j0 is the wave height
        # Bessel function j1 is related to the slope (derivative)
        # We want particles to move to NODES (where Amplitude is 0)
        # Force pushes from High Amplitude -> Low Amplitude
        
        # Current wave height at particle position
        wave_val = j0(k * r)
        
        # Derivative of j0(x) is -j1(x). Chain rule gives factor of k.
        # This tells us which way is "downhill" towards a quiet spot
        slope = -k * j1(k * r) 
        
        # We push particles away from peaks (intensity gradient)
        # A simple approximation: Force ~ - Gradient of Energy (Amplitude^2)
        # F ~ - d/dr (A^2) = -2*A * dA/dr
        gradient += 2 * wave_val * slope

    # 4. Apply Forces (Newton's 2nd Law)
    # The force direction is radial (in or out along the radius)
    # Normalize position vector (x/r, y/r) to get direction
    norm_x = positions[:, 0] / r
    norm_y = positions[:, 1] / r
    
    # Force pushes towards negative gradient (downhill to node)
    # If gradient is positive (slope up), force is negative (push back)
    force_magnitude = -gradient 
    
    # Update Velocity
    velocities[:, 0] += force_magnitude * norm_x * dt
    velocities[:, 1] += force_magnitude * norm_y * dt
    
    # Apply Friction (Damping) so they settle
    velocities *= friction
    
    # Update Position
    positions += velocities * dt
    
    # Keep particles inside the box for viewing (optional)
    positions = np.clip(positions, -1, 1)

    if step % 50 == 0:
        print(f"Simulation Step {step}/{steps}...")

print("Morphogenesis Complete.")

# 5. Visualization: The Organized System
plt.figure(figsize=(8, 8), facecolor='black')

# Plot the particles as white stars
plt.scatter(positions[:, 0], positions[:, 1], s=1, c='cyan', alpha=0.6)

# Overlay the Center "Sun"
plt.scatter([0], [0], s=50, c='yellow', marker='o')

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axis('off')
plt.title('Gravity as Geometry: Particles Settling in Riemann Zones', color='white', fontsize=15)
plt.tight_layout()
plt.show()
