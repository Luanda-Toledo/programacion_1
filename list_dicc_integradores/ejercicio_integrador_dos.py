# Ejercicio integrador 2 (completo)
# Luanda Gisel Toledo Viera 
# Div H

flag_menu = True
lista_de_miembros = [{"id" : 100, "nombre" : "nombre1", "edad" : 6, "membresia": "mensual"},
                     {"id" : 200, "nombre" : "nombre2", "edad" : 10, "membresia": "anual"}]

while flag_menu == True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        
        id_ingresado = int(input("Ingrese el numero de identificador: "))
        
        for i in range(len(lista_de_miembros)):
            id_existente = int(lista_de_miembros[i]["id"])
            
            if id_existente == id_ingresado:
                print("\n El numero de id ya corresponde a un miembro \n")
                nombre_ingresado = int(input("Ingrese el numero de identificador: "))
                break
                        
        nombre_ingresado = input("Ingrese el nombre: ")
        edad_ingresada = int(input("Ingrese la edad: "))
        membresia_ingresada = input("Ingrese el tipo de membresia: (mensual / anual) \n")
                
        nuevo_miembro = {}
        nuevo_miembro["id"] = id_ingresado
        nuevo_miembro["nombre"] = nombre_ingresado
        nuevo_miembro["edad"] = edad_ingresada
        nuevo_miembro["membresia"] = membresia_ingresada
        
        lista_de_miembros.append(nuevo_miembro)
    
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        
        for i in range(len(lista_de_miembros)):
            miembros = lista_de_miembros[i]
            print("Lista de miembros: \n {0}".format(miembros))
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
                
        actualizar_id = int(input("Ingrese el numero de id del miembro para actualizar datos: "))
        flag_primer_intento_actualizar = True
        
        for i in range(len(lista_de_miembros)):
            id_existente = int(lista_de_miembros[i]["id"])
            
            if id_existente == actualizar_id:
                print("Ingrese el numero del dato que desea modificar: ")
                print("1 - ID")
                print("2 - Nombre")
                print("2 - Edad")
                print("2 - Membresia")
                opcion_actualizar = int(input("Ingrese la opcion: "))
                
                if opcion_actualizar == 1:
                    id_actualizado = int(input("Ingrese el nuevo id: "))
                    lista_de_miembros[i]["id"] = id_actualizado
                    
                elif opcion_actualizar == 2:
                    nombre_actualizar = input("Ingrese el nuevo nombre: ") 
                    lista_de_miembros[i]["nombre"] = nombre_actualizar
                
                elif opcion_actualizar == 3:
                    edad_actualizar = int(input("Ingrese la nueva edad: "))
                    lista_de_miembros[i]["edad"] = edad_actualizar
                
                elif opcion_actualizar == 4:
                    membresia_actualizar = input("Ingrese la nueva membresia: ")
                    lista_de_miembros[i]["membresia"] = membresia_actualizar
                    
            else: 
                
                if flag_primer_intento_actualizar == True:
                    print("\n \n No existe un miembro registrado con ese ID \n \n")
                    flag_primer_intento_actualizar = False
                else: 
                    pass

    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id_miembro_mostrar = int(input("Ingrese el ID del miembro: "))
        flag_primer_intento_mostrar = True
        
        for i in range(len(lista_de_miembros)):
            id_existente_mostrar = int(lista_de_miembros[i]["id"])

            if id_existente_mostrar == id_miembro_mostrar:
                mostrar_miembro = lista_de_miembros[i]
                print("\n {0} \n".format(mostrar_miembro))
  
                flag_primer_intento_mostrar = False                
            else:
                if flag_primer_intento_mostrar == True:
                    print("\n \n No existe un miembro registrado con ese ID \n \n")
                    flag_primer_intento_mostrar = False
                
    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        acumulador_edad = 0
        
        for i in range(len(lista_de_miembros)):
            indice_edad = int(lista_de_miembros[i]["edad"])
            acumulador_edad += indice_edad
        
        promedio_edades = acumulador_edad / len(lista_de_miembros)
        print("\n El promedio de edades es de: {0} \n".format(promedio_edades))

   #  Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        pass
        flag_primer_iteracion = True
        
        for i in range(len(lista_de_miembros)):
            indice_edad = int(lista_de_miembros[i]["edad"])
            
            if flag_primer_iteracion == True:
                edad_maxima = indice_edad
                edad_minima = indice_edad
                indice_id_edad_maxima = lista_de_miembros[i]["id"]
                indice_id_edad_minima = lista_de_miembros[i]["id"]
                indice_nombre_edad_maxima = lista_de_miembros[i]["nombre"]
                indice_nombre_edad_minima = lista_de_miembros[i]["nombre"]
                flag_primer_iteracion = False
                
            else: 
                if indice_edad > edad_maxima:
                    edad_maxima = indice_edad
                    indice_id_edad_maxima = lista_de_miembros[i]["id"]
                    indice_nombre_edad_maxima = lista_de_miembros[i]["nombre"]
                    
                elif indice_edad < edad_minima:
                    edad_minima = indice_edad
                    indice_id_edad_minima = lista_de_miembros[i]["id"]
                    indice_nombre_edad_minima = lista_de_miembros[i]["nombre"]

        print("\nEl miembro viejo se llama '{2}', tiene '{0} años' y su id es: {1}".format(
            edad_maxima, indice_id_edad_maxima, indice_nombre_edad_maxima))
        print("El miembro joven se llama '{2}', tiene '{0} años' y su id es: {1} \n".format(
            edad_minima, indice_id_edad_minima, indice_nombre_edad_minima))

    # Opcion 0: Salir
    elif opcion == "0":
        flag_menu = False

    else:
        print("Opción inválida. Intente de nuevo.")