def crear_laberinto(filas, columnas, muros):
    # Crear matriz vacía con espacios
    laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]
    
    # Colocar los muros
    for fila, columna in muros:
        laberinto[fila][columna] = 'X'
    
    # Colocar la salida
    laberinto[filas-1][columnas-1] = 'S'
    
    return laberinto


# Datos del ejercicio
muros = ((0,1), (0,2), (0,3), (0,4),
         (1,1),
         (2,1), (2,3),
         (3,3),
         (4,0), (4,1), (4,2), (4,3))

laberinto = crear_laberinto(5, 5, muros)

# Mostrar laberinto
for fila in laberinto:
    print(fila)



def resolver_laberinto(laberinto):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    movimientos = [
        (1, 0, 'Abajo'),
        (-1, 0, 'Arriba'),
        (0, 1, 'Derecha'),
        (0, -1, 'Izquierda')
    ]
    
    visitado = set()
    camino = []
    
    def dfs(fila, columna):
        # Si estamos fuera de límites o es muro o ya visitado
        if (fila < 0 or fila >= filas or
            columna < 0 or columna >= columnas or
            laberinto[fila][columna] == 'X' or
            (fila, columna) in visitado):
            return False
        
        # Si llegamos a la salida
        if (fila, columna) == (filas-1, columnas-1):
            return True
        
        visitado.add((fila, columna))
        
        for df, dc, nombre in movimientos:
            nueva_fila = fila + df
            nueva_columna = columna + dc
            
            camino.append(nombre)
            if dfs(nueva_fila, nueva_columna):
                return True
            camino.pop()
        
        return False
    
    dfs(0, 0)
    return camino


# Resolver el laberinto
solucion = resolver_laberinto(laberinto)

print("\nSecuencia de movimientos:")
print(solucion)