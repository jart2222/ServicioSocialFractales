import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Configuración de la escena
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor((0, 0, 0))  # Fondo negro

# Parámetros
R = 0.1  # Radio
L = 2  # Lado del área cuadrada
n = 200  # Número de píxeles por lado del área
N = 10  # Número de ciclos
Nr = 100  # Número de secciones
Th = -45  # Ángulo theta
Ph = 30  # Ángulo phi
# Definición de la función de Mandelbrot
def mandelbrot(p, q):
    X = 0
    Y = 0
    for i in range(1, N + 1):
        XX = X * X - Y * Y + p * L / n - 1
        YY = 2 * X * Y + q * L / n
        X = XX
        Y = YY
        if X * X + Y * Y > R:
            if X * X + Y * Y < R + 0.01:
                for k in range(Nr):
                    ax.plot([p], [q * np.cos(np.pi * k / Nr)], [q * np.sin(np.pi * k / Nr)], marker='o', markersize=1, color='yellow')

# Generación de la Mandelbrot 3D
for p in range(-n, n + 1):
    for q in range(-n, n + 1):
        mandelbrot(p, q)

# Configuración de la vista
ax.view_init(Th, Ph)

# Mostrar la figura
plt.show()
