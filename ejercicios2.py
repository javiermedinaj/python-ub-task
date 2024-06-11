# #Ejercicio 1:Implementa un programa que muestre todos los múltiplos de 6 entre 6 y 150, ambosinclusive.
# inicio = 6
# fin = 150
# for num in range(inicio, fin + 1):
#     if num % 6 == 0:
#         print(num)

# Ejercicio2:
# Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos inclusive).
# Si el usuario teclea un número fuera del rango válido, el programa solicitará nuevamente
# la introducción del valor cuantas veces sea menester.


# numero = int(input("Por favor, ingrese un número del 1 al 10: "))


# while numero < 1 or numero > 10:
#     numero = int(input("El número debe estar entre 1 y 10 (inclusive). Por favor, inténtalo nuevamente: "))

# print("Has ingresado el número", numero)


#  Ejercicio 3:

# Escribir un programa que muestre, de a diez números por línea y separados por un blanco,
# todos los números entre 100 y 1000 que sean divisibles por 5 y 6
# count = 0
# for num in range(100, 1001):
#     if num % 5 == 0 and num % 6 == 0:
#         print(num, end=" ")
#         count += 1
#         if count % 10 == 0:
#             print()


#ejercicio 4 y 5
def multiplicacion_rusa(n, m):
    resultado = 0
    pasos = []
    
    while m > 0:
        if m % 2 != 0:  # Si m es impar
            resultado += n
            pasos.append(f"* {n} | {m}")
        else:
            pasos.append(f"  {n} | {m}")
        n = n * 2
        m = m // 2
        
    return resultado, pasos

# Ejemplo de uso
n = 31
m = 27
producto, pasos = multiplicacion_rusa(n, m)

print(f"El resultado de {n} * {m} es: {producto}")
print("Pasos intermedios:")
for paso in pasos:
    print(paso)


# #ejercicio 6
# Diseñar un programa que genere una lista de números usando el siguiente proceso: 
# comenzar con un entero n que deberá ingresar el usuario. Si n es par, dividirlo por 2. Si n 
# es impar, multiplicarlo por 3 y sumarle 1. Repetir este proceso hasta que el nuevo valor 
# obtenido para n sea 1.
# Ejemplo, para n = 22, la secuencia que se obtiene es: 
# 22 11 33 17 52 26 13 40 20 10 5 16 8 4 2 1
# def generar_lista(n):
#     lista = [n]
#     while n != 1:
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3 * n + 1
#         lista.append(n)
#     return lista

# n = int(input("Ingrese un número entero positivo: "))
# lista_generada = generar_lista(n)
# print("Lista generada:", lista_generada)

