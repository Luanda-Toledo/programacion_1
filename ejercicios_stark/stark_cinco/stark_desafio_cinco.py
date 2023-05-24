from biblioteca_funciones_genericas import *
import re

# Luanda Gisel Toledo Viera
# DIV K
# DESAFIO O3

# ----------------------------- NORMALIZAR DATOS - IMPRIMIR DATOS ---------------------------------------------
def stark_normalizar_datos(lista_personajes:list):
    '''
    Convertir al tipo de dato correcto las keys en caso de ser necesario, 
    mostrar si se normalizaron los datos y devolver la lista de datos normalizada
    '''
    flag_modificado = False
    if len(lista_personajes) > 0:
        for diccionarios in lista_personajes:
            for elementos in diccionarios:
                llave = diccionarios.get(elementos)
                if type(llave) == str:
                    if "." in llave:
                        diccionarios[elementos] = float(llave)
                        flag_modificado = True
                    elif llave.isdigit():
                        diccionarios[elementos] = int(llave)
                        flag_modificado = True
    else:
        return print("Error: Lista de heroes vacia")
                        
    if flag_modificado == True:
        print("Datos normalizados")
        
    return lista_personajes

def imprimir_dato(cadena_de_texto:str):
    '''
    toma un strin y lo imprime
    '''
    print(cadena_de_texto)

# --------------------- OPCIONES DEL MENU DESDE LA "A" A LA "N"---------------------------------------------------------
def imprimir_por_genero(lista_personajes, genero):
    '''
    Recibe una lista de diccionarios, y el genero.
    Guarda en una nueva lista los heroes que coincidan con el genero pasado por parametro.
    Devuelve la lista de heroes segun genero.
    '''
    lista_segun_genero = []
    for i in range(len(lista_personajes)):
        genero_del_personaje = lista_personajes[i]["genero"]
        nombre_del_personaje = lista_personajes[i]["nombre"]

        if genero == "M" and genero_del_personaje == genero:
            lista_segun_genero.append(nombre_del_personaje)
        elif genero == "F" and genero_del_personaje == genero:
            lista_segun_genero.append(nombre_del_personaje)

    return lista_segun_genero

# G) Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# H) Recorrer la lista y determinar la altura promedio de los superhéroes de género F
def imprimir_promedio_altura_segun_genero(lista_personajes, genero):
    acumulador_altura = 0
    contador_personajes = 0
    
    for personajes in lista_personajes:
        
        if genero == personajes["genero"]:
            acumulador_altura += float(personajes["altura"])
            contador_personajes += 1
    
    print(acumulador_altura)
    print(contador_personajes)
            
    return acumulador_altura / contador_personajes

# I) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores 
# (ítems C a F) ok cada item ya tiene asociado su nombre

# J) Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# M) Listar todos los superhéroes agrupados por color de ojos.
def imprimir_contar_color_de_ojos(lista_personajes):
    colores_de_ojos = {}
    superheroes_por_color = {}

    for personaje in lista_personajes:
        color = personaje["color_ojos"]
        
        if color in colores_de_ojos:
            colores_de_ojos[color] += 1
        else:
            colores_de_ojos[color] = 1

        if color in superheroes_por_color:
            superheroes_por_color[color].append(personaje["nombre"])
        else:
            superheroes_por_color[color] = [personaje["nombre"]]

    return [colores_de_ojos, superheroes_por_color]
    

# K) Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# N) Listar todos los superhéroes agrupados por color de pelo.
def imprimir_contar_segun_color_pelo(lista_personajes):
    colores_de_pelo = {}
    supeheroes_por_color_pelo = {}
    
    for personajes in lista_personajes:
        color_pelo = personajes["color_pelo"]
        
        if color_pelo == "":
            color_pelo = "No tiene"
        
        if color_pelo in colores_de_pelo:
            colores_de_pelo[color_pelo] += 1 
        else:
            colores_de_pelo[color_pelo] = 1 
            
        if color_pelo in supeheroes_por_color_pelo:
            supeheroes_por_color_pelo[color_pelo].append(personajes["nombre"])
        else:
            supeheroes_por_color_pelo[color_pelo] = [personajes["nombre"]]          
            
    return [colores_de_pelo, supeheroes_por_color_pelo]        
        
