# # Ejercicio 1:
# # Escribir funciones que, tomando como entrada una lista de números enteros, decida si la 
# # lista:
# # ●está ordenada crecientemente.
# # ●está ordenada decrecientemente. 
# # ●es gaspariforme.  Se dice que un lista de n elementos es gaspariforme si todas sus 
# # sumas   parciales son no negativas, y la suma total es igual a 0. Las sumas parciales de 
# # una lista a de n elementos está definida por
# # sk=∑i=0
# # k
# # ai para k = 0,...,n-1
# # Ejemplo: 
# # Si a = [ 10, 5, 2, 20, 6], n = 5
# # s0 = 10
# # s1 = 10 + 5 = 15
# # s2 = 10 + 5 + 2 = 15  + 2 = 17
# # s3 = 10 + 5 + 2 +  20 = 17 + 20 =  37
# # s4 = 10 + 5 + 2 +  20 + 6= 17 + 20 + 6 =  37 + 6 = 43
# # ●es melchoriforme. Se dice que una lista es melchoriforme si alguno de sus elementos es 
# # un centro . Un elemento es un centro si su valor coincide  con la suma de los otros 
# # elementos de la lista.
# def esta_ordenada_creciente(lista):
#     return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

# def esta_ordenada_decreciente(lista):
#     return all(lista[i] >= lista[i + 1] for i in range(len(lista) - 1))

# # def es_gaspariforme(lista):
# #     suma_parcial = 0
# #     for num in lista:
# #         suma_parcial += num
# #         if suma_parcial < 0:
# #             return False
# #     return suma_parcial == 0

# # def es_melchoriforme(lista):
# #     total = sum(lista)
# #     for num in lista:
# #         if num == total - num:
# #             return True
# #     return False


# lista = [222, 55, 46, 20, 16] #lista de ejemplo 
# print(esta_ordenada_creciente(lista))
# print(esta_ordenada_decreciente(lista))
# # print(es_gaspariforme(lista))
# # print(es_melchoriforme(lista))


print("falta el ejercicio 2")

# Ejercicio 3 # Diseñar una función que determine si una lista de números enteros está ordenada de 
# menor a mayor y cada número i entre 1 y n aparece exactamente i veces. 
# Ejemplo:
# para n = 5
# esTelescopio(5,[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5])   --> verdadero
def esTelescopio(n, lista):
    if len(lista) != n*(n+1)//2:
        return False
    for i in range(1, n+1):
        if lista.count(i) != i:
            return False
    return lista == sorted(lista)

n = 3
lista = [1, 2, 2, 3, 3, 3,3,3, 4, 4, 4, 4, 5, 5, 5, 5, ]
print(esTelescopio(n, lista))
