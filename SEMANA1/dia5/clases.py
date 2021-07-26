class Rectangulo:
    
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    
    def area(self):
        return self.ancho*self.alto
    
    
class FiguraGeometrica(Rectangulo,Cuadrado)
r=Rectangulo(20,30)
areaR=r.area()
print("Area del rectangulo : "+str(areaR))