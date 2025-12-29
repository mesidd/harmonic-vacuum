import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0  # Bessel function of the first kind (Drumhead physics)

# 1. The Data: The First 30 Riemann Zeros (The Driving Frequencies)
riemann_zeros = [
    14.1347, 21.0220, 25.0108, 30.4248, 32.9350, 37.5861, 40.9187, 43.3270, 48.0051, 49.7738,
    52.9703, 56.4462, 59.3470, 60.8317, 65.1125, 67.0798, 69.5464, 72.0671, 75.7046, 77.1448,
    79.3373, 82.9103, 84.7354, 87.4252, 88.8091, 92.4918, 94.6513, 95.8706, 98.8311, 101.3178
]

# 2. Setup the "Drum" (The 2D Grid)
resolution = 1000  # High res for smooth geometry
x = np.linspace(-1, 1, resolution)
y = np.linspace(-1, 1, resolution)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)  # Distance from center (Radius)

# Mask: We only care about the circle, not the square corners
mask = R <= 1.0

# 3. The Simulation: Superposition of Waves
# We sum the vibrations of all Riemann Zeros acting on the surface
Z_total = np.zeros_like(R)

print("Vibrating the Quantum Drum with Prime Frequencies...")

for t in riemann_zeros:
    # Scale frequency slightly to fit the unit circle visually
    # t represents the wavenumber k in J0(kr)
    # We use the raw zero value because it IS the natural frequency
    wave_mode = j0(t * R)
    Z_total += wave_mode

# Apply the circular mask (silence outside the drum)
Z_total[~mask] = np.nan

# 4. Visualization: The Chladni Pattern
plt.figure(figsize=(8, 8), facecolor='black')

# Plotting the "Nodes" (Where vibration is zero)
# In real life, sand collects where amplitude is near zero.
# We visualize the absolute amplitude. Dark = Sand (Nodes). Light = Vibration.
plt.imshow(np.abs(Z_total), extent=[-1, 1, -1, 1], cmap='inferno', origin='lower')

# Aesthetic tweaks
plt.axis('off')
plt.title('The Geometry of the Riemann Chord (Cymatics)', color='white', fontsize=15)
plt.tight_layout()

print("Rendering the geometry...")
plt.show()
