#################################
# whole 3D surface generation
# by Cartesian equation
# (matplotlib module)
#################################

import matplotlib.pyplot as plt   # import matplotlib pylot module
import numpy as np   # import numpy module

plt.style.use("dark_background") # set black background color

R = 4.0 # set radius value
X = np.arange(-2*np.pi, 2*np.pi, 0.1)  # set x co-ordinate array values
Y = np.arange(-2*np.pi, 2*np.pi, 0.1)  # set y co-ordinate array values
X, Y = np.meshgrid(X, Y)  # set xy grid
Z = np.e**(-.05*(X**2+Y**2))*np.cos(np.sqrt(X**2 + Y**2)) # set z function of x,y

fig = plt.figure()    # define 3D plot and axes
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z)   # plot surface as a whole
ax.set_zlim(-.3, 1.0)   # set z axis limits
ax.axis("off")  # do not plot co-ordinate axes
plt.show()