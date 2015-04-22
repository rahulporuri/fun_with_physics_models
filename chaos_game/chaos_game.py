#chaos game

import numpy as np
import matplotlib.pyplot as plt

#plot the edges:
v1 = [0,0]
v2 = [1,0]
v3 = [abs((v1[0]-v2[0])/2), np.sqrt(np.power((v1[0]-v2[0]),2) - np.power((v1[0]-v2[0])/2,2))]

plt.hold(True)
plt.plot(v1[0],v1[1])
plt.plot(v2[0],v2[1])
plt.plot(v3[0],v3[1])

N = 10^5   #number of points

#initial point
p = np.zeros([2,2])
p[0][0] = 0.5
p[0][1] = 0.1
plt.plot(p[0,0],p[0,1])

for ii in range(2,N):
    toss = np.random.choice([1,2,3])
    if (toss==1):
        p[1][0] = v1[0] + abs(p[0][0] - v1[0])/2
        p[1][1] = v1[1] + abs(p[0][1] - v1[1])/2
    elif (toss==2):
        p[1][0] = v2[0] - abs(p[0][0] - v2[0])/2
        p[1][1] = v2[1] + abs(p[0][1] - v2[1])/2
    elif (toss==3):
        p[1][0] = v3[0] - abs(p[0][0] - v3[0])/2
        p[1][1] = v3[1] - abs(p[0][1] - v3[1])/2

    plt.plot(p[1][0],p[1][1])
    
    p[0][0] = p[1][0]
    p[0][1] = p[1][1]
    
    p[1][0] = 0
    p[1][1] = 0
    
plt.show()
