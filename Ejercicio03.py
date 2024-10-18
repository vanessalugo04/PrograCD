# Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
# inserte en un alista los pares y en otr alos impares
# Imprimir ambas listas y el tamaño de las mismas
import random
numeros = [random.randint(1, 1000) for i in range(100)]
pares = [num for num in numeros if num %2 == 0]
impares = [num for num in numeros if num %2 != 0]

tamp = len(pares)
tamimp = len(impares)

print(f"Los numeros pares son: {pares} \nLa cantidad es: {tamp}")
print(f"Los numeros impares son: {impares}\nLa cantidad es: {tamimp}")