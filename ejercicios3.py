# Escribir una función que reciba una cadena que contiene un número entero largo y 
# devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe 
# ’1234567890’, debe devolver ’1.234.567.890’
def separar_miles(numero):
    separado = ""
    while len(numero) > 3:
        separado = "." + numero[-3:] + separado
        numero = numero[:-3]
    separado = numero + separado
    return separado

numero = input("Ingrese un número entero largo: ")
numero_con_separacion = separar_miles(numero)
print("Número con separación de miles:", numero_con_separacion)


# Ejercicio 2:
# Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por
# ejemplo, "amor", "chino" e "himno" son palabras "alfabéticas". Diseña un programa que lea
# una palabra y nos diga si es alfabética o no
def es_alfabetica(palabra):
    for i in range(len(palabra) - 1):
        if palabra[i] > palabra[i + 1]:
            return False
    return True

palabra = input("Ingrese una palabra: ")

if es_alfabetica(palabra):
    print("La palabra", palabra, "es alfabética.".format(palabra))
else:
    print("La palabra", palabra, "no es alfabética.".format(palabra))
