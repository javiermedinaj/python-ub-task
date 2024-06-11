# #Ejercicio 1:
# Escribir funciones que, tomando como entrada una lista de números enteros, decida si la 
# lista:
# ●está ordenada crecientemente.
# ●está ordenada decrecientemente. 
# ●es gaspariforme.  Se dice que un lista de n elementos es gaspariforme si todas sus 
# sumas   parciales son no negativas, y la suma total es igual a 0. Las sumas parciales de 
# una lista a de n elementos está definida por
# sk=∑i=0
# k
# ai para k = 0,...,n-1
# Ejemplo: 
# Si a = [ 10, 5, 2, 20, 6], n = 5
# s0 = 10
# s1 = 10 + 5 = 15
# s2 = 10 + 5 + 2 = 15  + 2 = 17
# s3 = 10 + 5 + 2 +  20 = 17 + 20 =  37
# s4 = 10 + 5 + 2 +  20 + 6= 17 + 20 + 6 =  37 + 6 = 43
# ●es melchoriforme. Se dice que una lista es melchoriforme si alguno de sus elementos es 
# un centro . Un elemento es un centro si su valor coincide  con la suma de los otros 
# elementos de la lista.