import numpy as np
import math
import matplotlib.pyplot as plt
import random
from modelo.Automata3d import Automata3d
import cv2
from shutil import rmtree
import os

dir = '/home/jart/Documentos/Python/ServicioSocialFractales/Servicio3DVida/imagenes'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))


n = 100
etapas=50

A = np.zeros((n, n, n))
xs = []
ys = []
zs = []
automatas = []
img_array=[]



def contadorVecinos(automata):
    contadorVecinos=0
    if(A[automata.getXi(), automata.getYa(), automata.getZa()]==1):
        contadorVecinos=contadorVecinos+1

    if (A[automata.getX(), automata.getYa(), automata.getZa()] == 1):
        contadorVecinos=contadorVecinos+1

    if (A[automata.getXd(), automata.getYa(), automata.getZa()] == 1):
        contadorVecinos=contadorVecinos+1

    if (A[automata.getXi(), automata.getY(), automata.getZa()] == 1):
        contadorVecinos=contadorVecinos+1

    if (A[automata.getXd(), automata.getY(), automata.getZa()] == 1):
        contadorVecinos=contadorVecinos+1

    if (A[automata.getXi(), automata.getYb(), automata.getZa()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getX(), automata.getYb(), automata.getZa()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXd(), automata.getYb(), automata.getZa()] == 1):
        contadorVecinos = contadorVecinos + 1

    #=
    if (A[automata.getXi(), automata.getYa(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getX(), automata.getYa(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXd(), automata.getYa(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXi(), automata.getY(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXd(), automata.getY(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXi(), automata.getYb(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getX(), automata.getYb(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXd(), automata.getYb(), automata.getZ()] == 1):
        contadorVecinos = contadorVecinos + 1

    # =
    if (A[automata.getXi(), automata.getYa(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getX(), automata.getYa(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXd(), automata.getYa(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXi(), automata.getY(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXd(), automata.getY(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXi(), automata.getYb(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getX(), automata.getYb(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    if (A[automata.getXd(), automata.getYb(), automata.getZb()] == 1):
        contadorVecinos = contadorVecinos + 1

    return contadorVecinos

#####################################

for i in range(n):
    for j in range(n):
        for k in range(n):
            if (random.random() > 0.99):
                xs.append(i)
                ys.append(j)
                zs.append(k)
                A[i, j, k] = 1;

xs.append(54)
ys.append(55)
zs.append(55)
A[54,55,55]=1;

xs.append(55)
ys.append(55)
zs.append(54)
A[55,55,54]=1;

xs.append(56)
ys.append(55)
zs.append(55)
A[56,55,55]=1;



# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)
ax.set_xlim(0, n)
ax.set_ylim(0, n)
ax.set_zlim(0, n)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig("imagenes/F0.png")
plt.close()



##########
for f in range(1, etapas):
    print('etapa:'+str(f))
    nXs = []
    nYs = []
    nZs = []

    for i in range(n):
        for j in range(n):
            for k in range(n):
                automata = Automata3d(i, j, k, n)
                contador = contadorVecinos(automata)

                if(A[i, j, k] == 0):
                    if(contador>2):
                        nXs.append(i)
                        nYs.append(j)
                        nZs.append(k)
                        print(str(automata)+ " nace por que tiene: "+str(contador)+ " vecinos")

                else:
                    if(contador>2 and contador<4):
                        nXs.append(i)
                        nYs.append(j)
                        nZs.append(k)
                        print(str(automata)+ " se mantiene por que tiene: "+str(contador)+ " vecinos")
                    else:
                        print(str(automata)+ " muere por que tiene: "+str(contador)+ " vecinos")



    A = np.zeros((n, n, n))
    xs = nXs
    ys = nYs
    zs = nZs
    print(len(xs))
    automatas = []

    # Plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.scatter(xs, ys, zs)
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_zlim(0, n)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.savefig("imagenes/F"+str(f)+".png")
    plt.close()

    for i in range(len(zs)):
        A[xs[i], ys[i], zs[i]] = 1;

    xs = []
    ys = []
    zs = []



#Video

img_array=[]
for i in range(0, etapas):
    path= "/home/jart/Documentos/Python/ServicioSocialFractales/Servicio3DVida/imagenes/F"+str(i)+".png"
    img= cv2.imread(path)
    img_array.append(img)

alto, ancho= img.shape[:2]

video= cv2.VideoWriter("Juego3D.mp4", cv2.VideoWriter.fourcc(*'mp4v'), 5, (ancho, alto))

for i in range(len(img_array)):
    video.write(img_array[i])

video.release()

















