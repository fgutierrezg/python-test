from functools import reduce

def es_impar(numero):
    return numero % 2 != 0

def sumar(a, b):
    return a + b

numeros = input("Introduce los numeros separados por coma:")

lista_numeros = numeros.split(",")
lista_numeros = list(map(int, set(lista_numeros)))

numeros_impares = sorted(list(filter(es_impar, lista_numeros)))

suma_impares = reduce(sumar, numeros_impares)

print("La suma de los impares es:", suma_impares)