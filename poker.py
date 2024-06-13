import random as r

def crear_mazo():
    mazo = []
    palos = ['❤️', '🔷', '♣', '♠']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for palo in palos:
        for valor in valores:
            carta = valor + ' de ' + palo
            mazo.append(carta)
    return mazo

def repartir_cartas(mazo):
    r.shuffle(mazo)
    jugador1 = []
    jugador2 = []
    for _ in range(5):
        jugador1.append(mazo.pop())
        jugador2.append(mazo.pop())
    return jugador1, jugador2

def esFull(mano):
    numeros = [carta.split(' ')[0] for carta in mano]
    for numero in numeros:
        if numeros.count(numero) == 3:
            for numero2 in numeros:
                if numeros.count(numero2) == 2:
                    return True
    return False

def esColor(mano):
    palos = [carta.split(' ')[-1] for carta in mano]
    for palo in palos:
        if palos.count(palo) == 5:
            return True
    return False

def valor_numerico(valor):
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return valores[valor]

def esEscalera(mano):
    numeros = [valor_numerico(carta.split(' ')[0]) for carta in mano]
    numeros.sort()
    for i in range(1, len(numeros)):
        if numeros[i-1] != numeros[i] - 1:
            return False
    return True

def esEscaleraColor(mano):
    return esEscalera(mano) and esColor(mano)

def main():
    mazo = crear_mazo()
    jugador1, jugador2 = repartir_cartas(mazo)

    print("Cartas del jugador 1:", jugador1)
    if esFull(jugador1):
        print("Jugador 1 tiene un Full")
    else:
        print("Jugador 1 no tiene un Full")

    if esColor(jugador1):
        print("Jugador 1 tiene un Color")
    else:
        print("Jugador 1 no tiene un Color")

    if esEscalera(jugador1):
        print("Jugador 1 tiene una Escalera")
    else:
        print("Jugador 1 no tiene una Escalera")

    if esEscaleraColor(jugador1):
        print("Jugador 1 tiene una Escalera de Color")
    else:
        print("Jugador 1 no tiene una Escalera de Color")

    print()
    print("Cartas del jugador 2:", jugador2)
    if esFull(jugador2):
        print("Jugador 2 tiene un Full")
    else:
        print("Jugador 2 no tiene un Full")

    if esColor(jugador2):
        print("Jugador 2 tiene un Color")
    else:
        print("Jugador 2 no tiene un Color")

    if esEscalera(jugador2):
        print("Jugador 2 tiene una Escalera")
    else:
        print("Jugador 2 no tiene una Escalera")

    if esEscaleraColor(jugador2):
        print("Jugador 2 tiene una Escalera de Color")
    else:
        print("Jugador 2 no tiene una Escalera de Color")

main()
