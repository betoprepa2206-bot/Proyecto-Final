import random

def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    print("\n  0   1   2")
    for i, fila in enumerate(tablero):
        print(i, "|".join(fila))
        if i < 2:
            print("  -----")

def busqueda_lineal_ganador(tablero, jugador):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True
    
    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] == jugador:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def movimiento_computadora(tablero):
    espacios = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                espacios.append((i, j))

    filas = [pos[0] for pos in espacios]
    burbuja(filas)

    return random.choice(espacios)

def jugar():
    tablero = crear_tablero()
    turno = "X"
    computadora = "O"

    print("JUEGO DEL GATO")
    mostrar_tablero(tablero)

    while True:
        if turno == "X":
            try:
                fila = int(input("Ingresa la fila (0-2): "))
                col = int(input("Ingresa la columna (0-2): "))
            except:
                print("Entrada inválida.")
                continue

            if fila not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Movimiento fuera del rango.")
                continue

            if tablero[fila][col] != " ":
                print("Ese espacio ya está ocupado.")
                continue

            tablero[fila][col] = "X"

            if busqueda_lineal_ganador(tablero, "X"):
                mostrar_tablero(tablero)
                print("Ganaste.")
                break

            turno = "O"

        else:
            print("Turno de la computadora...")
            fila, col = movimiento_computadora(tablero)
            tablero[fila][col] = "O"

            if busqueda_lineal_ganador(tablero, "O"):
                mostrar_tablero(tablero)
                print("Perdiste.")
                break

            turno = "X"

        mostrar_tablero(tablero)

        espacios_vacios = any(" " in fila for fila in tablero)
        if not espacios_vacios:
            mostrar_tablero(tablero)
            print("Empate.")
            break

jugar()
