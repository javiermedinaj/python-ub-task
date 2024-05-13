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
# #                       1-800-FLOWERS  ---> 1-800-3569377
# def convertir_a_numero_telefonico(telefono):
#     letras_telefono = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#     numero_telefonico = ''

#     for caracter in telefono:
#         for conjunto_letras, numero in zip(letras_telefono, range(2, 10)):
#             if caracter.upper() in conjunto_letras:
#                 numero_telefonico += str(numero)
#                 break
#         else:
#             numero_telefonico += caracter

#     return numero_telefonico

# telefono = input("Ingrese el número telefónico como un string: ")

# numero_telefonico_convertido = convertir_a_numero_telefonico(telefono)
# print("El número telefónico convertido es:", numero_telefonico_convertido)


# Ejercicio 8:
# Un ISBN-10 (International Standard Book Number) consiste de 10 dígitos:
# d1d2d3d4d5d6d7d8d9d10.
# El último dígito, d10, es el dígito verificador que se calcula como sigue:
# Si el dígito verificador es 10, el último dígito es x, de acuerdo a las normas ISBN. Escribir
# un programa que permita ingresar los primeros 9 dígitos como una cadena y muestre el
# número ISBN.
# Ejemplo:       013601267 ---> 0136012671
#                       013031997 ---> 013601267X
# def calcular_digito_verificador(primeros_nueve_digitos):
#     suma = 0
#     for i in range(9):
#         suma += int(primeros_nueve_digitos[i]) * (i + 1)
#     digito_verificador = suma % 11
#     if digito_verificador == 10:
#         return primeros_nueve_digitos + 'X'
#     else:
#         return primeros_nueve_digitos + str(digito_verificador)


# primeros_nueve_digitos = input("Ingrese los primeros 9 dígitos del ISBN-10: ")
# isbn = calcular_digito_verificador(primeros_nueve_digitos)
# print("El número ISBN completo es:", isbn)
      

        #FALTA HACER
# Ejercicio 9:
# ISBN-13 es un nuevo estandar para identificar libros. Usa 13 dígitos: 
# d1d2d3d4d5d6d7d8d9d10d11d12d13 .
# El último dígito, es el dígito verificador y se calcula con la siguiente fórmula:
# Si el dígito verificador es 10 se reemplaza por 0. El programa deberá permitir ingresar un 
# número como un string y mostrar el ISBN-13, ejemplo:
# 978013213080 ---> 9780132130806
         #FALTA HACER

# Ejercicio 10:
# Escribir una programa que permita ingresar un texto y un caracter e imprima la palabra 
# más larga en la que se encuentra ese carácter
# def encontrar_palabra_mas_larga(texto, caracter):
#     palabras = texto.split()
#     palabras_con_caracter = [palabra for palabra in palabras if caracter in palabra]
#     if palabras_con_caracter:
#         palabra_mas_larga = max(palabras_con_caracter, key=len)
#         return palabra_mas_larga
#     else:
#         return "No se encontró ninguna palabra con el caracter especificado."

# texto = input("Ingrese un texto: ")
# caracter = input("Ingrese un caracter: ")

# palabra_mas_larga = encontrar_palabra_mas_larga(texto, caracter)
# print("La palabra más larga que contiene el caracter es:", palabra_mas_larga)


#ejercicio 11
# La ley de Chargaff dice que en el ADN de un organismo la cantidad de Adenina es la 
# misma que la de Tiamina, y la de Citosina es la misma que la de Guanina. Dada una 
# secuencia de nucleótidos del estilo de ATTACCAGTACA... podemos comprobar si cumple
# dicha ley de la siguiente forma:
# Contamos la cantidad de A, T, C y G presentes en la cadena y calculamos los coeficientes
# donde NX indica la cantidad de nucleótidos del tipo X presentes en la secuencia.
# Partiremos de una cadena que contiene una cantidad indeterminada de caracteres, que 
# # solo pueden ser A, T, G ó C. Calcula a partir de dicha cadena los coeficientes a y c
# def calcular_coeficientes(secuencia):
#     a = secuencia.count('A')
#     t = secuencia.count('T')
#     c = secuencia.count('C')
#     g = secuencia.count('G')

#     return a, c

# secuencia = input("Ingrese la secuencia de nucleótidos: ")
# coeficientes = calcular_coeficientes(secuencia)
# #devuelve tupla con los valores de a y c
# print("Coeficientes: a =", coeficientes[0], "c =", coeficientes[1])


