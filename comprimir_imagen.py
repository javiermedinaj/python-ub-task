# Un grupo de investigadores se encuentra trabajando en un centro de observación espacial, 
# donde toman fotografías digitales mediante un nuevo telescopio a una zona aún no 
# explorada del espacio, con el objetivo de determinar la presencia de nuevos planetas 
# girando alrededor de las estrellas que allí se encuentran.
# Estas fotografías tienen la particularidad de contener muy pocos colores, por lo aque cada 
# pixel puede ser representado mediante alguna de las siguientes letras que indica su color: 
# 'B', 'N', 'R', 'V', 'A'. De esta forma una imagen es directamente una secuencia de letras. 
# Además de contener una poca cantidad de colores, también tienen la particularidad de ser 
# demasiado grandes con la intención de obtener la mejor resolución posible. Por este 
# motivo los investigadores necesitan de un método para comprimir estas imágenes y luego 
# poder ser almacenadas.
# Mediante un estudio determinaron que un método muy simple para comprimir estas 
# imágenes es buscar secuencias donde una letra este repetida de forma consecutiva, para 
# después almacenarse sólo una única letra junto al número de veces que se repite. Para 
# diferenciar las partes de la imagen que han sido comprimidas, y luego poder recuperar la 
# imagen original sin ningún problema, se encierran entre paréntesis tanto la letra como el 
# valor que indica la cantidad de repeticiones. Para lograr una verdadera compresión, se 
# debe reemplazar una repetición de letras siempre que esta sea mayor que 4, ya que en caso 
# contrario no se obtiene compresión alguna.
# Se pide escribir dos funciones, la primera recibiendo como entrada una cadena de 
# caracteres conteniendo una imagen sin comprimir y que genere y retorne otra cadena con 
# la compresión de la imagen y la segunda función que reciba una cadena conteniendo la 
# imagen comprimida, genere y retorne otra cadena con la imagen descomprimida.
# Ejemplo:
# primera función
# imagen: NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV
# imagen comprimida: (N8)BRAVB(R5)(A7)(V5)

# def comprimir_imagen(imagen):
#     comprimida = ''
#     i = 0
#     while i < len(imagen):
#         count = 1
#         while i + 1 < len(imagen) and imagen[i] == imagen[i + 1]:
#             i += 1
#             count += 1
#         if count > 4:
#             comprimida += f'({imagen[i]}{count})'
#         else:
#             comprimida += imagen[i] * count
#         i += 1
#     return comprimida

# def descomprimir_imagen(imagen_comprimida):
#     descomprimida = ''
#     i = 0
#     while i < len(imagen_comprimida):
#         if imagen_comprimida[i] == '(':
#             letra = imagen_comprimida[i + 1]
#             repeticiones = ''
#             i += 2
#             while imagen_comprimida[i] != ')':
#                 repeticiones += imagen_comprimida[i]
#                 i += 1
#             repeticiones = int(repeticiones)
#             descomprimida += letra * repeticiones
#         else:
#             descomprimida += imagen_comprimida[i]
#         i += 1
#     return descomprimida

# # Ejemplo de uso
# imagen = "NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV"
# imagen_comprimida = "(N8)BRAVB(R5)(A7)(V5)"
# imagen_descomprimida = descomprimir_imagen(imagen_comprimida)
# print("Imagen compriminada original", imagen_comprimida)
# print("Imagen descomprimida:", imagen_descomprimida)

import re

def comprimir_imagen(imagen):
    comprimida = ''
    for match in re.finditer(r'(\w)\1{3,}', imagen):
        comprimida += f'({match.group(1)}{len(match.group(0))})'
    return comprimida

# def descomprimir_imagen(imagen_comprimida):
#     return re.sub(r'\((\w)(\d+)\)', lambda match: match.group(1) * int(match.group(2)), imagen_comprimida)

def descomprimir_imagen(imagen_comprimida):
    imagen = ""
    i = 0
    while i < len(imagen_comprimida):
        if imagen_comprimida[i] == '(':
            j = i + 1
            while imagen_comprimida[j] != ')':
                j += 1
            letra = imagen_comprimida[j - 1]
            repeticiones = int(imagen_comprimida[i + 2:j])
            imagen += letra * repeticiones
            i = j + 1
        else:
            imagen += imagen_comprimida[i]
            i += 1
    return imagen

# Ejemplo de uso
# imagen = "NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV"
imagen = input(str("Ingrese la imagen sin comprimir: "))
imagen_comprimida = comprimir_imagen(imagen)
print("Imagen comprimida:", imagen_comprimida)

imagen_descomprimida = descomprimir_imagen(imagen_comprimida)
print("Imagen descomprimida:", imagen_descomprimida)




