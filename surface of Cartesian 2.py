
####################################
# whole sphere generation
# by paramteric equations
# (matplotlib module)
####################################

from mpl_toolkits.mplot3d import Axes3D   # import matplotlib module
import matplotlib.pyplot as plt  # import matplotlib module
import numpy as np # import numpy module
from matplotlib import cm


angle = np.linspace(0, 2 * np.pi, 32)  # define cylindrical co-ordinates
theta, phi = np.meshgrid(angle, angle)   # set theta, phi grid

R = 1.0     # set radius value
X = R * np.cos(phi) * np.cos(theta)   # evaluate x co-ordinate array
Y = R * np.cos(phi) * np.sin(theta)    # evaluate y co-ordinate array
Z = R * np.sin(phi)     # evaluate z co-ordinate array values

plt.style.use("dark_background")   # set black background color

fig = plt.figure()     # define 3D plot and axes
ax = fig.add_subplot(projection = '3d')

ax.set_xlim3d(-1, 1)     # set x axis limits
ax.set_ylim3d(-1, 1)     # set y axis limits
ax.set_zlim3d(-1, 1)     # set z axis limits

# plot surface as a whole
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

ax.axis("off")     # do not plot co-ordinate axes
plt.show()   # show surface a a whole