class Automata3d():
    def __init__(self, x, y, z, n):
        self.x=x
        self.y=y
        self.z=z
        self.dim=n-1

    def getX(self):
        return self.x;

    def getY(self):
        return self.y;

    def getZ(self):
        return self.z;

    def getXi(self):
        if(self.x==0):
            return self.dim
        else:
            return self.x-1

    def getXd(self):
        if(self.x==(self.dim)):
            return 0
        else:
            return self.x+1

    def getYa(self):
        if (self.y == 0):
            return self.dim
        else:
            return self.y-1

    def getYb(self):
        if (self.y == (self.dim)):
            return 0
        else:
            return self.y+1

    def getZa(self):
        if (self.z == 0):
            return self.dim
        else:
            return self.z-1

    def getZb(self):
        if (self.z == (self.dim)):
            return 0
        else:
            return self.z+1
    def __str__(self):
        return "A("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"





