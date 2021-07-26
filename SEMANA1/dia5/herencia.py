class vehiculo:
    def __init__(self,mar,km,col):
        self.marca=mar
        self.kilometraje=km
        self.color=col
    def encender():
        print("Encendiendo...")
        
class auto(vehiculo):
    def __init__(self,mar,km,col,cap):
        super().__init__(mar,km,col)
        self.capacidad=cap
    def encender(self):
        super().encender()
        print("Auto...")


ferrari=auto('ferrari','0','amarillo',2)
ferrari.encender()