import numpy as np
import matplotlib.pyplot as plt
# write down some parameter

# number of girds (x, y) [-]
nx=4
nz=4

# Length (x ,y) [m]
Lx = 1
Lz = 1

# time step [sec]
dt = 0.1

# end of ime [sec]
time = 1

# viscousity coefficient [m^2/s]
nu = 1e-6

# set up
x = np.linspace(0,Lx,nx+1)
z = np.linspace(0,Lz,nz+1)
xx, zz = np.meshgrid(x,z)


# scalar & fulux
t = np.zeros((nx  ,nz  )) # [K]
u = np.zeros((nx+1,nz  )) # [m/s]
w = np.zeros((nx  ,nz+1)) # [m/s]
