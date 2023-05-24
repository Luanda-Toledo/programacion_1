from ejercicios_stark.stark_cero_uno_dos.stark_biblioteca import *
import re
import json
import csv

def leer_archivo(ruta:str) -> str:
    '''
    recibe como parametro la ruta del archivo que se quiere leer
    abre, lee y cierra el archivo 
    retorna las lineas del archivo en un print
    '''
    with open(ruta, 'r') as archivo:
        contenido = json.load(archivo)
    return contenido['heroes']

lista_heroes = leer_archivo("/home/luli/Escritorio/programacion_1/ejercicios_stark/data_stark.json")

def capitalizar_palabras(cadena_texto:str):
    '''
    Recibe una cadena de texto y la devuelve capitalizada
    '''
    lista = cadena_texto.split()
    cadena_texto_nueva = []

    for palabra in lista:
            cadena_texto_nueva.append(palabra.capitalize())
    return " ".join(cadena_texto_nueva)

def obtener_nombre_capitalizado(diccionario:dict) -> str:
    '''
    Recibe un diccionario, y devulve los nombres capitalizados.
    '''
    mensaje = "Nombre: {0}".format(capitalizar_palabras(diccionario["nombre"]))
    return mensaje

def obtener_nombre_y_dato(diccionario:dict, clave:str):
    '''
    Recibe una lista y una clave, y devulve un mensaje con los datos que coinciden
    con diicha clave n el diccionario.
    '''
    mensaje = "{0} | {1}: {2}".format(obtener_nombre_capitalizado(diccionario), clave, diccionario[clave])
    return mensaje

# 1 - Listar los primeros N héroes. El valor de N será ingresado por el usuario (Validar que no supere max. de lista) -------------------
def listar_primeros_n_elementos(lista_heroes:list, cantidad_heroes:str):
    '''
    Recibe una lista y un parametro, e imprime la catidad de heroes indicada como parametro
    '''
    lista_filtrada = []
    if cantidad_heroes.isdigit():
        n = int(cantidad_heroes)

    if n < 0 or n > len(lista_heroes):
        imprimir_dato("Opcion invalida. Intente nuevamente")
    else:
        for heroes in range(n):
            lista_filtrada.append(lista_heroes[heroes])
        return lista_filtrada


# 2 - Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
# 3 - Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
def ordenar_lista_diccionarios_ascendente(lista:list, clave:str) -> list:
    '''
    Recibe una lista de diccionarios y la devuelve ordenada segun clave especifica de menor a mayor
    '''
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for i in range(len(lista) - 1):
            if lista[i][clave] > lista[i + 1][clave]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                flag_swap = True
    return lista

def ordenar_lista_diccionarios_descendente(lista:list, clave:str) -> list:
    '''
    Recibe una lista de diccionarios y la devuelve ordenada segun clave especifica de menor a mayor
    '''
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for i in range(len(lista) - 1):
            if lista[i][clave] < lista[i + 1][clave]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                flag_swap = True
    return lista

def ordenar_listar_ascendente_descendente(lista_heroes:list, key:str) -> list:
    '''
    Recibe una lista, una llave, y solicita al usuario el tipo de orden. Los ordena e imprime.
    '''
    lista_filtrada = []

    while True:
        tipo_orden = input("Ingrese el tipo de orden: asc o desc \n")
        
        if tipo_orden.lower() == "asc" or tipo_orden.lower() == "desc":
            break
        else:
            imprimir_dato("Opcion no valida. Intente nuevamente")
    
    if tipo_orden == "asc":
        lista_ordenada = ordenar_lista_diccionarios_ascendente(lista_heroes, key)
    else:
        lista_ordenada = ordenar_lista_diccionarios_descendente(lista_heroes, key)

    for heroe in lista_ordenada:
        diccionario_heroe_filtrado = {}
        diccionario_heroe_filtrado["nombre"] = heroe["nombre"]
        diccionario_heroe_filtrado[key] = heroe[key]
        lista_filtrada.append(diccionario_heroe_filtrado)
    
    return lista_filtrada


# 4 - Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio 
# (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.
def calcular_promedio_key(lista_heroes:list, key:str):
    '''
    Recibira una lista de diccionarios, una clave y devolvera el promedio de esa clave en la lista.
    '''
    if len(lista_heroes) > 0:
        valores = []
        for heroe in lista_heroes:
            if key in heroe:
                valores.append(heroe[key])
        return sum(valores) / len(valores)
    else:
        return 0

def filtrar_key_segun_valor(lista_heroes:list, key:str) -> list:
    '''
    Recibe una lista de diccionarios y una clave, devuelve una lista filtrada segun la clave
    con la condicion de superar o ser igual a el valor 
    '''
    lista_filtrada= []
    valor = calcular_promedio_key(lista_heroes, key)
    print(valor)

    while True:
        condicion = input("Ingrese el tipo de condicion: mayor o menor \n")
        
        if condicion.lower() == "mayor" or condicion.lower() == "menor":
            break
        else:
            imprimir_dato("Opcion no valida. Intente nuevamente")

    for heroes in lista_heroes:
        if condicion == "mayor":
            if key in heroes and heroes[key] >= valor:
                diccionario_heroe_filtrado = {}
                diccionario_heroe_filtrado["nombre"] = heroes["nombre"]
                diccionario_heroe_filtrado[key] = heroes[key]
                lista_filtrada.append(diccionario_heroe_filtrado)
        else:
             if key in heroes and heroes[key] <= valor:
                diccionario_heroe_filtrado = {}
                diccionario_heroe_filtrado["nombre"] = heroes["nombre"]
                diccionario_heroe_filtrado[key] = heroes[key]
                lista_filtrada.append(diccionario_heroe_filtrado)

    return lista_filtrada


