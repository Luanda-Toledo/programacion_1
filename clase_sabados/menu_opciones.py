# DIV H
# LUANDA TOLEDO VIERA
# EJERCICIO MENU DE OPCIONES

lista_animales = [{"gato": "mamifero terrestre"}, {"perro": "mamifero terrestre"},
                 {"delfin": "mamifero acuatico"}, {"tiburon": "peces cartilaginosos"},
                 {"lobos": "mamifero terrestre"}, {"leones": "mamifero terrestre"}, 
                 {"serpiente": "reptil"}, {"cocodrilo": "reptil"}, 
                 {"foca": "mamifero acuatico"}, {"iguanas": "reptil"}]

# 1
def agregar_elementos_lista(lista_animales):
    respuesta = "si"
    while respuesta == "si":
        nuevo_elemento = {}
        animal_ingresado = input("Ingrese un animal: ")
        tipo_ingresado = input("Ingrese que tipo de animal es: ")
        nuevo_elemento[animal_ingresado] = tipo_ingresado
        lista_animales.append(nuevo_elemento)
        respuesta = input("Desea agregar otro animal? (si/no): ")

# 2
def imprimir_lista(lista_animales):
    for animal in lista_animales:
        print(animal)

# 3
def imprimir_porcentaje_por_tipo(lista_animales):
    contador_tipos = {}
    cantidad_animales = len(lista_animales)

    for animales in lista_animales:
        for animal, tipo in animales.items():
            if tipo not in contador_tipos:
                contador_tipos[tipo] = 0

            contador_tipos[tipo] += 1    

    for tipo, cantidad_tipos in contador_tipos.items():
        porcentaje = cantidad_tipos / cantidad_animales * 100
        print("{0} : {1}%".format(tipo, porcentaje))

# 4 - 5
def mayor_menor_por_tipo(lista_animales, buscar = "max"):
    contador_tipos = {}
    cantidad_buscada = None
    nombre_del_tipo = None

    for animales in lista_animales:
        for animal, tipo in animales.items():
            if tipo not in contador_tipos:
                contador_tipos[tipo] = 0
            contador_tipos[tipo] += 1
        
    for tipo, cantidad_tipos in contador_tipos.items():

        if buscar == "max":
            if cantidad_buscada is None or cantidad_tipos > cantidad_buscada:
                cantidad_buscada = cantidad_tipos
                nombre_del_tipo = tipo
        if buscar == "min":
            if cantidad_buscada is None or cantidad_tipos < cantidad_buscada:
                cantidad_buscada = cantidad_tipos 
                nombre_del_tipo = tipo

    print("El tipo {0} es: {1} {2}".format(buscar, cantidad_buscada, nombre_del_tipo))  

# 6
def buscar_animal(lista_animales):
    animal_ingresado = input("Ingrese el animal que desea buscar en la lista: ")
    for animal in lista_animales:
        if animal_ingresado == animal[animal_ingresado]:
            print(animal)
        
    if lista_animales[animal_ingresado] not in lista_animales:
        print("El animal no se encuentra en la lista \n")
               


def main():
    while True:
        # Mostrar menú de opciones
        print("Menú de opciones:")
        print("1. Agregar animales y tipo")
        print("2. Imprimir la lista completa de animales con su tipo")
        print("3. Mostrar el porcentaje de animales por tipo")
        print("4. Mayor cantidad de animales por tipo")
        print("5. Menor cantidad de animales por tipo")
        print("6. Informar si un animal se encuentra en la lista e imprimirlo")
        print("7. Ingresar un animal e informar la primer ocurrencia de ese animal en la lista si existe")
        print("8. Informar la cantidad de animales por cada tipo de animal")
        print("9. Vaciar la lista")
        print("10. Salir del programa")

        opcion = input("\nIngrese la opción deseada: ")

        # Opcion 1: Agregar animales y tipo
        if opcion == "1":
            agregar_elementos_lista(lista_animales)

        # Opción 2: Imprimir la lista completa de animales con su tipo
        elif opcion == "2":
            imprimir_lista(lista_animales)

        # Opción 3: Mostrar el porcentaje de animales por tipo
        elif opcion == "3":
            imprimir_porcentaje_por_tipo(lista_animales)

        # Opción 4: Mayor cantidad de animales por tipo
        elif opcion == "4":
            mayor_menor_por_tipo(lista_animales, "max")

        # Opción 5: Menor cantidad de animales por tipo
        elif opcion == "5": 
            mayor_menor_por_tipo(lista_animales, "min")

        # Opcion 6: Informar si un animal se encuentra en la lista e imprimirlo
        elif opcion == "6":
            buscar_animal(lista_animales)

        # Opcion 7: ngresar un animal e informar la primer ocurrencia de ese animal en la lista si existe
        elif opcion == "7":
            pass

        # Opcion 8: Informar la cantidad de animales por cada tipo de animal
        elif opcion == "8":
            pass

        # Opcion 9: Vaciar la lista
        elif opcion == "9":
            pass

        # Opcion 10: Salir del programa
        elif opcion == "10":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

main()









