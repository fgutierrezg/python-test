class Vehiculo:
    color = "Amarillo"
    ruedas = 5
    puertas = 4

class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 1.4
    def __init__(self):
        super().__init__()

car = Coche()
print(car.color)
print(car.ruedas)
print(car.puertas)
print(car.velocidad)
print(car.cilindrada)
