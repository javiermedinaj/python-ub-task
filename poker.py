import random as r

mazo = []
#mazo de cartas como un array vacio

palos = ['❤️', '♦', '♣', '♠']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for palo in palos:
    for valor in valores:
        carta = valor + ' de ' + palo
        mazo.append(carta)
#metodo append para agregar las cart-as al mazo array vacio

# metodo shuffler para mezclar el mazo
r.shuffle(mazo)

# Repartir las cartas
jugador1 = []
jugador2 = []
for i in range(5):
    jugador1.append(mazo.pop())
    jugador2.append(mazo.pop())
# el metodo pop() es para sacar la carta de la parte superior de la baraja y asignarla primer o segundo jugador. Esto asegura que cada jugador reciba una carta diferente y que no haya repeticiones.

print("Cartas del jugador 1:", jugador1)
print("Cartas del jugador 2:", jugador2)
