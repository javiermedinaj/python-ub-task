# # Escribir una función que reciba una cadena que contiene un número entero largo y 
# # devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe 
# # ’1234567890’, debe devolver ’1.234.567.890’
# def separar_miles(numero):
#     separado = ""
#     while len(numero) > 3:
#         separado = "." + numero[-3:] + separado
#         numero = numero[:-3]
#     separado = numero + separado
#     return separado

# numero = input("Ingrese un número entero largo: ")
# numero_con_separacion = separar_miles(numero)
# print("Número con separación de miles:", numero_con_separacion)




# # Ejercicio 2:
# # Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por
# # ejemplo, "amor", "chino" e "himno" son palabras "alfabéticas". Diseña un programa que lea
# # una palabra y nos diga si es alfabética o no
# def es_alfabetica(palabra):
#     for i in range(len(palabra) - 1):
#         if palabra[i] > palabra[i + 1]:
#             return False
#     return True

# palabra = input("Ingrese una palabra: ")

# if es_alfabetica(palabra):
#     print("La palabra", palabra, "es alfabética.".format(palabra))
# else:
#     print("La palabra", palabra, "no es alfabética.".format(palabra))


# Ejercicio 3:
# Hay un tipo de pasatiempos que propone descifrar un texto del que se han suprimido
# las vocales. Por ejemplo, el texto ".n .j.mpl. d. p.s.t..mp.s", se descifra sustituyendo cada
# punto con una vocal del texto. La solución es "un ejemplo de pasatiempos". Diseña un
# programa que ayude al creador de pasatiempos. El programa recibirá una cadena y 
# mostrará otra en la que cada vocal ha sido reemplazada por un punto

# def reemplazar_vocales():
#     cadena = input("Ingrese una cadena de texto: ")
#     vocales = ['a', 'e', 'i', 'o', 'u']
#     nueva_cadena = ""
#     for letra in cadena:
#         if letra.lower() in vocales:
#             nueva_cadena += '.'
#         else:
#             nueva_cadena += letra
#     return nueva_cadena

# #el operador += se utiliza para concatenar una cadena con otra cadena o con un valor entero o flotante 

# cadena_reemplazada = reemplazar_vocales()
# print("Cadena con vocales reemplazadas:", cadena_reemplazada)

# Haz un programa que lea dos cadenas que representen sendos números binarios. A
# continuación, el programa mostrará el número binario que resulta de sumar ambos (y que 
# será otra cadena). Si, por ejemplo, el usuario introduce las cadenas ’100’ y ’111’, el 
# programa mostrará como resultado la cadena ’1011’.
# Nota: El procedimiento de suma con acarreo que implementes deberá trabajar 
# directamente con la representación binaria leída
# def sumar_binarios(binario1, binario2):
#     # Convertir los números binarios a enteros
#     num1 = int(binario1, 2)
#     num2 = int(binario2, 2)
    
#     # Sumar los números enteros
#     suma = num1 + num2
    
#     # Convertir la suma de nuevo a binario
#     binario_suma = bin(suma)[2:]
    
#     return binario_suma

# binario1 = input("Ingrese el primer número binario: ")
# binario2 = input("Ingrese el segundo número binario: ")

# resultado = sumar_binarios(binario1, binario2)
# print("Resultado de la suma binaria:", resultado)

# def sumar_binarios(binario1, binario2):
#     # Convertir los números binarios a enteros
#     num1 = int(binario1, 2)
#     num2 = int(binario2, 2)
    
#     # Sumar los números enteros
#     suma = num1 + num2
    
#     # Convertir la suma de nuevo a binario
#     binario_suma = bin(suma)[2:]
    
#     return binario_suma

# def validar_binario(numero_binario):
#     # Verificar si el número ingresado es un binario válido
#     return all(bit in '01' for bit in numero_binario)

# binario1 = input("Ingrese el primer número binario: ")
# while not validar_binario(binario1):
#     print("Ingrese un número binario válido (solo 0 y 1).")
#     binario1 = input("Ingrese el primer número binario: ")

# binario2 = input("Ingrese el segundo número binario: ")
# while not validar_binario(binario2):
#     print("Ingrese un número binario válido (solo 0 y 1).")
#     binario2 = input("Ingrese el segundo número binario: ")

# resultado = sumar_binarios(binario1, binario2)
# print("Resultado de la suma binaria:", resultado)


# Ejercicio 5:
# Escribir un programa que verifique si un string es una password correcta. Las reglas para 
# determinar si es correcta son:
# Debe tener como mínimo 8 caracteres.
#  Sólo puede tener letras y dígitos.
# Como mínimo debe tener dos dígito
# def verificar_password(password):
#     if len(password) < 8:
#         return False
    
#     digit_count = 0
#     for char in password:
#         if not char.isalnum():
#             return False
#         if char.isdigit():
#             digit_count += 1
    
#     if digit_count < 2:
#         return False
    
#     return True

# password = input("Ingrese una contraseña: ")

# if verificar_password(password):
#     print("La contraseña es correcta.")
# else:
#     print("La contraseña no cumple con los requisitos.")


# # Ejercicio 6:
# Escribir un programa que retorne el número que le corresponde a una letra en mayúscula  
# de acuerdo al teclado telefónico (ver figura):
# def teclado_telefonico(letra):
#     letras = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#     letra_mayuscula = letra.upper()
#     for i, conjunto_letras in enumerate(letras):
#         if letra_mayuscula in conjunto_letras:
#             return i + 2
#     return "No se encontró la letra en el teclado telefónico."

# letra = input("Ingrese una letra en mayúscula: ")

# numero = teclado_telefonico(letra)

# print("El número que le corresponde a la letra", letra, "en el teclado telefónico es", numero)


# Ejercicio 7:
# Escribir un programa que ingrese un número telefónico como un string y convierta los
# caracteres a el dígito correspondiente, ejemplo:
#                       1-800-FLOWERS  ---> 1-800-3569377
def convertir_a_numero_telefonico(telefono):
    letras_telefono = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    numero_telefonico = ''
    
    for caracter in telefono:
        for conjunto_letras, numero in zip(letras_telefono, range(2, 10)):
            if caracter.upper() in conjunto_letras:
                numero_telefonico += str(numero)
                break
        else:
            numero_telefonico += caracter
    
    return numero_telefonico

telefono = input("Ingrese el número telefónico como un string: ")

numero_telefonico_convertido = convertir_a_numero_telefonico(telefono)
print("El número telefónico convertido es:", numero_telefonico_convertido)


# Ejercicio 8:
# Un ISBN-10 (International Standard Book Number) consiste de 10 dígitos: 
# d1d2d3d4d5d6d7d8d9d10.
# El último dígito, d10, es el dígito verificador que se calcula como sigue:
# Si el dígito verificador es 10, el último dígito es x, de acuerdo a las normas ISBN. Escribir 
# un programa que permita ingresar los primeros 9 dígitos como una cadena y muestre el 
# número ISBN.
# Ejemplo:       013601267 ---> 0136012671
#                       013031997 ---> 013601267X
def calcular_digito_verificador(primeros_nueve_digitos):
    suma = 0
    for i in range(9):
        suma += int(primeros_nueve_digitos[i]) * (i + 1)
    digito_verificador = suma % 11
    if digito_verificador == 10:
        return primeros_nueve_digitos + 'X'
    else:
        return primeros_nueve_digitos + str(digito_verificador)

primeros_nueve_digitos = input("Ingrese los primeros 9 dígitos del ISBN-10: ")
isbn = calcular_digito_verificador(primeros_nueve_digitos)
print("El número ISBN completo es:", isbn)