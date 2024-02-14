import matplotlib.pyplot as plt       # import matplotlib modules
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.figure as fg
from matplotlib import cm    # import color maps module
import numpy as np    # import numpy module

fig = plt.figure()   # set 3D figure environment
ax = fig.add_subplot(111, projection='3d')
ax.view_init(azim=120,elev=45) # set view orientation
ax.dist = 4.5 # set viewpoint distance
ax.set_facecolor([0.0,0.3,0.6]) # set background color

n = 16      # set number of cycles
dx = -0.1     # set initial x parameter shift
dy = 0.0      # set initial y parameter shift
L = 1.7    # set square area side
M = 200   # set side number of pixels

def f(Z):      # def scale damping of the elevation function
    return np.e**(-np.abs(Z))

x = np.linspace(-L+dx,L+dx,M)     # x variable array
y = np.linspace(-L+dy,L+dy,M)     # y variable array
X,Y = np.meshgrid(x,y)     # square area grid
cX = -0.7454294   # C parameter real part value
cY = 0   # C parameter imaginary part value
C = cX + 1j*cY      # complex C matrix
W = np.zeros((M,M))     # zero matrix of elevation values
Z = X + 1j*Y     # complex plane area

for k in range(1,n+1):     # recursion cycle
   ZZ = Z**2 + C
   Z = ZZ
   W = f(Z)

ax.set_xlim(dx-L,dx+L)    # set x axis limits
ax.set_zlim(dy-L,dy+L)    # set y axis limits
ax.set_zlim(-.8*L,1.5*L)    # set z axis limits
ax.axis("off")    # do not plot axes
ax.contourf3D(X, Y, W, 2*n, cmap="pink")   # make contour plot
plt.show() # show plot