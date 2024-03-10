from mpl_toolkits.mplot3d import Axes3D # import matplotlib module
import matplotlib.pyplot as plt      # import matplotlib module
import numpy as np     # import numpy module

angle = np.linspace(0, 2 * np.pi, 32)  # define cylindrical co-ordinates
theta, phi = np.meshgrid(angle, angle) # set theta, phi grid
r, R = .25, 1.
X = (R + r * np.cos(phi)) * np.cos(theta)  # evaluate x co-ordinate array
Y = (R + r * np.cos(phi)) * np.sin(theta)   # evaluate y co-ordinate array
Z = r * np.sin(phi)

plt.style.use("dark_background")    # set black background color

fig = plt.figure()    # define 3D plot and axes
ax = fig.add_subplot(projection = '3d')
ax.set_xlim3d(-1, 1)     # set x axis limits
ax.set_ylim3d(-1, 1)     # set y axis limits
ax.set_zlim3d(-1, 1)     # set z axis limits

# plot surface as a whole
ax.plot_surface(X, Y, Z, color = 'cyan', rstride = 1,cstride = 1)

ax.axis('off')   # do not plot co-ordinate axes
plt.show()  # show surface as a whole
