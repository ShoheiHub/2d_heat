import numpy as np
# write down some parameter

# number of girds (x, y) [-]
nx=2
ny=2

# Length (x ,y) [m]
Lx = 1
Ly = 1

# time step [sec]
dt = 0.1

# viscousity coefficient [m^2/s]
nu = 1e-6

# set up
x = np.linspace(0,1,nx)
y = np.linspace(0,1,ny)
xx, yy = np.meshgrid(x,y)

dx = np.array([ x[i+1]-x[i] for i in range(nx-1)])
dy = np.array([ y[j+1]-y[j] for j in range(ny-1)])
#print(dx)


t = np.zeros((nx  ,ny  ,3))
u = np.zeros((nx+1,ny  ,3))
v = np.zeros((nx  ,ny+1,3))
