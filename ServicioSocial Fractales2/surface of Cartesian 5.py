import numpy as np
import matplotlib.pyplot as plt

# Definir función Mandelbrot
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Configuración de la imagen
xmin, xmax, ymin, ymax = -2, 2, -2, 2
width, height = 400, 400
max_iter = 30

# Generación de la imagen
img = np.zeros((height, width))
for x in range(width):
    for y in range(height):
        cx = np.linspace(xmin, xmax, width)[x]
        cy = np.linspace(ymin, ymax, height)[y]
        c = complex(cx, cy)
        img[y, x] = mandelbrot(c, max_iter)

# Visualización de la imagen
plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap='hot', aspect='auto')
plt.colorbar(label='Iteraciones')
plt.title('Conjunto de Mandelbrot (2D)')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.show()
