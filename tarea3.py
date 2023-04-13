peso = int(input("Introduce tu peso(kgs): "))
estatura = float(input("Introduce tu estatura(mts): "))

imcvar = peso / (estatura * estatura)
print("Tu IMC es: " + str(imcvar))
