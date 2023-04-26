paises = input("Introduce los paises separados por coma:")

lista_paises = paises.split(",")
lista_paises = list(set(lista_paises))

print(sorted(lista_paises))

