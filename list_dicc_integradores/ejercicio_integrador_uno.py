# Ejercicio integrador 1 (completo)
# Luanda Gisel Toledo Viera 
# Div H

flag_menu = True

lista_id = ["1", "2"]
lista_nombres = ["nombre1", "nombre2"]
lista_edades = ["10", "2", "4"]
lista_membresia = ["mensual", "anual"]

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
        nombre_ingresado = input("Ingrese el nombre: ")
        edad_ingresada = int(input("Ingrese la edad: "))
        membresia_ingresada = input("Ingrese el tipo de membresia: (mensual / anual) \n")
        
        for i in range(len(lista_id)):
            id_existente = int(lista_id[i])
            
            if id_existente == id_ingresado:
                print("El numero de id ya corresponde a un miembro")
                nombre_ingresado = int(input("Ingrese el numero de identificador"))
                
        lista_id.append(id_ingresado)
        lista_nombres.append(nombre_ingresado)
        lista_edades.append(edad_ingresada)
        lista_membresia.append(membresia_ingresada)
    
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        
        for i in range(len(lista_id)):
            
            mostrar_id = lista_id[i]
            mostrar_nombre = lista_nombres[i]
            mostrar_edad = lista_edades[i]
            mostrar_membresia = lista_membresia[i]
        
            print("ID: {0} \tNombre: {1} \tEdad: {2} \tTipo membresia: {3}".format(
                mostrar_id, mostrar_nombre, mostrar_edad, mostrar_membresia))
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        actualizar_id = int(input("Ingrese el numero de id del miembro para actualizar datos: "))
        flag_primer_intento_actualizar = True
        
        for i in range(len(lista_id)):
            id_existente = int(lista_id[i])
            
            if id_existente == actualizar_id:
                print("Ingrese el numero del dato que desea modificar: ")
                print("1 - ID")
                print("2 - Nombre")
                print("2 - Edad")
                print("2 - Membresia")
                opcion_actualizar = int(input("Ingrese la opcion: "))
                
                if opcion_actualizar == 1:
                    id_actualizado = int(input("Ingrese el nuevo id: "))
                    lista_id[i] = id_actualizado
                    
                elif opcion_actualizar == 2:
                    nombre_actualizar = input("Ingrese el nuevo nombre: ") 
                    lista_nombres[i] = nombre_actualizar
                
                elif opcion_actualizar == 3:
                    edad_actualizar = int(input("Ingrese la nueva edad: "))
                    lista_edades[i] = edad_actualizar
                
                elif opcion_actualizar == 4:
                    membresia_actualizar = input("Ingrese la nueva membresia: ")
                    lista_membresia[i] = membresia_actualizar
                    
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
        
        for i in range(len(lista_id)):
            id_existente_mostrar = int(lista_id[i])

            if id_existente_mostrar == id_miembro_mostrar:
                mostrar_un_id = lista_id[i]
                mostrar_un_nombre = lista_nombres[i]
                mostrar_un_edad = lista_edades[i]
                mostrar_un_membresia = lista_membresia[i]
        
                print("\n ID: {0} \tNombre: {1} \tEdad: {2} \tTipo membresia: {3} \n".format(
                mostrar_un_id, mostrar_un_nombre, mostrar_un_edad, mostrar_un_membresia))
                
                flag_primer_intento_mostrar = False
                
            else:
                if flag_primer_intento_mostrar == True:
                    print("\n \n No existe un miembro registrado con ese ID \n \n")
                    flag_primer_intento_mostrar = False
                else: 
                    pass

    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        acumulador_edad = 0
        
        for i in range(len(lista_edades)):
            indice_edad = int(lista_edades[i])
            acumulador_edad += indice_edad
        
        promedio_edades = acumulador_edad / len(lista_edades)
        print("\n El promedio de edades es de: {0} \n".format(promedio_edades))

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        flag_primer_iteracion = True
        
        for i in range(len(lista_edades)):
            indice_edad = int(lista_edades[i])
            
            if flag_primer_iteracion == True:
                edad_maxima = indice_edad
                edad_minima = indice_edad
                indice_id_edad_maxima = lista_id[i]
                indice_id_edad_minima = lista_id[i]
                flag_primer_iteracion = False
                
            else: 
                if indice_edad > edad_maxima:
                    edad_maxima = indice_edad
                    indice_id_edad_maxima = lista_id[i]
                    
                elif indice_edad < edad_minima:
                    edad_minima = indice_edad
                    indice_id_edad_minima = lista_id[i]

        print("\nEl miembro viejo tiene '{0} años', y su id es: {1}".format(
            edad_maxima, indice_id_edad_maxima))
        print("El miembro joven tiene '{0} años', y su id es: {1} \n".format(
            edad_minima, indice_id_edad_minima))

    # Opcion 0: Salir
    elif opcion == "0":
        flag_menu = False

    else:
        print("Opción inválida. Intente de nuevo.")
