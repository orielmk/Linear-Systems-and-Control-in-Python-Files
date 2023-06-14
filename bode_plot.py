# bode plots
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Example transfer function: H(s) = (s + 1) / (s^2 + 2s + 2)
mone = [1, 4]
mehane = [1, 3, 2, 0]
sys = signal.TransferFunction(mone, mehane)

# Generate the frequency response
w, mag, phase = signal.bode(sys)

# Find the frequency where magnitude crosses 0 dB (gain crossover frequency)
gain_crossover_index = np.argmin(np.abs(mag))
gain_crossover_freq = w[gain_crossover_index]

# Find the phase at gain crossover frequency
phase_at_gain_crossover = phase[gain_crossover_index]

# Calculate the phase margin
phase_margin = 180 + phase_at_gain_crossover

# Find the frequency where phase is -180 degrees (phase crossover frequency)
phase_crossover_index = np.argmin(np.abs(phase + 180))
phase_crossover_freq = w[phase_crossover_index]

# Calculate the gain margin at phase crossover frequency
gain_at_phase_crossover = mag[phase_crossover_index]

# Calculate the gain margin
gain_margin = -gain_at_phase_crossover

# Plot the Bode plot
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)

plt.axvline(gain_crossover_freq, color='r', linestyle='--')
plt.axvline(phase_crossover_freq, color='g', linestyle='--')

plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Phase [degrees]')
plt.grid(True)

plt.axvline(gain_crossover_freq, color='r', linestyle='--')
plt.axvline(phase_crossover_freq, color='g', linestyle='--')

plt.show()

# Print the gain margin and phase margin
print("Gain margin:", gain_margin, "dB")
print("Phase margin:", phase_margin, "degrees")
