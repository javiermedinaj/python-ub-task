# #4-Diseña un programa que, dado un número entero, determine si éste es el doble de un
# #número impar. (Ejemplo: 14 es el doble de 7, que es impar.)


# numero = int(input("Ingresa un número entero: "))


# es_par = numero % 2 == 0


# es_doble_de_impar = (numero // 2) % 2 != 0 if es_par else False


# if es_doble_de_impar:
#     print(numero, "es el doble de un número impar.")
# else:
#     print(numero, "no es el doble de un número impar.")

# #5 Escribir un programa que permita ingresar dos números enteros y escribirlos en orden creciente.

# numero1 = int(input("Ingresa el primer número entero: "))
# numero2 = int(input("Ingresa el segundo número entero: "))


# if numero1 < numero2:
#     print("Los números en orden creciente son:", numero1, ",", numero2)
# else:
#     print("Los números en orden creciente son:", numero2, ",", numero1)

# #6Ejercicio 6:Escribir un programa que permita ingresar tres números enteros y escribirlos en ordencreciente.
# # Pedir al usuario que ingrese tres números enteros
# numero1 = int(input("Ingresa el primer número entero: "))
# numero2 = int(input("Ingresa el segundo número entero: "))
# numero3 = int(input("Ingresa el tercer número entero: "))


# if numero1 <= numero2 <= numero3:
#     print("Los números en orden creciente son:", numero1, ",", numero2, ",", numero3)
# elif numero1 <= numero3 <= numero2:
#     print("Los números en orden creciente son:", numero1, ",", numero3, ",", numero2)
# elif numero2 <= numero1 <= numero3:
#     print("Los números en orden creciente son:", numero2, ",", numero1, ",", numero3)
# elif numero2 <= numero3 <= numero1:
#     print("Los números en orden creciente son:", numero2, ",", numero3, ",", numero1)
# elif numero3 <= numero1 <= numero2:
#     print("Los números en orden creciente son:", numero3, ",", numero1, ",", numero2)
# else:
#     print("Los números en orden creciente son:", numero3, ",", numero2, ",", numero1)


# # Ejercicio 7:Escribir un programa que permita ingresar el mes y el año y muestre la cantidad de díasdel mes. Por ejemplo, si el usuario ingresa mes 2 y año 2000, el programa debe responderque Febrero 2000 tiene 29 días. Si el usuario ingresa mes 3 y año 2005, el programa responderá que Marzo 2005 tiene 31 días.Pedir al usuario que ingrese el mes y el año
# mes = int(input("Ingresa el número del mes (1-12): "))
# año = int(input("Ingresa el año: "))


# dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
#     dias_por_mes[1] = 29


# dias = dias_por_mes[mes - 1]


# print("El mes", mes, "del año", año, "tiene", dias, "días.")

# #Ejercicio 8:
# #Escribir un programa que permita ingresar las coordenadas (x,y) de un punto en el plano y
# #verifique si el punto está dentro del círculo con centro en (0,0) y radio 10, o está fuera o en
# #la circunferencia. Mostrar los mensajes adecuados.
# # Pedir al usuario que ingrese las coordenadas (x, y) del punto
# x = float(input("Ingresa la coordenada x del punto: "))
# y = float(input("Ingresa la coordenada y del punto: "))


# distancia_al_centro = (x**2 + y**2)**0.5


# if distancia_al_centro < 10:
#     print("El punto está dentro del círculo.")
# elif distancia_al_centro == 10:
#     print("El punto está en la circunferencia del círculo.")
# else:
#     print("El punto está fuera del círculo.")
