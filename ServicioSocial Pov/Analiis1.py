import numpy as np
import math
import matplotlib.pyplot as plt


R =   0.1
L = 2;    #set square area side
n = 50; #set number of pixels per area side
st = 1;     #set increment step
N = 40;       #set number of cycles
Th = -45;     #set rotation angles
Ph = 30;

K= np.zeros((2*n+1, 2*n+1, 2*n+1))


for p in range(-n, n, 1):
    IncX = p * L / n;
    for q in range(-n, n, 1):
        IncY = q * L / n;
        for r in range(-n, n, 1):
            IncZ = r * L / n;
            #print("p: ", p, "q: ", q, "r: ", r)
            #print(IncX, ", ", IncY, ", ",IncZ)
            X = 0;    # start MandX
            Y = 0;    # start MandY
            Z = 0;

            for k in range(0, N):
                XX = X*X - Y*Y - Z*Z + IncX;    #cycle MandX
                YY = 2*X*Y + IncY;    #cycle MandY
                ZZ = 2*X*Z + IncZ;     #cycle MandZ
                X = XX;
                Y = YY;
                Z = ZZ;
                W = X*X +Y*Y + Z*Z;
                #print("X: ",X,", Y: ", Y, ", Z: ", Z, ", W:", W)
                if W<R:
                    K[p + n][q + n][r + n] = k
                    #print((p + n))
                    #print((q + n))
                    #print((r + n))
                    #print("W:", W, " R: ", R)



Rnd_1 = np.random.default_rng(1153);
Rnd_2 = np.random.default_rng(553);
Rnd_3 = np.random.default_rng(876);
pp = 0;
qq = 0;
rr = 0;
xs =[]
ys = []
zs =[]

for i in range(0, pow(n, 3)):
    p = pp + st*pow(-1,int(n*Rnd_1.random()));
    q = qq + st*pow(-1,int(n*Rnd_2.random()));
    r = rr + st*pow(-1,int(n*Rnd_3.random()));

    if (abs(p)<n and abs(q)<n and abs(r)<n and K[p+n][q+n][r+n] > 0):
        xs.append(p)
        ys.append(q)
        zs.append(r)
        pp = p;
        qq = q;
        rr = r;





# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
