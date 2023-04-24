import pickle
class Vehiculo():
    marca = ""
    modelo = ""
    anio = 0

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.marca = modelo
        self.marca = anio

    def mostrarAtributos(self):
        print("Marca ", self.marca)
        print("Modelo ", self.modelo)
        print("Anio ", self.anio)


v1 = Vehiculo("Honda", "Civic", 2005)

f = open('datos.bin','wb')

## Serializando
pickle.dump(v1,f)
f.close()

##Des serialializar

f2 = open('datos.bin','rb')
v2 = pickle.load(f2)
f2.close()

print(v2.mostrarAtributos())
