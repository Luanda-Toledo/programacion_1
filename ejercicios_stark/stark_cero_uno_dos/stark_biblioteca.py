

# Luanda Gisel Toledo Viera 
# DIV K
# DESAFIO O3

# 0
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

# 1.1
def obtener_nombre(heroe:dict):
    '''
    Recibe un diccionario y devuelve nombre en el formato especificado
    '''
    heroe = heroe["nombre"]
    return "Nombre: {0}".format(heroe)

# 1.2
def imprimir_dato(cadena_de_texto:str):
    '''
    toma un strin y lo imprime
    '''
    print(cadena_de_texto)
    
# 1.3
def stark_imprimir_nombres_heroes(lista_personajes:list):
    '''
    Toma una lista de heroes, la recorre y devuelve los nombres
    '''
    lista_heroes = stark_normalizar_datos(lista_personajes)
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre(heroe))   
    else:
        return -1
    
# 2
def obtener_nombre_y_dato(heroe:dict, texto_clave:str) -> str:
    '''
    toma un diccionario y devuelve el nombre y la clave de la llave que se indica 
    como segundo parametro.
    '''
    nombre = obtener_nombre(heroe)
    dato_a_obtener = heroe[texto_clave]
    imprimir_dato("{0} | {1}: {2}".format(nombre, texto_clave, dato_a_obtener)) 
    
# 3
def stark_imprimir_nombres_alturas(lista_personajes:list):
    '''
    toma una lista de heroes y la recorre para devolver nombre y altura 
    de cada heroe
    '''
    lista_heroes = stark_normalizar_datos(lista_personajes)
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            obtener_nombre_y_dato(heroe, "altura")
    else:
        return -1
    
''' 4.1
def calcular_max(lista_personajes, texto_clave:str):

    #toma una lista de personajes, la recorre y devuelve el heroe
    #que tiene el maximo en el texto clave ingresado

    lista_heroes = stark_normalizar_datos(lista_personajes) 
    heroe_max = lista_heroes[0]
    
    for heroe in lista_heroes:
        if heroe[texto_clave] > heroe_max[texto_clave]:
            heroe_max = heroe
            
    return heroe_max

4.2 
def calcular_min(lista_personajes, texto_clave:str):

    #toma una lista de personajes, la recorre y devuelve el heroe
    #que tiene el minimo en el texto clave ingresado

    lista_heroes = stark_normalizar_datos(lista_personajes) 
    heroe_min = lista_heroes[0]
    
    for heroe in lista_heroes:
        if heroe[texto_clave] < heroe_min[texto_clave]:
            heroe_min = heroe
            
    return heroe_min

'''
# 4.3
def calcular_max_min_dato(lista_personajes:list, texto_clave:str, calcular = "max"):
    '''
    toma una lista de heroes, los recorre y devuelve el heroe que cumple con
    la caracteristica de max o min en clave de la llave ingresada en texto_clave
    '''
    lista_heroes = stark_normalizar_datos(lista_personajes)
    heroe_buscado = lista_heroes[0]
    
    for heroe in lista_heroes:
        if calcular == "max":
            if heroe[texto_clave] > heroe_buscado[texto_clave]:
                heroe_buscado = heroe
        else:
            if heroe[texto_clave] < heroe_buscado[texto_clave]:
                heroe_buscado = heroe
                
    return heroe_buscado

# 4.4
def stark_calcular_imprimir_heroe(lista_personajes:list, tipo_calculo:str, texto_cadena:str):
    '''
    obtiene el heroe que cumpla dichas condiciones, imprime su nombre y su valor
    '''
    lista_heroes = stark_normalizar_datos(lista_personajes)
    for heroe in lista_heroes:
        if heroe == calcular_max_min_dato(lista_personajes, texto_cadena, tipo_calculo):
            nombre = heroe["nombre"]
            valor_calculado = heroe[texto_cadena]
           
    imprimir_dato("\nNombre y {2} {3}:\t {0}: {1} \n".format(
                    nombre, valor_calculado, texto_cadena, tipo_calculo))

# 5.1    
def sumar_dato_heroe(lista_personajes:list, texto_clave:str):
    '''
    toma una lista y el dato que se quiere sumar, devuelve el resultado de la suma
    '''
    lista_heroes = stark_normalizar_datos(lista_personajes)
    acumulador = 0
    for heroe in lista_heroes:
        if type(heroe) == dict:
            acumulador += heroe[texto_clave]
    
    return acumulador

# 5.2
def dividir(dividendo, divisor):
    '''
    recibe dos numeros, los divide, y devuelve el resultado
    '''
    if divisor > 0:
        return dividendo / divisor
    else:
        return 0

# 5.3 
def calcular_promedio(lista_personajes:str, dato_del_heroe:str):
    '''
    recibe una lista, un dato a calcular.
    Calcula el promedio de dicho dato y lo devuelve
    '''
    return dividir(sumar_dato_heroe(lista_personajes, dato_del_heroe), len(lista_personajes))

# 5.4
def stark_calcular_imprimir_promedio_altura(lista_personajes:list):
    if len(lista_personajes) > 0:
        promedio = calcular_promedio(lista_personajes, "altura")
        promedio = round(promedio, 2)
        imprimir_dato("El promedio de la altura de los heroes es: {0}".format(
                promedio))
    else:
        return -1
    
# 6.1
def imprimir_menu():
     # Mostrar menú de opciones
    imprimir_dato("Menú de opciones:")
    imprimir_dato("1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    imprimir_dato("2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    imprimir_dato("3. Recorrer la lista y determinar cuál es el superhéroe más alto y el mas bajo")
    imprimir_dato("4. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    imprimir_dato("5. Calcular e informar cual es el superhéroe más y menos pesado.")
    imprimir_dato("0. Salir del programa")

    
# 6.2
def validar_entero(numero_ingresado):
    if numero_ingresado.isdigit():
        return True
    else:
        return False
    
# 6.3
def stark_menu_principal():
    
    while True:
        imprimir_menu()
        opcion = input("\nIngrese la opción deseada: ")
        if validar_entero(opcion) == True:
            return int(opcion)
        else:
            return -1

# 7
def stark_marbel_app(lista_personajes):
    while True:
        opcion = stark_menu_principal()

        if opcion == 1:
                stark_imprimir_nombres_heroes(lista_personajes)

        # Opción 2:
        elif opcion == 2:
            stark_imprimir_nombres_alturas(lista_personajes)

        # Opción 3:
        elif opcion == 3:
            stark_calcular_imprimir_heroe(lista_personajes, "max", "altura")
            stark_calcular_imprimir_heroe(lista_personajes, "min", "altura")
    
        # Opción 4:
        elif opcion == 4:
            stark_calcular_imprimir_promedio_altura(lista_personajes)
            
        # Opción 5:
        elif opcion == 5:
            stark_calcular_imprimir_heroe(lista_personajes, "max", "peso")
            stark_calcular_imprimir_heroe(lista_personajes, "min", "peso")

        # Opcion 0: Salir
        elif opcion == 0:
            break

        else:
            print("Opción inválida. Intente de nuevo.")
        
           
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










