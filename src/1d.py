import numpy as np
import matplotlib.pyplot as plt

nx = 5

Lx = 1

dt = 0.1
tmx=10

# set-up parameter
nu = 1.e-6

# set-up array
x = np.linspace(0,Lx,nx+1)


# scalar <'m':t-1, ' ':t, 'p':t+1>
t  = np.zeros(nx)
tp = np.zeros(nx)
tm = np.zeros(nx)
# flux <'m':t-1, ' ':t, 'p':t+1>
u  = np.zeros(nx+1)
up = np.zeros(nx+1)
um = np.zeros(nx+1)

def diff_sca():
    return

def diff_flux(x,u,i):
    print(x)
    return

diff_flux(1,1,1)


"""
# check grid number 
for k in range(nz):
    for i in range(nx):
        mk=f'{i},{k}'
        plt.scatter(xx[i,k],zz[i,k],c='b',marker=rf'${i},{k}$',s=500)
plt.show()
"""
