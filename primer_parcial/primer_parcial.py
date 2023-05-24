import json

def leer_archivo(ruta:str)->str:
    '''
    recibe como parametro la ruta del archivo que se quiere leer
    abre, lee y cierra el archivo 
    retorna las lineas del archivo en un print
    '''
    with open(ruta, 'r') as archivo:
        contenido = json.load(archivo)
    return contenido['jugadores']
dicc_jugadores = leer_archivo("/home/luli/Escritorio/programacion_1/primer_parcial/data_jugadores.json")

def imprimir_dato(cadena_de_texto:str):
    '''
    toma un strin y lo imprime
    '''
    print(cadena_de_texto)

# 1 - Mostrar la lista de todos los jugadores del Dream Team. 
# Con el formato: Nombre Jugador - Posición. Ejemplo: Michael Jordan - Escolta
def mostrar_jugadores(dicc_jugadores):
    '''
    Recibe el diccionario de jugadores.
    Lo recorre. Toma el nombre y la posicion para luego
    imprimirlo por consola.
    '''
    for jugador in dicc_jugadores:
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        imprimir_dato(f"{nombre} - {posicion}")
        
mostrar_jugadores(dicc_jugadores)

# 2 - Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, 
# incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, 
# promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, 
# bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.



















