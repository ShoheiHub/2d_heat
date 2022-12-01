import numpy as np
import matplotlib.pyplot as plt


from mod import *

if __name__=="__main__":
    time_num = int(time/dt)
    for t in range(1,time_num+1):
        print(dt*t)