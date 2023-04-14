def esBisiesto(anio):
    return True if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else False

input_anio = int(input("Introduce un año:"))

if(esBisiesto(input_anio)):
    print("Es bisiesto")
else:
    print("No es bisiesto")
