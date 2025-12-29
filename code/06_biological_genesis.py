import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0

# 1. The Data: Riemann Zeros (The DNA Frequencies)
riemann_zeros = [
    14.1347, 21.0220, 25.0108, 30.4248, 32.9350, 37.5861, 40.9187, 43.3270, 48.0051, 49.7738,
    52.9703, 56.4462, 59.3470, 60.8317, 65.1125, 67.0798, 69.5464, 72.0671, 75.7046, 77.1448
]

# 2. Setup the Space (The Womb)
resolution = 800
x = np.linspace(-1.5, 1.5, resolution)
y = np.linspace(-1.5, 1.5, resolution)
X, Y = np.meshgrid(x, y)

# 3. Define Two Sources (Mitosis)
# Source A (Left) and Source B (Right)
source_a = np.array([-0.4, 0]) 
source_b = np.array([0.4, 0])

# Calculate distances from each pixel to the sources
# R1 = Distance to Source A
# R2 = Distance to Source B
R1 = np.sqrt((X - source_a[0])**2 + (Y - source_a[1])**2)
R2 = np.sqrt((X - source_b[0])**2 + (Y - source_b[1])**2)

# 4. The Simulation: Constructive Interference
Z_total = np.zeros_like(R1)

print("Igniting Binary Sources...")

for k in riemann_zeros:
    # We sum the waves from both sources
    # Interaction = Wave(A) + Wave(B)
    wave_field = j0(k * R1) + j0(k * R2)
    Z_total += wave_field

# 5. Visualization: The "Spark of Life"
plt.figure(figsize=(8, 8), facecolor='black')

# We use 'twilight' or 'seismic' to show the duality (Positive vs Negative waves)
plt.imshow(Z_total, extent=[-1.5, 1.5, -1.5, 1.5], cmap='twilight', origin='lower')

# Mark the Sources
plt.scatter([source_a[0], source_b[0]], [source_a[1], source_b[1]], 
            color='lime', s=50, label='Sources (Nuclei)')

plt.colorbar(label='Field Intensity')
plt.title('The Vesica Piscis: Riemann Interference Pattern', color='white', fontsize=15)
plt.axis('off')
plt.tight_layout()
plt.show()
