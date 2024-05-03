import numpy as np
import random
from modelo.Automata3d import Automata3d

class RepositorioVecinos:
    def __init__(self, n):
        self.dim=n
        self.A = np.zeros((n, n, n))
        self.xs = []
        self.ys = []
        self.zs = []
        self.lAutomatas=[]
        self.etapaActual=0

    def poblarAzar(self):
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if (random.random() > 0.99):
                        self.xs.append(i)
                        self.ys.append(j)
                        self.zs.append(k)
                        self.A[i, j, k] = 1

    def nuevaEtapa(self):
        self.reiniciarParametros()

        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    automata = Automata3d(i, j, k, self.dim)
                    contador = self.contadorVecinos(automata)
                    if (self.A[i, j, k] == 0):
                        if (contador == 4):
                            self.xs.append(i)
                            self.ys.append(j)
                            self.zs.append(k)
                            print(str(automata) + " nace por que tiene: " + str(contador) + " vecinos")

                    else:
                        if (contador > 3 and contador < 5):
                            self.xs.append(i)
                            self.ys.append(j)
                            self.zs.append(k)
                            print(str(automata) + " se mantiene por que tiene: " + str(contador) + " vecinos")

                        else:
                            print(str(automata) + " muere por que tiene: " + str(contador) + " vecinos")


        self.nuevaMatriz()


    def nuevaMatriz(self):
        self.A = np.zeros((self.dim, self.dim, self.dim))
        for i in range(len(self.zs)):
            self.A[self.xs[i], self.ys[i], self.zs[i]] = 1

        self.etapaActual+=1
    def reiniciarParametros(self):
        self.xs = []
        self.ys = []
        self.zs = []

    def contadorVecinos(self, automata):
        contadorVecinos = 0
        if (self.A[automata.getXi(), automata.getYa(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getX(), automata.getYa(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getYa(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXi(), automata.getY(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getY(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXi(), automata.getYb(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getX(), automata.getYb(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getYb(), automata.getZa()] == 1):
            contadorVecinos = contadorVecinos + 1

        # =
        if (self.A[automata.getXi(), automata.getYa(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getX(), automata.getYa(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getYa(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXi(), automata.getY(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getY(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXi(), automata.getYb(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getX(), automata.getYb(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getYb(), automata.getZ()] == 1):
            contadorVecinos = contadorVecinos + 1

        # =
        if (self.A[automata.getXi(), automata.getYa(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getX(), automata.getYa(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getYa(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXi(), automata.getY(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getY(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXi(), automata.getYb(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getX(), automata.getYb(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        if (self.A[automata.getXd(), automata.getYb(), automata.getZb()] == 1):
            contadorVecinos = contadorVecinos + 1

        return contadorVecinos