# L) Determinar cuántos superhéroes tienen cada tipo de inteligencia 
# (En caso de no tener, Inicializarlo con ‘No Tiene’). 
# O) Listar todos los superhéroes agrupados por tipo de inteligencia
def imprimir_contar_segun_tipo_inteligencia(lista_personajes):
    tipos_inteligencia = {}
    supeheroes_por_tipo_inteligencia = {}
    
    for personajes in lista_personajes:
        inteligencia = personajes["inteligencia"]
        
        if inteligencia == "":
            inteligencia = "No tiene"
        
        if inteligencia in tipos_inteligencia:
            tipos_inteligencia[inteligencia] += 1
        else:
            tipos_inteligencia[inteligencia] = 1

        if inteligencia in supeheroes_por_tipo_inteligencia:
            supeheroes_por_tipo_inteligencia[inteligencia].append(personajes["nombre"])
        else: 
            supeheroes_por_tipo_inteligencia[inteligencia] = [personajes["nombre"]]
            
    return [tipos_inteligencia, supeheroes_por_tipo_inteligencia]

# ---------------------------------------------- 1 ---------------------------------------------------
def leer_archivo(ruta:str)->str:
    '''
    recibe como parametro la ruta del archivo que se quiere leer
    abre, lee y cierra el archivo 
    retorna las lineas del archivo en un print
    '''
    import json
    with open(ruta, 'r') as archivo:
        contenido = json.load(archivo)
    return contenido['heroes']
lista_personajes = leer_archivo("/home/luli/Escritorio/programacion_1/ejercicios_stark/data_stark.json")

def guardar_archivo(archivo:str, dato):
    '''
    Recibe la ruta donde se guardara el archivo, y los datos que seran guardados en esa ruta.
    Sino existe el archivo lo crea.
    Devuelve un mensaje en caso de que se guarde correctamente o no.
    '''
    with open(archivo, "w+") as archivo:
        archivo.write(dato)
        if len(dato) == 0:
            mensaje = f"Error al crear el archivo {archivo}"
        else: 
            mensaje = f"Se creo el archivo: {archivo}"
    return mensaje 

def capitalizar_palabras(cadena_texto:str):
    '''
    Recibe una cadena de texto.   
    Devuelve una nueva cadena con todas las palabras capitalizadas.
    '''
    lista = cadena_texto.split()
    cadena_texto_nueva = []

    for palabra in lista:
            cadena_texto_nueva.append(palabra.capitalize())
    return " ".join(cadena_texto_nueva)

def obtener_nombre_capitalizado(diccionario:dict) -> str:
    '''
    Recibe un diccionario. Obtiene el nombre, lo capitaliza.
    Y lo devuelve.
    '''
    mensaje = "Nombre: {0}".format(capitalizar_palabras(diccionario["nombre"]))
    return mensaje

def obtener_nombre_y_dato(diccionario:dict, clave:str):
    '''
    Recibe el diccionario, y una string que sera una clave del diccionario.
    Toma el nombre, y la clave para obtener su valor.
    Imprime un mensaje con los datos obtenidos.
    '''
    mensaje = "{0} | {1}: {2}".format(obtener_nombre_capitalizado(diccionario), clave, diccionario[clave])
    return mensaje

# --------------------------------------------------------  2  --------------------------------------------------------------
#2.1
def es_genero(diccionario:dict, genero:str):
    '''
    Recibe un diccionario, y un string.
    Compara si la clave del diccionario coicide con el genero.
    Devulve True si coinciden, o False en caso contrario.
    '''
    if diccionario["genero"] == genero:
        return True 
    else:
        return False
    
#2.2 
def stark_guardar_heroe_genero(lista_heroes:list, genero:str) -> str:
    '''
    Recibe una lista de diccionarios, y un string que sera el genero.
    Guarda en un archivo csv todos los heroes que coincidan con dicho genero.
    Devvulve True si se guardo correctamente, o false en caso contrario.
    '''
    ruta_archivo = "/home/luli/Escritorio/programacion_1/ejercicios_stark/stark_cinco/genero{0}.csv".format(genero)
    lista_genero = []
    separador = ", "

    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            obtener_nombre_capitalizado(heroe)
            lista_genero.append(heroe["nombre"])
    cadena_nombres = separador.join(lista_genero)
        
    if guardar_archivo(ruta_archivo, cadena_nombres):
        return True
    else: 
        return False   

# ------------------------------------------------ 3 ----------------------------------------------------------------------
#3.1
def calcular_min(lista_heroes:list, genero:str, tipo:str) -> dict:
    '''
    Recibe la lista de diccionarios, el genero y el tipo (clave).
    Calcula el minimo segun lo indicado en los parametros y devulve
    el diccionario que contine el valor minimo.
    '''
    lista_heroes = stark_normalizar_datos(lista_heroes)
    flag_genero = False
    indice_min = None

    for indice_heroe in range(len(lista_heroes)):
        if es_genero(lista_heroes[indice_heroe], genero):
            
            if not flag_genero:
                indice_min = indice_heroe
                flag_genero = True

            if lista_heroes[indice_heroe][tipo] < lista_heroes[indice_min][tipo]:
                indice_min = indice_heroe
        
    if indice_min is not None:
        return lista_heroes[indice_min]
    else:
        return None

