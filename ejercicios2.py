# #Ejercicio 1:Implementa un programa que muestre todos los múltiplos de 6 entre 6 y 150, ambosinclusive.


# Ejercicio2:
# Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos inclusive).
# Si el usuario teclea un número fuera del rango válido, el programa solicitará nuevamente
# la introducción del valor cuantas veces sea menester.


# numero = int(input("Por favor, ingrese un número del 1 al 10: "))


# while numero < 1 or numero > 10:
#     numero = int(input("El número debe estar entre 1 y 10 (inclusive). Por favor, inténtalo nuevamente: "))

# print("¡ Has ingresado el número", numero)


#  Ejercicio 3:

# Escribir un programa que muestre, de a diez números por línea y separados por un blanco,
# todos los números entre 100 y 1000 que sean divisibles por 5 y 6
for i in range(100, 1001):
    if i % 5 == 0 and i % 6 == 0:
        print(i)
        if i % 10 == 0:
            print()


