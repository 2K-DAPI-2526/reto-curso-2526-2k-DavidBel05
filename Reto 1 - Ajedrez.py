def crear_tablero_inicial():
    return [
        ["♜","♞","♝","♛","♚","♝","♞","♜"],
        ["♟","♟","♟","♟","♟","♟","♟","♟"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ["♙","♙","♙","♙","♙","♙","♙","♙"],
        ["♖","♘","♗","♕","♔","♗","♘","♖"]
    ]


def guardar_tablero(tablero, fichero):
    for fila in tablero:
        fichero.write("\t".join(fila) + "\n")
    fichero.write("\n")   # separa tableros


def mover_pieza(tablero, f1, c1, f2, c2):
    tablero[f2][c2] = tablero[f1][c1]
    tablero[f1][c1] = " "


# Programa principal
nombre = input("Nombre del fichero: ")

tablero = crear_tablero_inicial()

with open(nombre, "w", encoding="utf-8") as f:

    guardar_tablero(tablero, f)

    while True:

        opcion = input("¿Hacer movimiento? (s/n): ")

        if opcion.lower() == "n":
            break

        f1 = int(input("Fila origen (0-7): "))
        c1 = int(input("Columna origen (0-7): "))
        f2 = int(input("Fila destino (0-7): "))
        c2 = int(input("Columna destino (0-7): "))

        mover_pieza(tablero, f1, c1, f2, c2)

        guardar_tablero(tablero, f)

print("Partida guardada.")



def mostrar_movimiento(nombre_fichero, num_movimiento):

    with open(nombre_fichero, "r", encoding="utf-8") as f:
        contenido = f.read()

    tableros = contenido.strip().split("\n\n")

    if num_movimiento < 0 or num_movimiento >= len(tableros):
        print("Movimiento no existe")
        return

    tablero = tableros[num_movimiento]

    for linea in tablero.split("\n"):
        print(linea.replace("\t"," "))


archivo = input("Introduce el fichero de la partida: ")
mov = int(input("Movimiento a mostrar: "))

mostrar_movimiento(archivo, mov)