import numpy as np
from scipy.io.wavfile import write

# 1. The Data: First 30 Riemann Zeros (The Frequencies)
# These are the "Dark Spots" on the Critical Line.
riemann_zeros = [
    14.1347, 21.0220, 25.0108, 30.4248, 32.9350, 37.5861, 40.9187, 43.3270, 48.0051, 49.7738,
    52.9703, 56.4462, 59.3470, 60.8317, 65.1125, 67.0798, 69.5464, 72.0671, 75.7046, 77.1448,
    79.3373, 82.9103, 84.7354, 87.4252, 88.8091, 92.4918, 94.6513, 95.8706, 98.8311, 101.3178
]

# 2. Audio Settings
sample_rate = 44100  # CD Quality
duration = 5.0       # Seconds
scaling_factor = 20  # Scale up frequencies so humans can hear them (14Hz * 20 = 280Hz)

# 3. Time Axis
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# 4. The Synthesizer: Stacking the Waves
# We start with silence
composite_wave = np.zeros_like(t)

print("Synthesizing the Prime Chord...")

for zero in riemann_zeros:
    freq = zero * scaling_factor
    # Generate a pure sine wave for this zero
    wave = np.sin(2 * np.pi * freq * t)
    # Add it to the composite (Superposition)
    composite_wave += wave
    print(f"Adding Frequency: {freq:.2f} Hz")

# 5. Normalization (Volume Control)
# If we just add 30 waves, the volume will be too loud. We scale it down to fit between -1 and 1.
composite_wave = composite_wave / np.max(np.abs(composite_wave))

# 6. Save to File
output_filename = "riemann_chord.wav"
# Convert to 16-bit integer PCM format for standard audio players
scaled_data = np.int16(composite_wave * 32767)
write(output_filename, sample_rate, scaled_data)

print(f"\nSaved audio to: {output_filename}")
print("Play this file. It is the sound of the Critical Line.")
