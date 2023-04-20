class Alumno():
    nota = 1
    nombre = "Sin nombre"

    def mostrarAtributos(self, nombre, nota):
        print("Alumno ", nombre)
        print("Nota",nota)
        if(nota >= 4):
            print("Aprueba")
        else:
            print("No aprueba")

estudiante = Alumno()

estudiante.mostrarAtributos("Gerardo",4.1)
