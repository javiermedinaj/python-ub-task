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

import random as r

def crear_tablero(filas, columnas):
    tablero = []
    tablero2=[]
    naufragos = 0
    for _ in range(filas):
        fila = []
        fila2 = []
        for _ in range(columnas):
            fila.append(0)
            fila2.append('~~')
        tablero.append(fila)
        tablero2.append(fila2)
    
    if filas*columnas >= 4:
        while naufragos <4:
            fil = r.randint(0,filas-1)
            col = r.randint(0,columnas-1)
            if tablero[fil][col] == 0:
                tablero[fil][col] = 1
                naufragos+=1 
    else:
        print('¡El tablero debe tener al menos 4 casillas para poder colocar los naufragos!')
        return None, None
    return tablero, tablero2


def buscar_naufrago(tablero,tablero2):
    if tablero == None:
        return False
    
    filas = len(tablero)
    columnas = len(tablero[0])
    
    naufragos = 0
    sondas = 0
    while sondas <=10:
        
        sondas += 1
        print()
        print('/'*55,'\n')
        
        sondaFila = int(input('Elija la fila en donde activará la sonda: '))
        sondaColumna = int(input('Elija la columna en donde se activará la sonda: '))
        
        if sondaFila > filas or sondaColumna > columnas:
            print('¡La sonda no puede ser activada en una casilla fuera del tablero!')
        else:
            sondaFila-=1
            sondaColumna-=1
            tablero2[sondaFila][sondaColumna] = f'S{str(sondas)}'
            
            print()
            print('Sondas usadas: ', sondas )
            print('Te quedan', 10-sondas, 'sondas','\n')
            
            if tablero[sondaFila][sondaColumna] == 1:
                print(f'Naufrago encontrado en la fila {sondaFila +1} y columna {sondaColumna +1} \n')
                tablero[sondaFila][sondaColumna] = 3
                tablero2[sondaFila][sondaColumna] = 'N'
                naufragos += 1

            fila = sondaFila - 1
            while fila >= 0:
                if tablero[fila][sondaColumna] == 1:
                    print ('¡Se encontró una luz al norte!')
                fila -= 1

            fila = sondaFila + 1
            while fila < filas:
                if tablero[fila][sondaColumna] == 1:
                    print('¡Se encontró una luz al sur!')
                fila += 1

            columna = sondaColumna + 1
            while columna < columnas:
                if tablero[sondaFila][columna] == 1:
                    print('¡Se encontró una luz al este!')
                columna += 1

            columna = sondaColumna - 1
            while columna >= 0:
                if tablero[sondaFila][columna] == 1:
                    print('¡Se encontró una luz al oeste!')
                columna -= 1
                
            print()  
            for i in tablero2:
                print(i) 
            if naufragos == 4:
                return True
    return False

fila_tab = int(input('Elija la cantidad de filas que tendrá el tablero: '))
columna_tab = int(input('Elija la cantidad de columnas que tendrá el tablero: '))
    
tablero, tablero2 = crear_tablero(fila_tab,columna_tab)

if buscar_naufrago(tablero,tablero2):
    print('¡Felicitaciones, encontraste a todos los naufragos! :)')
elif tablero == None:
    print('¡No se pudo crear el tablero! :/')
else:
    print('Te quedaste sin sondas, ¡perdiste! :(')