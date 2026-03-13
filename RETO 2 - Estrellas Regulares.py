import turtle
def dibujar_estrella(puntas, tamaño):
    angulo = 180 - (180/puntas)

    for i in range(puntas):
        turtle.forward(tamaño)
        turtle.right(angulo)


#CONFIGURACIÓN DE LA VENTANA
turtle.speed(3)

#PEDIR NÚMERO DE PUNTAS AL USUARIO
while True:
    try:
        puntas = int(input("Introduce el número de puntas de la estrella: "))
        break
    except ValueError:
        print("Introduce solo un número.")
#DIBUJAR LA ESTRELLA
dibujar_estrella(puntas, 200)

turtle.done()