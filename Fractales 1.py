import matplotlib.pyplot as plt       # import matplotlib modules
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.figure as fg
from matplotlib import cm    # import color maps module
import numpy as np   # import numpy module

fig = plt.figure()   # set 3D figure environment
ax = fig.add_subplot(111, projection='3d')
ax.view_init(azim=-120,elev=45) # set view orientation
ax.dist =5.0 # set viewpoint distance
ax.set_facecolor([.1,0.0,0.0]) # set ground color

n = 8     # set number of cycles
dx = -0.7    # set initial x parameter shift
dy = 0.0     # set initial y parameter shift
L = 1.5    # set square area side
M = 200  # set side number of pixels

def f(Z):   # def scale damping of the elevation function
    return np.e**(-np.abs(Z))

x = np.linspace(-L+dx,L+dx,M)   # x variable array
y = np.linspace(-L+dy,L+dy,M)    # y variable array

X,Y = np.meshgrid(x,y)      # square area grid
Z = np.zeros(M)        # complex plane starting points area
W = np.zeros((M,M))    # zero matrix of elevation values
C = X + 1j*Y         # complex plane area

for k in range(1,n+1):       # recursion cycle
   ZZ = Z**2 + C
   Z = ZZ
   W = f(Z)      # smoothed sum moduls

ax.set_xlim(dx-L,dx+L)     # set x axis limits
ax.set_zlim(dy-L,dy+L)     # set y axis limits
ax.set_zlim(-L,2*L)     # set z axis limits
ax.axis("off")    # do not plot axes
ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap="pink")
# plot surface as a whole
plt.show() # show plot