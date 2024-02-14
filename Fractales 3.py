#########################################################
# Julia mountain landscape generation as a whole
# (Matplotlib Mesh plot)
#########################################################

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.figure as fg
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(azim=-120,elev=45) # set view orientation
ax.dist =4.0 # set viewpoint distance
ax.set_facecolor([0.25,0.3,0.7]) # set background color

n = 8
L = 2.0
dx = 0.0
dy = 0.0

M = 200

def f(Z):
    return np.e**(-np.abs(Z))

x = np.linspace(-L+dx,L+dx,M)
y = np.linspace(-L+dy,L+dy,M)
X,Y = np.meshgrid(x,y)
cX = -0.7454294
cY = 0
C = cX + 1j*cY
W = np.zeros((M,M))
Z = X + 1j*Y

for k in range(1,n+1):
    ZZ = Z**2 + C
    Z = ZZ
    W = f(Z)

ax.set_xlim(dx-L,dx+L)
ax.set_zlim(dy-L,dy+L)
ax.set_zlim(-1.3*L,2*L)
ax.axis("off")
ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap="coolwarm")

plt.show()