import random as r
def crear_mazo():
    mazo: list[str] = []
    palos: list[str] = ['❤️', '♦️', '♣', '♠']
    valores: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for palo in palos:
        for valor in valores:
            carta = valor + ' de ' + palo
            mazo.append(carta)
    return mazo


def repartir_cartas(mazo):
    r.shuffle(mazo)
    jugador1 = []
    jugador2 = []
    for i in range(5):
        jugador1.append(mazo.pop())
        jugador2.append(mazo.pop())
    return jugador1, jugador2


def esFull(mano):
    valores = [carta[0] for carta in mano]
    counts = {valor: valores.count(valor) for valor in valores}
    return 3 in counts.values() and 2 in counts.values()


def esColor(mano):
    palos = set([carta[1] for carta in mano])
    return len(palos) == 1


def esEscalera(mano):
    valores = [carta[0] for carta in mano]
    valores_numericos = [int(valor) if valor.isdigit() else (
        11 if valor == 'J' else (12 if valor == 'Q' else (13 if valor == 'K' else 1))) for valor in valores]
    return sorted(valores_numericos) == list(range(min(valores_numericos), max(valores_numericos) + 1))


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
    if esColor(jugador1) and esEscalera(jugador1):
        print("Jugador 1 tiene una Escalera de Color")
    else:
        print("Jugador 1 no tiene una Escalera de Color")

    #mano del jugador 2
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

    if esColor(jugador2) and esEscalera(jugador2):
        print("Jugador 2 tiene una Escalera de Color")
    else:
        print("Jugador 2 no tiene una Escalera de Color")


main()
