import numpy as np
import matplotlib.pyplot as plt
D = 100 # diffusivity
Lx = 300 # length of grid
dx = 0.5 # step size
x = np.arange(start=0, stop=Lx, step=dx) # array
nx = len(x) # array length
C = np.zeros_like(x) #creates array filled with zeros mirroring array x
C_left = 500
C_right = 0
C[x <= Lx//2] = C_left # // returns integers only
C[x > Lx//2] = C_right
plt.figure()
plt.plot(x,C,"r")
plt.xlabel("x")
plt.ylabel("C")
plt.title("Initial concentration profile")
time = 0
nt = 5000
dt = 0.5 * dx**2 / D # ** = ^ in R
for t in range(0, nt):
    C += D * dt / dx**2 * (np.roll(C, -1) - 2*C + np.roll(C, 1)) # += adds current value to result
    C[0] = C_left
    C[-1] = C_right
plt.figure()
plt.plot(x, C, "b")
plt.xlabel("x")
plt.ylabel("C")
plt.title("Final concentration profile")