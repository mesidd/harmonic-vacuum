import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp, zeta, findroot

# 1. Setup High Precision
mp.dps = 25 

# 2. Define the Zeta Grid
# We go slightly past 1 to make sure we see the full strip, but handle the pole logic below
real_axis = np.linspace(0, 1, 100)
imag_axis = np.linspace(0, 50, 500)

Z = np.zeros((len(imag_axis), len(real_axis)), dtype=complex)

print("Calculating the Zeta Field... (Scanning the Terrain)")

# 3. Compute Zeta for every point in the grid
for i, y in enumerate(imag_axis):
    for j, x in enumerate(real_axis):
        s = complex(x, y)
        
        # --- THE FIX IS HERE ---
        try:
            # Try to calculate Zeta
            Z[i, j] = complex(zeta(s))
        except ValueError:
            # If we hit the "Pole" at s=1, just set it to NaN (Not a Number)
            # This tells the plot to just leave that pixel blank/white
            Z[i, j] = complex(np.nan, np.nan) 

# 4. Extract the Magnitude 
M = np.abs(Z)

# 5. Visualization
plt.figure(figsize=(12, 8))

# Plot the Heatmap
plt.imshow(np.log(M + 1), extent=[0, 1, 0, 50], origin='lower', aspect='auto', cmap='magma')

# Draw the Critical Line
plt.axvline(x=0.5, color='cyan', linestyle='--', linewidth=2, label='Critical Line (0.5)')

plt.colorbar(label='Log Magnitude of Zeta(s)')
plt.title('The Riemann Zeta Landscape: Hunting for Zeros')
plt.xlabel(r'Real Part ( $\sigma$ )')
plt.ylabel(r'Imaginary Part ( $t$ ) - Frequency')
plt.legend()
plt.show()

# 6. The "Zero Hunter"
print("\nScanning the Critical Line (0.5 + it) for the first few Zeros...")
print("-" * 50)

target_t_values = [14.1, 21.0, 25.0, 30.4, 32.9]

for t_guess in target_t_values:
    try:
        root = findroot(zeta, complex(0.5, t_guess))
        
        t_value = float(root.imag)
        magnitude = float(abs(zeta(root)))
        
        print(f"Zero found at: 0.5 + i({t_value:.5f}) | Magnitude: {magnitude:.2e}")
        
    except Exception as e:
        print(f"Could not converge on zero near {t_guess}: {e}")