# Ejercicio 12:
# Escribe un programa que lea dos cadenas y devuelva el prefijo común más largo de
# ambas. Ejemplo: las cadenas "politécnico" y "polinización" tienen como prefijo común más
# largo a la cadena "poli"
# def encontrar_prefijo_comun(cadena1, cadena2):
#     prefijo = ""
#     min_length = min(len(cadena1), len(cadena2))
#     for i in range(min_length):
#         if cadena1[i] == cadena2[i]:
#             prefijo += cadena1[i]
#         else:
#             return prefijo
#     return prefijo

# cadena1 = input("Ingrese la primera cadena: ")
# cadena2 = input("Ingrese la segunda cadena: ")

# prefijo_comun = encontrar_prefijo_comun(cadena1, cadena2)
# print("El prefijo común más largo es:", prefijo_comun)

# Ejercicio 13:
# Necesitamos buscar en diversas secuencias de ARN las posibles apariciones del codón 
# iniciador 'AUG', que marca el inicio de un gen. Como en una secuencia de ARN puede 
# haber más de un gen, deseamos conocer todas las posiciones en las que aparece dicho 
# codón. Para ello elaboraremos un programa que ingresará una cadena de caracteres que 
# representa una secuencia de ARN y comprobará que la secuencia de ARN contiene 
# únicamente los caracteres 'A','U', 'G' ó 'C'. En caso contrario, la secuencia es inválida y se 
# deberá imprimir un mensaje adecuado.
# def buscar_codon_iniciador(secuencia_arn):
#     for nucleotido in secuencia_arn:
#         if nucleotido not in ['A', 'U', 'G', 'C']:
#             print("La secuencia de ARN es inválida.")
#             return
    
#     indices = []
#     for i in range(len(secuencia_arn) - 2):
#         if secuencia_arn[i:i+3] == 'AUG':
#             indices.append(i)
    
#     if indices:
#         print("Posiciones del codón iniciador 'AUG':", indices)
#     else:
#         print("El codón iniciador 'AUG' no se encuentra en la secuencia de ARN.")


# # secuencia_arn = "AUGGCAUGGCAUGAUGGCAUG" #ejemplo
# secuencia_arn = input("Ingrese una secuencia de ARN: ")
# buscar_codon_iniciador(secuencia_arn)

#el ejercico14 es opcional


# Ejercicio 15:
# Dos palabras son anagramas si tienen las mismas letras pero en otro orden. Por ejemplo, 
# «torpes» y «postre» son anagramas, mientras que «aparta» y «raptar» no lo son, ya que 
# «raptar» tiene una r de más y una a de menos.
# Escriba la función sonAnagramas(p1, p2) que indique si las palabras p1 y p2 son 
# anagramas:
# sonAnagramas('torpes', 'postre') ---> True
# sonAnagramas('aparta', 'raptar') ---> False
# def sonAnagramas(p1, p2):
#     # replace para eleiminar espacios en blanc y lower para asegurarme que ambas palabras esten en minúsculas
#     p1 = p1.replace(" ", "").lower()
#     p2 = p2.replace(" ", "").lower()

#     #validacion para devolver false si no son iguales las palabras
#     if len(p1) != len(p2):
#         return False
    
    
#     frecuencias_p1 = {}
#     frecuencias_p2 = {}

    
#     for letra in p1:
#         frecuencias_p1[letra] = frecuencias_p1.get(letra, 0) + 1

    
#     for letra in p2:
#         frecuencias_p2[letra] = frecuencias_p2.get(letra, 0) + 1

#     #comparacion de palabras    
#     return frecuencias_p1 == frecuencias_p2


# # print(sonAnagramas('torpes', 'postre'))  # Devuelve True
# # print(sonAnagramas('aparta', 'raptar'))  # Devuelve False
# palabra1 = input(" ingrese una palabra: ")
# palabra2 = input(" ingrese otra palabra: ")

# if sonAnagramas(palabra1, palabra2):
#     print("las palabras son anagramas")
# else:
#     print("las palabras no son anagramas")

# Ejercicio 16:
# Las palabras panvocálicas son las que tienen las cinco vocales. Por ejemplo: centrifugado, 
# bisabuelo, hipotenusa. Escriba la función esPanvocalica(palabra) que indique si una 
# palabra es panvocálica o no:
# esPanvocalica('educativo') ---> True
# esPanvocalica('pedagogico') ---> False
# def esPanvocalica(palabra):
    
#     palabra = palabra.lower()
    
#     # set para almacenar las vocales
#     vocales = set()
    
    
#     for letra in palabra:
#         if letra in 'aeiou':
#             vocales.add(letra)
    
#     return len(vocales) == 5


# # print(esPanvocalica('educativo'))   # Devuelve True
# # print(esPanvocalica('pedagogico'))   # Devuelve False
# palabra = input("ingrese una palabra: ")

# if esPanvocalica(palabra):
#     print("la palabra es panvocalica")
# else:
#     print("la palabra no es panvocalica")

