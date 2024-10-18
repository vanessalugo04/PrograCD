import string
import random

minusculas_ascii = string.ascii_lowercase
print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
print(mayusculas_ascii)

numeros = string.digits
print(numeros)


def generarPassword(n):
    # Escribe una funcion que genere un password aleatorio de n caracteres
    # el password debe contener letras mayusculas minusculas y numeros
    password = [random.choice(minusculas_ascii), random.choice(mayusculas_ascii), random.choice(numeros)]
    todos_caracteres = minusculas_ascii + mayusculas_ascii + numeros
    password += random.choices(todos_caracteres)
    
    return ''.join(password)


for i in range(10, 20):
    print(generarPassword(i))