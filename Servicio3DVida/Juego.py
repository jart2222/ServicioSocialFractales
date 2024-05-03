from repositorio.RepositorioImagenes import RepositorioImagenes
from repositorio.RepositorioVecinos import RepositorioVecinos

rImagenes=RepositorioImagenes("JuegoDeLaVida5")
rImagenes.borrarImagenes()
rVecinos=RepositorioVecinos(100)

rVecinos.poblarAzar()

rImagenes.crearImagen(rVecinos.xs, rVecinos.ys, rVecinos.zs, rVecinos.dim, rVecinos.etapaActual)

for i in range(1,200):
    print("Etapa: "+str(i))
    rVecinos.nuevaEtapa()
    rImagenes.crearImagen(rVecinos.xs, rVecinos.ys, rVecinos.zs, rVecinos.dim, rVecinos.etapaActual)

rImagenes.crearVideo(rVecinos.etapaActual+1)


















