import numpy as np
import matplotlib.pyplot as plt


from mod import *

if __name__=="__main__":
    # I.C.
    print(t)
    t[:]=1
    print(t)

    
    time_num = int(time/dt)
    for t in range(1,time_num+1):
        for k in range(nz):
            for i in range(nx):
                
                continue


    #plt.scatter(xx,zz,color="y")
    #plt.scatter(xxu,zzu,color="b",marker=f"$u$")
    #plt.scatter(xxw,zzw,color="g",marker=f"$w$")
    #plt.scatter(xxs,zzs,color="r",marker=f"$T$")
    #plt.show()