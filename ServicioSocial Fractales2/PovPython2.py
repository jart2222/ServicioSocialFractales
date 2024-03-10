import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

plt.style.use('_mpl-gallery')

u=np.linspace(0,2*np.pi,100)

v=np.linspace(0,2*np.pi,100)
u,v=np.meshgrid(u,v)

a = 2
b = 9
X = (b + a*np.cos(u)) * np.cos(v)
Y = (b + a*np.cos(u)) * np.sin(v)
Z = a * np.sin(u)

fig = plt.figure(figsize=(6,6),dpi=130)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_zlim(-10,10)
ax.set_box_aspect((1,1,1))

ax.plot_surface(X, Y, Z,alpha=0.8, cmap=cm.Wistia)
plt.show()