#3.2
def calcular_max(lista_heroes:list, genero:str, tipo:str) -> dict:
    '''
    Recibe la lista de diccionarios, el genero y el tipo (clave).
    Calcula el maximo segun lo indicado en los parametros y devulve
    el diccionario que contine el valor maximo.
    '''
    lista_heroes = stark_normalizar_datos(lista_heroes)
    flag_genero = False
    indice_min = None

    for indice_heroe in range(len(lista_heroes)):
        if es_genero(lista_heroes[indice_heroe], genero):
            
            if not flag_genero:
                indice_min = indice_heroe
                flag_genero = True

            if lista_heroes[indice_heroe][tipo] > lista_heroes[indice_min][tipo]:
                indice_min = indice_heroe
        
    if indice_min is not None:
        return lista_heroes[indice_min]
    else:
        return None

#3.3 
def calcular_min_max_dato_genero(lista_heroes: list, genero: str, tipo: str, es_min: bool) -> dict:
    '''
    Recibe una lista de diccionarios, el genero, tipo (clave), y el valor booleano que indicara
    si se debe calcular el min o max. Llama a la funcion que corresponde y devuelve el diccionario
    que corresponde segun la opcion elegida.
    '''
    if es_min:
        resultado = calcular_min(lista_heroes, genero, tipo)
    else:
        resultado = calcular_max(lista_heroes, genero, tipo)

    return resultado

#3.4
def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list, tipo_calculo:str, clave:str, genero:str): 
    '''
    Obtiene el héroe o heroína que cumpla con las condiciones, imprime su nombre y su valor, 
    y guarda el resultado en un archivo CSV.
    '''
    heroe = calcular_min_max_dato_genero(lista_heroes, clave, tipo_calculo, genero)

    mensaje = obtener_nombre_y_dato(heroe, clave)
    imprimir_dato(mensaje)

    archivo = "/home/luli/Escritorio/programacion_1/ejercicios_stark/stark_cinco/heroes{0}_{1}_{2}.csv".format(tipo_calculo, clave, genero)
    resultado = guardar_archivo(archivo, mensaje)

    if resultado:
        return True
    else:
        return False
    
# ------------------------------------------------- 4 --------------------------------------------------------
#4.1
def sumar_dato_heroe_genero(lista_heroes:list, texto_clave:str, genero:str):
    '''
    Toma una lista de diccionarios, la clave, el genero y los suma segun las 
    especificaciones pasadas por parametro.
    Devuelve el resultado de la suma.
    '''
    acumulador = 0
    for heroe in lista_heroes:
        if type(heroe) == dict and bool(heroe): # Bool devuelve False si el diccionario esta vacio
            if heroe[texto_clave] == genero:
                acumulador += heroe[texto_clave] 

    if acumulador > 0:
        return acumulador
    else:
        return -1
    
#4.2
def cantidad_heroes_genero(lista_heroes:list, genero:str):
    pass































