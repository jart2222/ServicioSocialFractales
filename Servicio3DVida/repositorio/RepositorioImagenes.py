import os
import matplotlib.pyplot as plt
import cv2
from shutil import rmtree

class RepositorioImagenes:
    def __init__(self, nombre):
        self.dir='/home/jart/Documentos/Python/ServicioSocialFractales/Servicio3DVida/imagenes'
        self.nombreVideo=nombre


    def borrarImagenes(self):
        for f in os.listdir(self.dir):
            os.remove(os.path.join(self.dir, f))

    def crearImagen(self, xs, ys, zs, dim, etapaActual):
        # Plot
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.scatter(xs, ys, zs)
        ax.set_xlim(0, dim)
        ax.set_ylim(0, dim)
        ax.set_zlim(0, dim)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.savefig("imagenes/F_"+str(etapaActual)+".png")
        plt.close()

    def crearVideo(self, etapas):
        img_array = []
        for i in range(0, etapas):
            path = self.dir+"/F_" + str(i) + ".png"
            img = cv2.imread(path)
            img_array.append(img)
        alto, ancho = img.shape[:2]
        video = cv2.VideoWriter(self.nombreVideo+".mp4", cv2.VideoWriter.fourcc(*'mp4v'), 5, (ancho, alto))

        for i in range(len(img_array)):
            video.write(img_array[i])

        video.release()






