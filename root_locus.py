import numpy as np
import matplotlib.pyplot as plt
import control

# Define the numerator and denominator coefficients of the transfer function
num = [2**0.5]  # (s+1)(s+2)(s+3)
den = [1,1,0]  # s^4

# Create the transfer function
sys = control.TransferFunction(num, den)

# Compute the roots of the transfer function
zeros = sys.zero()
poles = sys.pole()

# Plot the root locus
control.root_locus(sys)

# Set up the plot
plt.plot(np.real(zeros), np.imag(zeros), "ko", label="Zeros")
plt.plot(np.real(poles), np.imag(poles), "rx", label="Poles")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.title("Root Locus")
plt.legend()
plt.grid(True)
plt.axis("equal")

# Show the plot
plt.show()
