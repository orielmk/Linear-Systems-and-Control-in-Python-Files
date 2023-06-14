import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the numerator and denominator coefficients of the transfer function
num = [1, 1]  # (s+1)(s+2)(s+3)
den = [1, 0,1]  # s^4

# Create the transfer function
sys = signal.TransferFunction(num, den)

# Compute the frequency response
w, H = signal.freqresp(sys)

# Get the complex frequency response
G = H * np.exp(1j * 0)

# Plot the Nyquist diagram
plt.plot(np.real(G), np.imag(G), "b")
plt.plot(np.real(G), -np.imag(G), "r")
plt.plot(-1, 0, "ko")  # Plot the point (-1, 0) for the -1+j0 point
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.title("Nyquist Diagram")
plt.grid(True)
plt.axis("equal")

# Show the plot
plt.show()