# 5 - Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx)
def buscar_filtrar_segun_key(lista_heroes:list, key:str):
    '''
    Recibe una lista de diccionarios y una clave, busca y filtra los elementos de la lista segun una clave
    que cumplan con una condicion.
    '''
    condicion_regex = re.compile(r"good|average|high")

    for heroe in lista_heroes:
        if key in heroe and condicion_regex.search(heroe[key]):
            imprimir_dato("{0}: {1}".format(heroe["nombre"], heroe[key]))


# 6 -  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4] --------------------------------------
def guardar_archivo(ruta, lista_heroes):
    '''
    Recibe una lista de diccionarios y un dato, lo guarda y devuelve un mensaje.
    '''
    with open(ruta, "w") as archivo:
        for heroes in lista_heroes:
            valores = [str(valor) for valor in heroes.values()]
            archivo.write(", ".join(valores) + "\n")


def opcion_para_guardar_archivo(opcion, lista_heroes):
    '''
    Esta funcion selecciona dependiendo la opcion que es lo que se va a guardar.
    Recibe la opcion, y a lista de heroes.
    Devuelve la lista segun la opcion elegida.
    '''

    if opcion == "1":
        lista_filtrada_y_ordenada = listar_primeros_n_elementos(lista_heroes, "2")

    elif opcion == "2":
        lista_filtrada_y_ordenada = ordenar_listar_ascendente_descendente(lista_heroes, "altura")

    elif opcion == "3":
        lista_filtrada_y_ordenada = ordenar_listar_ascendente_descendente(lista_heroes, "fuerza")

    elif opcion == "4":
        lista_filtrada_y_ordenada = filtrar_key_segun_valor(lista_heroes, "altura")

    else:
        return imprimir_dato("Error al guardar el archivo.")
    
    return lista_filtrada_y_ordenada
        

def guardar_lista_ordenada_segun_opcion(lista_heroes):
    '''
    Recibe una lista de diccionarios y una opcion, guarda la lista ordenada en un archivo csv.
    Devuelve True si se relizo correcamente, sino False.
    '''
    #opcion = stark_menu_principal_desafio_parcial()
    ruta_archivo = "/home/luli/Escritorio/programacion_1/ejercicios_stark/opcion.csv"
        
    if lista_heroes is None:
        return False
    
    retorno_del_guardardo = guardar_archivo(ruta_archivo, lista_heroes)
        
    return retorno_del_guardardo

# -------------------------------------------------------MENU------------------------------------------------------------------------------

def imprimir_menu_desafio_parcial():
    '''
    Imprime el menu de opciones
    '''
    imprimir_dato("Menú de opciones:")
    imprimir_dato("1 - Listar los primeros N héroes. El valor de N será ingresado por el usuario")
    imprimir_dato("2 - Ordenar y Listar héroes por altura. (asc o desc)")
    imprimir_dato("3 - Ordenar y Listar héroes por fuerza. (asc o desc)")
    imprimir_dato("4 - Calcular promedio de cualquier key numérica, filtrar los mayores o iguales al promedio")
    imprimir_dato("5 - Buscar héroes por inteligencia [good, average, high]")
    imprimir_dato("6 - Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]")
    imprimir_dato("0 - Salir")
    
def stark_menu_principal_desafio_parcial():
    opcion_valida = False
    
    while not opcion_valida:
        imprimir_menu_desafio_parcial()
        opcion = input("\nIngrese la opción deseada: ")
        if re.match("^[0-6]$", opcion) and len(opcion) == 1:
            opcion_valida = True
        else:
            imprimir_dato("Opcion invalida. Intente nuevamente")
        
    return opcion


def stark_marvel_app_parcial(lista_heroes):
    while True:
        # Mostrar menú de opciones
        opcion = stark_menu_principal_desafio_parcial()

        if opcion == "1":
            lista_filtrada = listar_primeros_n_elementos(lista_heroes, "2")
            imprimir_dato(lista_filtrada)

        # Opción 2:
        elif opcion == "2":
            lista_filtrada = ordenar_listar_ascendente_descendente(lista_heroes, "altura")
            imprimir_dato(lista_filtrada)
        
        # Opción 3:
        elif opcion == "3":
            lista_filtrada = ordenar_listar_ascendente_descendente(lista_heroes, "fuerza")
            imprimir_dato(lista_filtrada)

        # Opción 4:
        elif opcion == "4":
            lista_filtrada = filtrar_key_segun_valor(lista_heroes, "altura")
            imprimir_dato(lista_filtrada)
            
        # Opción 5:
        elif opcion == "5":
            buscar_filtrar_segun_key(lista_heroes, "inteligencia")
        
        # Opcion 6    
        elif opcion == "6":
            guardar_lista_ordenada_segun_opcion(lista_filtrada)
            print("opcion 6")
            
        # Opcion 0: Salir
        elif opcion == "0":
            break


#  ----------------------------------------- MAIN ---------------------------------
def main():
    stark_normalizar_datos(lista_heroes)
    stark_marvel_app_parcial(lista_heroes)

main()










