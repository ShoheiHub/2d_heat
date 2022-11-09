import numpy as np

# import para mod
from para import *
    
 
def diff(x=None,y=None):
    print('diffusion')
    im = np.shape(x)[0]
    jm = np.shape(y)[1]

    im = np.shape(x)[0]
    jm = np.shape(y)[1]
    print(im,jm)
    for j in range(1,im-1):
        for i in range(1,jm-1):
            #dtdx2 = dt / (dx[i]**2)
            #dtdy2 = dt / (dy[j]**2)
            #print(f'i={i},j={j},{dx[i]},{dy[j]}')
            #fxx = x[i+1,j  ,0] - 2*x[i,j,0] + x[i-1,j  ,0]
            #fxy = x[i  ,j+1,0] - 2*x[i,j,0] + x[i  ,j-1,0]
            #fyx = y[i+1,j  ,0] - 2*y[i,j,0] + y[i-1,j  ,0]
            #fyy = y[i  ,j+1,0] - 2*y[i,j,0] + y[i  ,j-1,0]

            #x[i,j,1] = x[i,j,0] + nu*( dtdx2*fxx + dtdy2*fxy )
            #y[i,j,1] = y[i,j,0] + nu*( dtdx2*fyx + dtdy2*fyy )
    return x, y