# -------------------------------------- MENU - APP - MAIN ----------------------------------------------
def imprimir_menu_desafio_5():
    '''
    Imprime el menu de opciones
    '''
    imprimir_dato("Menú de opciones:")
    imprimir_dato("A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    imprimir_dato("B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    imprimir_dato("C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    imprimir_dato("D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    imprimir_dato("E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    imprimir_dato("F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    imprimir_dato("G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    imprimir_dato("H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    imprimir_dato("I. Determinar cuántos superhéroes tienen cada tipo de color de ojos")
    imprimir_dato("J. Listar todos los superhéroes agrupados por color de ojos.")
    imprimir_dato("K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    imprimir_dato("L. Listar todos los superhéroes agrupados por color de pelo.")
    imprimir_dato("M. Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    imprimir_dato("N. Listar todos los superhéroes agrupados por tipo de inteligencia")
    imprimir_dato("O. Salir")

def stark_menu_principal_desafio_5():
    '''
    Valida la opcion ingresada y la devuelve si es correcta.
    '''
    opcion_valida = False
    
    while not opcion_valida:
        imprimir_menu_desafio_5()
        opcion = input("\nIngrese la opción deseada: ")
        if re.match("^[a-oA-O]$", opcion) and len(opcion) == 1:
            opcion_valida = True
        else:
            imprimir_dato("Opcion invalida. Intente nuevamente")
    return opcion


def stark_marvel_app_5(lista_personajes):
    '''
    Recibe como parametro la lista de diccionarios, Muestra el menu y
    contenido que corresponda segun la opcion seleccionada.
    '''

    while True:
        # Mostrar menú de opciones
        opcion = stark_menu_principal_desafio_5()

        if opcion == "A":
            mensaje = "\n".join(imprimir_por_genero(lista_personajes, genero="M"))
            imprimir_dato(mensaje)

        # Opción 2:
        elif opcion == "B":
            mensaje = "\n".join(imprimir_por_genero(lista_personajes, genero="F"))
            imprimir_dato(mensaje)
        
        # Opción 3:
        elif opcion == "C": #MAX
            diccionario_info_personajes = calcular_min_max_dato_genero(lista_personajes, "M", "altura", False)
            nombre_mas_alto_m = diccionario_info_personajes["nombre"]
            mensaje = "Nombre: {0}".format(nombre_mas_alto_m)
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "M", "altura", False))
            imprimir_dato(mensaje)

        # Opción 4:
        elif opcion == "D": # MAX
            diccionario_info_personajes = calcular_min_max_dato_genero(lista_personajes, "F", "altura", False)
            nombre_mas_alto_f = diccionario_info_personajes["nombre"]
            mensaje = "Nombre: {0}".format(nombre_mas_alto_f)
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "F", "altura", False))
            imprimir_dato(mensaje)
            
        # Opción 5:
        elif opcion == "E": #MIN
            info_personajes = calcular_min_max_dato_genero(lista_personajes, "M", "altura", True) 
            nombre_mas_bajo_m = info_personajes["nombre"]
            mensaje = "Nombre: {0}".format(nombre_mas_bajo_m)
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "M", "altura", True))
            imprimir_dato(mensaje)        

        # Opcion 6    
        elif opcion == "F": #MIN
            info_personajes = calcular_min_max_dato_genero(lista_personajes, "F", "altura", True)
            nombre_mas_bajo_f = info_personajes["nombre"]
            mensaje = "Nombre: {0}".format(nombre_mas_bajo_f)
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "F", "altura", True))
            imprimir_dato(mensaje)
        
        # Opcion 7 
        elif opcion == "G":
            promedio_m = imprimir_promedio_altura_segun_genero(lista_personajes, "M")
            mensaje = "El promedio de altura segun genero Masculino es: {0}".format(round(promedio_m, 2))
            imprimir_dato(mensaje)
        
        # Opcion 8
        elif opcion == "H":
            promedio_f = imprimir_promedio_altura_segun_genero(lista_personajes, "F")
            mensaje = "El promedio de altura segun genero Femenino es: {0}".format(round(promedio_f, 2))
            imprimir_dato(mensaje)
        
        # Opcion 9
        elif opcion == "I":
            lista_info_colores = imprimir_contar_color_de_ojos(lista_personajes)
            contador_color_ojos = lista_info_colores[0]
            imprimir_dato(contador_color_ojos)
        
        # Opcion 10
        elif opcion == "J":
            lista_info_colores = imprimir_contar_color_de_ojos(lista_personajes)
            categoria_colores = lista_info_colores[1]
            imprimir_dato(categoria_colores)
        
        # Opcion 11
        elif opcion == "K":
            lista_info_colores = imprimir_contar_segun_color_pelo(lista_personajes)
            contador_color_pelo = lista_info_colores[0]
            imprimir_dato(contador_color_pelo)
        
        # Opcion 12
        elif opcion == "L":
            lista_info_colores = imprimir_contar_segun_color_pelo(lista_personajes)
            categoria_colores = lista_info_colores[1]
            imprimir_dato(categoria_colores)
        
        # Opcion 13
        elif opcion == "M":
            lista_info_inteligencia = imprimir_contar_segun_tipo_inteligencia(lista_personajes)
            contador_tipo_inteligencia = lista_info_inteligencia[0]
            imprimir_dato(contador_tipo_inteligencia)
        
        # Opcion 14
        elif opcion == "N":
            lista_info_inteligencia = imprimir_contar_segun_tipo_inteligencia(lista_personajes)
            categorias_tipo_inteligencia = lista_info_inteligencia[1]
            imprimir_dato(categorias_tipo_inteligencia)

        # Opcion 0: Salir
        elif opcion == "O":
            break

def main():
    #Ejecuta la app
    stark_normalizar_datos(lista_personajes)
    stark_marvel_app_5(lista_personajes)

main()

"""
    Funcion: muestra y devuelve el dato y atributo de un heroe de la lista
    Recibe: un heroe del diccionario y un atributo cualquiera del diccionario de ese heroe
    Devuelve: el nombre y el dato de ese heroe en un formato especifico
"""