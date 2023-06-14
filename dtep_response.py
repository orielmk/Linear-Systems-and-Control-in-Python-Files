import numpy as np
import control
import matplotlib.pyplot as plt

# Define the transfer function
# num = [1]
# den = [8**0.5, 2**0.5, 0]
#
#
# # Create the transfer function object
# sys = control.TransferFunction(num, den)
gp1 = [50]
gp2 = [2, 1, 0]
gp = control.TransferFunction(gp1,gp2)
gc1 = [500/21, 1]
gc2 = [50000/23, 1]
gc = control.TransferFunction(gc1, gc2)
sys = gp*gc
# Compute the step response
t, y = control.step_response(sys/(1+sys))

# Plot the step response
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid(True)
plt.show()
