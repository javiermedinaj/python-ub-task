print("Tablero:")
print("  a b c d e f g h")
print(" +----------------")
for i in range(8, 0, -1):
    row = str(i) + "|"
    for j in range(1, 9):
        row += ". "
    row += "|" + str(i)
    print(row)
print(" +----------------")
print("  a b c d e f g h")

rey1 = int(input("Escriba la fila donde está el rey: "))
rey2 = int(input("Escriba la columna donde está el rey: "))
if rey1 > 8 or rey2 > 8 or rey1 < 1 or rey2 < 1:
    print("Error")
else:
    print("Tablero con la posición del rey:")
    print("  a b c d e f g h")
    print(" +----------------")
    for i in range(8, 0, -1):
        row = str(i) + "|"
        for j in range(1, 9):
            if i == rey1 and j == rey2:
                row += "♔ "
            else:
                row += ". "
        row += "|" + str(i)
        print(row)
    print(" +----------------")
    print("  a b c d e f g h")

    pieza = input("Ingrese qué pieza desea utilizar (peon, reina, alfil, caballo, torre): ")

if pieza == "alfil":
    alfil1 = int(input("Ingrese la fila donde está el alfil: "))
    alfil2 = int(input("Ingrese la columna donde está el alfil: "))
    
    if alfil1 > 8 or alfil2 > 8 or alfil1 < 1 or alfil2 < 1:
        print("Error")
    else:
        print("Tablero con la posición del alfil:")
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(8, 0, -1):
            row = str(i) + "|"
            for j in range(1, 9):
                if i == alfil1 and j == alfil2:
                    row += "♗ "
                elif i == rey1 and j == rey2:
                    row += "♔ "
                else:
                    row += ". "
            row += "|" + str(i)
            print(row)
        print(" +----------------")
        print("  a b c d e f g h")
        
        alfil3 = abs(rey1 - alfil1)
        alfil4 = abs(rey2 - alfil2)
        
        if alfil3 == alfil4:
            print("El rey está en jaque.")
        else:
            print("El rey no está en jaque.")
elif pieza == "reina":
    reina1 = int(input("Ingrese la fila donde está la reina: "))
    reina2 = int(input("Ingrese la columna donde está la reina: "))
    
    if reina1 > 8 or reina2 > 8 or reina1 < 1 or reina2 < 1:
        print("Error")
    else:
        print("Tablero con la posición de la reina:")
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(8, 0, -1):
            row = str(i) + "|"
            for j in range(1, 9):
                if i == reina1 and j == reina2:
                    row += "♕ "
                elif i == rey1 and j == rey2:
                    row += "♔ "
                else:
                    row += ". "
            row += "|" + str(i)
            print(row)
        print(" +----------------")
        print("  a b c d e f g h")
        
        reina3 = abs(rey1 - reina1)
        reina4 = abs(rey2 - reina2)
        
        if reina3 == reina4 or rey1 == reina1 or rey2 == reina2:
            print("El rey está en jaque.")
        else:
            print("El rey no está en jaque.")
elif pieza == "caballo":
    caballo1 = int(input("Ingrese la fila donde está el caballo: "))
    caballo2 = int(input("Ingrese la columna donde está el caballo: "))
    if caballo1 > 8 or caballo2 > 8 or caballo1 < 1 or caballo2 < 1:
        print("Error")
    else:
        print("Tablero con la posición del caballo:")
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(8, 0, -1):
            row = str(i) + "|"
            for j in range(1, 9):
                if i == caballo1 and j == caballo2:
                    row += "♘ "
                elif i == rey1 and j == rey2:
                    row += "♔ "
                else:
                    row += ". "
            row += "|" + str(i)
            print(row)
        print(" +----------------")
        print("  a b c d e f g h")
        
        caballo3 = abs(rey1 - caballo1)
        caballo4 = abs(rey2 - caballo2)
        if (caballo3 == 1 and caballo4 == 2) or (caballo3 == 2 and caballo4 == 1):
            print("El rey está en jaque.")
        else:
            print("El rey no está en jaque.")
elif pieza == "torre":    
    torre1 = int(input("ingrese la fila donde esta la torre: "))
    torre2 = int(input("ingrese la columna donde esta la torre: "))
    if torre1 > 8 or torre2 > 8 or torre1 < 1 or torre2 < 1:
        print("Error")
    elif torre1 == rey1 or torre2 == rey2:
        print("Tablero con la posición de la torre:")
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(8, 0, -1):
            row = str(i) + "|"
            for j in range(1, 9):
                if i == torre1 and j == torre2:
                    row += "♖ "
                elif i == rey1 and j == rey2:
                    row += "♔ "
                else:
                    row += ". "
            row += "|" + str(i)
            print(row)
        print(" +----------------")
        print("  a b c d e f g h")
        print("El rey está en jaque.")
    else:
        print("Tablero con la posición de la torre:")
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(8, 0, -1):
            row = str(i) + "|"
            for j in range(1, 9):
                if i == torre1 and j == torre2:
                    row += "♖ "
                elif i == rey1 and j == rey2:
                    row += "♔ "
                else:
                    row += ". "
            row += "|" + str(i)
            print(row)
        print(" +----------------")
        print("  a b c d e f g h")
        print("El rey no está en jaque")
elif pieza == "peon":
    peon1 = int(input("Ingrese la fila donde está el peon: "))
    peon2 = int(input("Ingrese la columna donde está el peon: "))
    if peon1 > 8 or peon2 > 8 or peon1 < 1 or peon2 < 1:
        print("Error")
    elif rey1 == peon1 + 1 and abs(rey2 - peon2) == 1:
        print("Tablero con la posición del peón:")
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(8, 0, -1):
            row = str(i) + "|"
            for j in range(1, 9):
                if i == peon1 and j == peon2:
                    row += "♙ "
                elif i == rey1 and j == rey2:
                    row += "♔ "
                else:
                    row += ". "
            row += "|" + str(i)
            print(row)
        print(" +----------------")
        print("  a b c d e f g h")
        print("El rey está en jaque.")
    else:
        print("Tablero con la posición del peón:")
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(8, 0, -1):
            row = str(i) + "|"
            for j in range(1, 9):
                if i == peon1 and j == peon2:
                    row += "♙ "
                elif i == rey1 and j == rey2:
                    row += "♔ "
                else:
                    row += ". "
            row += "|" + str(i)
            print(row)
        print(" +----------------")
        print("  a b c d e f g h")
        print("El rey no está en jaque.")
else:
    print("Error")

