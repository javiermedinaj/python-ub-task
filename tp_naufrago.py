
# 1
#  Trabajo Práctico 16
# Náufragos es un juego basado en el juego Galaxis que consiste en rescatar personas 
# perdidas en el espacio. En nuestro caso, el rescate se produce en el mar, y el objetivo es 
# rescatar la máxima cantidad de personas, con la menor cantidad de sondas detectoras.
# Una sonda detectora es un artefacto que se utiliza para detectar personas. Cuando una 
# sonda es activada en una posición dada, ésta envía una señal en dirección de cada uno de 
# los cuatro puntos cardinales. La señal se propaga hasta perderse salvo que choque con el 
# dispositivo reflector de alguno de los náufragos. En ese caso, la señal retorna a la sonda lo 
# que produce que se encienda una luz intermitente sobre la cubierta de la sonda. Note que 
# cada sonda tiene una única luz, por lo cual cuando la luz comienza a parpadear, no hay 
# forma de saber si esto ocurre por que retornaron varias señales o sólo una, tampoco hay 
# cómo saber desde que dirección retornó la señal, y menos aún, a qué distancia de la sonda 
# se encontraba el dispositivo reflector que hizo retornar la señal.
# Sin embargo la sonda detectora sí es capaz de determinar si ella es activada en la posición 
# en que se encuentra un náufrago, en cuyo caso la luz se enciende y no parpadea. Cuando 
# esto sucede, el náufrago puede ser rescatado desde la posición en que se ha activado la 
# sonda.
# En el siguiente ejemplo se muestra las posiciones de 4 náufragos, representados por la 
# letra N. Así, si la sonda detectora es activada en la posición [3,3] la señal se pierde, en tanto 
# que si es activada en la posición [6,2] se detecta un náufrago, y en la posición [6,5] se 
# rescata un náufrago.
# Estrategia de solución
# Para implementar este juego se utiliza una lista bidimensional que representar ́a el tablero 
# correspondiente al espacio del naufragio. El tamaño del tablero será configurable, y en él 
# se dispondrán los náufragos en posiciones aleatorias. La cantidad de náufragos, así como la 
# cantidad de sondas disponibles también será configurable.
# En cada paso, debe pedirse al jugador la posición en la cual desea activar una sonda 
# detectora.
# El algoritmo deberá determinar si en esa posición existe un náufrago, si en alguna de las 
# cuatro direcciones existe un náufrago, o si la señal se pierde. En cualquier situación debe 
# notificar el resultado al jugador. Esta rutina se repite hasta que se hayan rescatado todos 
# los náufragos, o se acaben las sondas detectoras.

import random

def generar_naufragos(filas, columnas, num_naufragos):
    naufragos = []
    while len(naufragos) < num_naufragos:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if (fila, columna) not in naufragos:
            naufragos.append((fila, columna))
    return naufragos

def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

def activar_sonda(tablero, naufragos, fila, columna):
    if (fila, columna) in naufragos:
        print("¡Náufrago rescatado en la posición ({}, {})!".format(fila, columna))
        tablero[fila][columna] = 'R'
        naufragos.remove((fila, columna))
        return "rescatado"
    else:
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        señal_encontrada = False
        for dir in direcciones:
            i, j = fila, columna
            while 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
                if tablero[i][j] == 'N':
                    señal_encontrada = True
                    break
                i += dir[0]
                j += dir[1]
        if señal_encontrada:
            print("¡Señal detectada en ({}, {})!".format(fila, columna))
            tablero[fila][columna] = 'S'
            return "señal_detectada"
        else:
            print("Señal perdida en ({}, {})".format(fila, columna))
            tablero[fila][columna] = 'P'
            return "señal_perdida"

def juego_terminado(naufragos, sondas_usadas, num_sondas):
    return len(naufragos) == 0 or sondas_usadas >= num_sondas

def jugar():
    filas = 10
    columnas = 10
    num_naufragos = 4
    num_sondas = 10

    tablero = [['-' for _ in range(columnas)] for _ in range(filas)]
    naufragos = generar_naufragos(filas, columnas, num_naufragos)
    for fila, columna in naufragos:
        tablero[fila][columna] = 'N'

    sondas_usadas = 0
    rescatados = 0

    print("Bienvenido al juego de Náufragos!")
    while not juego_terminado(naufragos, sondas_usadas, num_sondas):
        mostrar_tablero(tablero)
        fila = int(input("Ingrese la fila para activar la sonda: "))
        columna = int(input("Ingrese la columna para activar la sonda: "))
        resultado = activar_sonda(tablero, naufragos, fila, columna)
        sondas_usadas += 1
        if resultado == "rescatado":
            rescatados += 1

    if rescatados == num_naufragos:
        print("¡Felicidades! Todos los náufragos han sido rescatados.")
    else:
        print("Juego terminado. No se han podido rescatar a todos los náufragos.")
    mostrar_tablero(tablero)

if __name__ == "__main__":
    jugar()
