###################################
# Random sphere generation
# by Paramteric equations
# (matplotlib module)
###################################

from mpl_toolkits import mplot3d   # import matplotlib module
import matplotlib.pyplot as plt    # import pylot module
import numpy as np    # import numpy module
import random as rd   # import random module
from matplotlib import cm


r = 6.0   # set radius value
n = 100   # set number of cycles
theta = np.linspace(0.0, 2*np.pi, n)   # set theta co-ordinate array
phi = np.linspace(0.0, np.pi, n)   # set phi co-ordinate array
theta, phi = np.meshgrid(theta, phi)  # set theta,phi grid

# spherical to Cartesian transformations
X = r * np.sin(theta)*np.sin(phi)
Y = r * np.cos(theta)*np.sin(phi)
Z = r*np.cos(phi)


fig = plt.figure(figsize=(6,6),dpi=130)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.set_xlim(-4.5,4.5)
ax.set_ylim(-5.0,5.0)
ax.set_zlim(-5.0,40)
ax.set_box_aspect((1,1,1))

ax.plot_surface(X, Y, Z,alpha=0.8, cmap=cm.Wistia)
plt.show()

