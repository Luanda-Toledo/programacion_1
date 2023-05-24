from data_stark import lista_personajes

# Luanda Gisel Toledo Viera 
# DIV K

# lista_heroes =
# [
# {
#   "nombre": "Howard the Duck",
#   "identidad": "Howard (Last name unrevealed)",
#   "empresa": "Marvel Comics",
#   "altura": "79.349999999999994",
#   "peso": "18.449999999999999",
#   "genero": "M",
#   "color_ojos": "Brown",
#   "color_pelo": "Yellow",
#   "fuerza": "2",
#   "inteligencia": "average"
# }
# ]

# DESAFIO OO
# A) Analizar detenidamente el set de datos

# B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def imprimir_nombres():
    for heroe in lista_personajes:
        print(heroe["nombre"])

# C) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def imprimir_nombre_y_altura():
    for heroe in lista_personajes:
        altura = float(heroe["altura"])
        print("Nombre: {0} Altura: {1} ".format(heroe["nombre"], altura))

# D) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def imprimir_mas_alto():
    altura_maxima = None

    for indice in range(len(lista_personajes)):
        if (indice == 0 or altura_maxima < float(lista_personajes[indice]["altura"])):
            altura_maxima = float(lista_personajes[indice]["altura"])
            nombre_altura_maxima = lista_personajes[indice]["nombre"]

    return print("Nombre personaje mas alto: {0}, altura: {1}".format(
        nombre_altura_maxima, altura_maxima))

# E) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def imprimir_mas_bajo():
    altura_minima = None

    for indice in range(len(lista_personajes)):
        if (indice == 0 or altura_minima > float(lista_personajes[indice]["altura"])):
            altura_minima = float(lista_personajes[indice]["altura"])
            nombre_altura_minima = lista_personajes[indice]["nombre"]

    return print("Nombre personaje mas bajo: {0}, altura: {1}".format(
        nombre_altura_minima, altura_minima))

# F) Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def imprimir_promedio():
    acumulador_altura = 0

    for indice in range(len(lista_personajes)):
            acumulador_altura += float(lista_personajes[indice]["altura"])

    promedio = acumulador_altura / len(lista_personajes)

    print("El promedio de la altura es: {0}".format(promedio))

# G) Calcular e informar cual es el superhéroe más y menos pesado.
def imprimir_mas_pesado():
    peso_maximo = None

    for indice in range(len(lista_personajes)):
        if (indice == 0 or peso_maximo < float(lista_personajes[indice]["peso"])):
            peso_maximo = float(lista_personajes[indice]["peso"])
            nombre_peso_maximo = lista_personajes[indice]["nombre"]

    return print("Nombre personaje mas pesado: {0}, peso: {1}".format(
        nombre_peso_maximo, peso_maximo))

def imprimir_menos_pesado():
    peso_minimo = None

    for indice in range(len(lista_personajes)):
        if (indice == 0 or peso_minimo > float(lista_personajes[indice]["peso"])):
            peso_minimo = float(lista_personajes[indice]["peso"])
            nombre_peso_minimo = lista_personajes[indice]["nombre"]

    return print("Nombre personaje con peso mas bajo: {0}, peso: {1}".format(
        nombre_peso_minimo, peso_minimo))



def main():
    while True:
        # Mostrar menú de opciones
        print("Menú de opciones:")
        print("1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
        print("2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
        print("3. Recorrer la lista y determinar cuál es el superhéroe más alto y el mas bajo")
        print("4. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
        print("5. Calcular e informar cual es el superhéroe más y menos pesado.")
        print("0. Salir del programa")
        opcion = input("\nIngrese la opción deseada: ")

        if opcion == "1":
            imprimir_nombres()

        # Opción 2:
        elif opcion == "2":
            imprimir_nombre_y_altura()

        # Opción 3:
        elif opcion == "3":
            imprimir_mas_alto()
            imprimir_mas_bajo()

        # Opción 4:
        elif opcion == "4":
            imprimir_promedio()

        # Opción 5:
        elif opcion == "5":
            imprimir_mas_pesado()
            imprimir_menos_pesado()

        # Opcion 0: Salir
        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

main()
