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

# DESAFIO O1
# A) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F


def imprimir_por_genero(lista_personajes, genero="M"):
    lista_segun_genero = []
    for i in range(len(lista_personajes)):
        genero_del_personaje = lista_personajes[i]["genero"]
        nombre_del_personaje = lista_personajes[i]["nombre"]

        if genero == "M" and genero_del_personaje == genero:
            lista_segun_genero.append(nombre_del_personaje)
        elif genero == "F" and genero_del_personaje == genero:
            lista_segun_genero.append(nombre_del_personaje)

    return lista_segun_genero

# C) Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D) Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
# F) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
def imprimir_mas_alto_bajo_segun_genero(lista_personajes, genero, tipo):
    altura_min_personaje = 0
    altura_max_personaje = 0
    nombre_altura_min = None
    nombre_altura_max = None
    
    for personaje in lista_personajes:
        if genero == personaje["genero"]:
            altura_personaje = float(personaje["altura"])
            
            if tipo == "alto":               
                if altura_max_personaje < altura_personaje:               
                    altura_max_personaje = altura_personaje
                    nombre_altura_max = personaje["nombre"]
                
            elif tipo == "bajo":                                      
                if altura_min_personaje == 0 or altura_min_personaje > altura_personaje:                
                    altura_min_personaje = altura_personaje
                    nombre_altura_min = personaje["nombre"]
                
    return [altura_max_personaje, altura_min_personaje, nombre_altura_max, nombre_altura_min]

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


def main():
    while True:
        # Mostrar menú de opciones
        print("Menú de opciones:")
        print("1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
        print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
        print("3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
        print("4. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
        print("5. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M")
        print("6. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F")
        print("7. Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
        print("8. Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
        print("9. Determinar cuántos superhéroes tienen cada tipo de color de ojos")
        print("10. Listar todos los superhéroes agrupados por color de ojos.")
        print("11. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
        print("12. Listar todos los superhéroes agrupados por color de pelo.")
        print("13. Determinar cuántos superhéroes tienen cada tipo de inteligencia")
        print("14. Listar todos los superhéroes agrupados por tipo de inteligencia")
        print("0. Salir")
        opcion = input("\nIngrese la opción deseada: ")

        if opcion == "1":
            print("\n".join(imprimir_por_genero(lista_personajes, genero="M")))

        # Opción 2:
        elif opcion == "2":
            print("\n".join(imprimir_por_genero(lista_personajes, genero="F")))
        
        # Opción 3:
        elif opcion == "3":
            lista_info_personajes = imprimir_mas_alto_bajo_segun_genero(lista_personajes, "M", "alto")
            mas_alto_m = round(lista_info_personajes[0], 2) 
            nombre_mas_alto_m = lista_info_personajes[2]
            print("{0}, nombre: {1}".format(mas_alto_m, nombre_mas_alto_m))

        # Opción 4:
        elif opcion == "4":
            lista_info_personajes = imprimir_mas_alto_bajo_segun_genero(lista_personajes, "F", "alto")
            mas_alto_f = round(lista_info_personajes[0], 2) 
            nombre_mas_alto_f = lista_info_personajes[2]
            print("{0}, nombre: {1}".format(mas_alto_f, nombre_mas_alto_f))
            
        # Opción 5:
        elif opcion == "5":
            lista_info_personajes = imprimir_mas_alto_bajo_segun_genero(lista_personajes, "M", "bajo")
            mas_bajo_m = round(lista_info_personajes[1], 2) 
            nombre_mas_bajo_m = lista_info_personajes[3]
            print("{0}, nombre: {1}".format(mas_bajo_m, nombre_mas_bajo_m))
        
        # Opcion 6    
        elif opcion == "6":
            lista_info_personajes = imprimir_mas_alto_bajo_segun_genero(lista_personajes, "F", "bajo")
            mas_bajo_f = round(lista_info_personajes[1], 2) 
            nombre_mas_bajo_f = lista_info_personajes[3]
            print("{0}, nombre: {1}".format(mas_bajo_f, nombre_mas_bajo_f))
        
        # Opcion 7 
        elif opcion == "7":
            promedio_m = imprimir_promedio_altura_segun_genero(lista_personajes, "M")
            print("El promedio de altura segun genero Masculino es: {0}".format(round(promedio_m, 2)))
        
        # Opcion 8
        elif opcion == "8":
            promedio_f = imprimir_promedio_altura_segun_genero(lista_personajes, "F")
            print("El promedio de altura segun genero Femenino es: {0}".format(round(promedio_f, 2)))
        
        # Opcion 9
        elif opcion == "9":
            lista_info_colores = imprimir_contar_color_de_ojos(lista_personajes)
            contador_color_ojos = lista_info_colores[0]
            print(contador_color_ojos)
        
        # Opcion 10
        elif opcion == "10":
            lista_info_colores = imprimir_contar_color_de_ojos(lista_personajes)
            categoria_colores = lista_info_colores[1]
            print(categoria_colores)
        
        # Opcion 11
        elif opcion == "11":
            lista_info_colores = imprimir_contar_segun_color_pelo(lista_personajes)
            contador_color_pelo = lista_info_colores[0]
            print(contador_color_pelo)
        
        # Opcion 12
        elif opcion == "12":
            lista_info_colores = imprimir_contar_segun_color_pelo(lista_personajes)
            categoria_colores = lista_info_colores[1]
            print(categoria_colores)
        
        # Opcion 13
        elif opcion == "13":
            lista_info_inteligencia = imprimir_contar_segun_tipo_inteligencia(lista_personajes)
            contador_tipo_inteligencia = lista_info_inteligencia[0]
            print(contador_tipo_inteligencia)
        
        # Opcion 14
        elif opcion == "14":
            lista_info_inteligencia = imprimir_contar_segun_tipo_inteligencia(lista_personajes)
            categorias_tipo_inteligencia = lista_info_inteligencia[1]
            print(categorias_tipo_inteligencia)

        # Opcion 0: Salir
        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

main()