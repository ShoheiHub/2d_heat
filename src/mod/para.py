import numpy as np
import matplotlib.pyplot as plt
# write down some parameter

# number of girds (x, y) [-]
nz=3
nx=3

# Length (x ,y) [m]
Lx = 1
Lz = 1

# time step [sec]
dt = 0.1

# end of ime [sec]
time = 1

# viscousity coefficient [m^2/s]
nu = 1e-6

# diffusivity coefficient [m^2/s]
Kh = 1e-6
Kv = 1e-6

# scalar & fulux
t = np.zeros((nx  ,nz  )) # [K]
u = np.zeros((nx+1,nz  )) # [m/s]
w = np.zeros((nx  ,nz+1)) # [m/s]

tp = np.zeros((nx  ,nz  )) # [K]
up = np.zeros((nx+1,nz  )) # [m/s]
wp = np.zeros((nx  ,nz+1)) # [m/s]

tm = np.zeros((nx  ,nz  )) # [K]
um = np.zeros((nx+1,nz  )) # [m/s]
wm = np.zeros((nx  ,nz+1)) # [m/s]

# set up grid
# along with grid line
x = np.linspace(0,Lx,nx+1)
z = np.linspace(0,Lz,nz+1)
xx, zz = np.meshgrid(x,z)

# vector of U
xu = np.array([ x[i] for i in range(nx+1) ])
zu = np.array([ 0.5*(z[k+1]+z[k]) for k in range(nz) ])
xxu, zzu = np.meshgrid(xu,zu)

# vector of W
xw = np.array([ 0.5*(x[i]+x[i+1]) for i in range(nx) ])
zw = np.array([ z[k] for k in range(nz+1) ])
xxw, zzw = np.meshgrid(xw,zw)

# scallar 
xs = np.array([ 0.5*(xu[i]+xu[i+1]) for i in range(nx) ])
zs = np.array([ 0.5*(zw[k+1]+zw[k]) for k in range(nz) ])
xxs, zzs = np.meshgrid(xs,zs)
