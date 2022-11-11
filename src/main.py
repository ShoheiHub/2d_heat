import numpy as np
import matplotlib.pyplot as plt


from mod import *

print(mod1())

"""
nx = 5
nz = 5

Lx = 1
Lz = 1

dt = 0.1


# set-up parameter
nu = 1.e-6

# set-up array
x = np.linspace(0,Lx,nx)
z = np.linspace(0,Lz,nz)

xx, zz = np.meshgrid(x,z,indexing='ij')

# scalar <'m':t-1, ' ':t, 'p':t+1>
t  = np.zeros((nx,nz))
tp = np.zeros((nx,nz))
tm = np.zeros((nx,nz))
# flux <'m':t-1, ' ':t, 'p':t+1>
u  = np.zeros((nx,nz))
up = np.zeros((nx,nz))
um = np.zeros((nx,nz))
w  = np.zeros((nx,nz))
wp = np.zeros((nx,nz))
wm = np.zeros((nx,nz))

def diff_sca():
    return

def diff_fulx():
    return

"""


"""
# check grid number 
for k in range(nz):
    for i in range(nx):
        mk=f'{i},{k}'
        plt.scatter(xx[i,k],zz[i,k],c='b',marker=rf'${i},{k}$',s=500)
plt.show()
"""
