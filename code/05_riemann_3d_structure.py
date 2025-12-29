import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from scipy.special import sph_harm
from scipy.special import sph_harm_y

# 1. The Data: Riemann Zeros (The Shells / Energy Levels)
riemann_zeros = [
    14.1347, 21.0220, 25.0108, 30.4248, 32.9350, 37.5861, 40.9187, 43.3270, 48.0051, 49.7738,
    52.9703, 56.4462, 59.3470, 60.8317, 65.1125, 67.0798, 69.5464, 72.0671, 75.7046, 77.1448
]

print("Building the 3D Hologram of the Riemann Atom...")

# 2. Setup the 3D Grid (Angles)
theta = np.linspace(0, np.pi, 50)    # Polar angle (North-South)
phi = np.linspace(0, 2*np.pi, 50)    # Azimuthal angle (East-West)
theta, phi = np.meshgrid(theta, phi)

# 3. Create the 3D Structure
fig = plt.figure(figsize=(8, 8), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# We will layer the shells (like an onion)
# Each Riemann Zero creates a shell
for i, zero in enumerate(riemann_zeros[:8]): # Let's visualize the first 8 shells
    
    # Scale the zero down to fit in the plot
    r_base = zero / 20.0 
    
    # The "Vibration" of the shell
    # We use Spherical Harmonics (Y_lm). 
    # As energy (Zero value) increases, complexity (l, m) increases.
    # Logic: Higher frequency = more complex shape.
    l = i % 4  # Cycle through shapes (s, p, d, f orbitals)
    m = 0      # Keep it symmetric for clarity
    
    # Calculate the shape deformation
    harmonic = np.abs(sph_harm_y(m, l, phi, theta))
    
    # The Radius oscillates based on the harmonic
    r = r_base + (0.2 * harmonic) 
    
    # Convert to Cartesian (x, y, z)
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    # Plot the Shell
    # Use a "Ghostly" transparency so we can see inside
    ax.plot_surface(x, y, z, rstride=2, cstride=2, 
                    cmap='viridis', alpha=0.3, edgecolor='none')
    
    # Highlight the "Nodes" (The Wireframe)
    ax.plot_wireframe(x, y, z, rstride=10, cstride=10, 
                      colors='cyan', alpha=0.1, linewidth=0.5)

# 4. The Nucleus (The Bindu)
ax.scatter([0], [0], [0], color='yellow', s=100, label='Singularity')

# Aesthetics
ax.set_axis_off()
plt.title("The 3D Geometry of Riemann Resonance", color='white', fontsize=15)
plt.tight_layout()
plt.show()
