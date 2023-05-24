# Ejercicios 1 -------------------------------------
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista_de_numeros:
    if not(i % 2 == 0):
        print(i)

# Ejercicio 2 -------------------------------------
lista_numeros_enteros = [1, 2, 3, 4, 5]
nuevo_numero_ingresado = int(input("Ingrese un numero: "))

lista_numeros_enteros[2] = nuevo_numero_ingresado
print(lista_numeros_enteros)

# Ejercicio 3 -------------------------------------
lista_numeros_ingresados = []
acumulador_ingresados = 0

while True:
    numero_ingresado = int(input("Ingrese un numero: "))
    
    if numero_ingresado < 0:
        break
    
    lista_numeros_ingresados.append(numero_ingresado)
    acumulador_ingresados += numero_ingresado
    
print(acumulador_ingresados)

# Ejercicio 4 -------------------------------------
lista_de_caracteres = []

while True:
    palabra_ingresada = input("Ingrese una palabra: ")
    primera_letra = palabra_ingresada[0]
    
    if primera_letra == "z" or primera_letra == "Z":
        print("Ingreso una palabra que comienza con la letra 'z' ")
        break
    
    print("Primera letra: {0}".format(primera_letra))
    
# Ejercicio 5 -------------------------------------
lista_de_ciudades = ["Ciudad1", "Ciudad2", "Ciudad3", "Ciudad4", "Ciudad5"]
ultimo_elemento = len(lista_de_ciudades) - 1
print(lista_de_ciudades[ultimo_elemento])

# Ejercicio 6 -------------------------------------
lista_numeros_enteros = [1, 2, 3]
lista_numeros_enteros.append(1)
print(lista_numeros_enteros)

# Ejercicio 7 -------------------------------------
lista_deportes = ["deporte1", "deporte2", "deporte3"]
lista_deportes.append("deporte4")
print(lista_deportes)

# Ejercicio 8 -------------------------------------
lista_libros = ["Libro1", "Libro2", "Libro3", "Libro4", "Libro5"]
lista_tres_primeros = []
lista_tres_primeros.append(lista_libros[0])
lista_tres_primeros.append(lista_libros[1])
lista_tres_primeros.append(lista_libros[2])
print(lista_tres_primeros)

# Ejercicio 9 -------------------------------------
lista_numeros = [1, 2, 3, 3]
flag_encontrado = False

numero_ingresado = int(input("Ingrese un numero: "))
lista_numeros.append(numero_ingresado)

posicion_nuevo_numero = len(lista_numeros) - 1
numero_nuevo_de_la_lista = lista_numeros[posicion_nuevo_numero] 

print("El nuevo numero es: {0}, y se encuentra en la posicion: {1}".format(
    numero_nuevo_de_la_lista, posicion_nuevo_numero))

for i in lista_numeros:
    elementos = lista_numeros[i - 1]
    
    if not(numero_ingresado == elementos):
        
        if i == len(lista_numeros) - 1:
            print("El numero NO se repite en la lista.")
            flag_encontrado == True

# Ejercicio 10 -------------------------------------
lista_de_palabras = ["Hola", "No", "Tengo hambre", "Dormir"]

for i in lista_de_palabras:
    if ( len(i) - 1 > 4) :
        print(i)

# Ejercicio 11 -------------------------------------
lista_de_palabras = ["Hola", "No", "Tengo hambre", "Dormir", "Comer", "Dormir"]
palabra_ingresada = input("Ingrese una palabra: ")
cantidad_caracteres = len(palabra_ingresada)
flag_no_encontrado = False
contador_coincidencias = 0
contador_iteraciones = 0

for i in lista_de_palabras:
    
    contador_iteraciones += 1
    
    if ( len(i) == cantidad_caracteres):
        contador_coincidencias += 1
        flag_no_encontrado = True
        
    if contador_iteraciones == len(lista_de_palabras):
        if flag_no_encontrado == False:
            print("No se encontro una palabra con la misma longitud")
        else:
            print("La palabra: {0}. Coincide en longitud con {1} palabra/s de la lista".format(
                palabra_ingresada, contador_coincidencias))

# Ejercicio 12 -------------------------------------
lista_peliculas = ["pelicula1", "pelicula2", "pelicula3"]

for i in range(len(lista_peliculas) - 1, -1, -1):
    print(lista_peliculas[i])
    
# Ejercicio 13 -------------------------------------
lista_de_numeros = [1, 2, 3, 4, 5]
suma_de_numeros = 0
elementos_de_la_lista = len(lista_de_numeros)

for i in lista_de_numeros:
    suma_de_numeros += i

promedio = suma_de_numeros / elementos_de_la_lista
print(promedio)

# Ejercicio 14 -------------------------------------
primera_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
segunda_lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
resultado = []

for i in range(len(primera_lista)):
    multiplicacion = primera_lista[i] * segunda_lista[i]
    
    resultado.append(multiplicacion)
    
print(resultado, end = " ")

# Ejercicio 15 -------------------------------------
lista_numeros_enteros = [1, 2, 3, 4, 5, 6]
suma_de_impares = 0

for i in range(len(lista_numeros_enteros)):
    
    if not(i % 2 == 0):
        
        elemento_de_la_lista = lista_numeros_enteros[i]
        suma_de_impares += elemento_de_la_lista

print("La suma de los numeros indices impares es: {0}".format(suma_de_impares))

# Ejercicio 16 -------------------------------------
lista_numeros = [1, 2, 3]
lista_caracteres = ["a", "b", "c"]
lista_combinada = []

for i in range(len(lista_numeros)):
    
    numero = lista_numeros[i]
    caracter = lista_caracteres[i]
    
    lista_combinada.append(numero)
    lista_combinada.append(caracter)
    
print(lista_combinada)

# Ejercicio 17 -------------------------------------
primera_lista = [1, 2, 3, 4, 5]
segunda_lista = [4, 5, 6, 7, 8]

for i in range(len(primera_lista)):
    
    primer_numero = primera_lista[i]
    
    for j in segunda_lista:
        
        if primer_numero == j:
            print(primer_numero)
            
# Ejercicio 18 -----------------------------------
lista_de_numeros = []
flag_primera_vez = True
respuesta = "si"

while respuesta == "si":
    
    numero_ingresado = int(input("Ingrese un numero: "))
    
    if numero_ingresado == 0:
        respuesta = "no"
        
    lista_de_numeros.append(numero_ingresado)
    
    for i in lista_de_numeros:
    
        if flag_primera_vez == True:
        
            numero_mayor = i
            flag_primera_vez = False
        
        else:
            if i > numero_mayor:
                numero_mayor = i
    
print("Los numeros ingresados son: {0}. Y el numero mayor es: {1}".format(lista_de_numeros, numero_mayor))

# Ejercicio 19 -----------------------------------
lista_de_palabras = []
lista_errores = [" ", "", "  "]

while len(lista_de_palabras) < 5:
    
    palabra_ingresada = input("Ingrese una palabra: ").capitalize()
    
    if palabra_ingresada not in lista_de_palabras and palabra_ingresada not in lista_errores:
        
        lista_de_palabras.append(palabra_ingresada)
    
    else: 
        print("Ingrese una palabra que no haya sido ingresada aun")
        
print("La lista de palabras ingresadas es: {0}".format(lista_de_palabras))

# Ejercicio 20 -----------------------------------
lista_de_numeros = [1, 80, 5, 0, 15, -5, 1, 79]
flag_primera_vez = True
suma_de_numeros = 0

for i in lista_de_numeros:
    
    suma_de_numeros += i
    
    if flag_primera_vez == True:
        
        numero_mayor = i
        numero_menor = i
        flag_primera_vez = False
        
    else:
        if i > numero_mayor:
            numero_mayor = i
        if i < numero_menor:
            numero_menor = i
            

promedio = suma_de_numeros / len(lista_de_numeros)
               
print("El numero mayor es: {0} \nEl numero menor es: {1}".format(numero_mayor, numero_menor))
print("El promedio es: {0} \nLa suma total de los elementos es: {1}".format(promedio, suma_de_numeros))

# Ejercicio 21 -----------------------------------
lista_precios_unitarios = []
lista_de_cantidades = []
contador = 0

while len(lista_precios_unitarios) < 5:
    
    precio_ingresado = int(input("Ingrese el precio unitario del producto: "))
    cantidad_ingresada = int(input("Ingrese la cantidad de producto: "))
    lista_precios_unitarios.append(precio_ingresado)
    lista_de_cantidades.append(cantidad_ingresada)

for i in range(len(lista_precios_unitarios)):
    
    multiplicacion = lista_precios_unitarios[i] * lista_de_cantidades[i]
    contador += 1
    
    print("Precio total Articulo {1}: ${0}".format(multiplicacion, contador))
    
# Ejercicio 22
lista_productos = []
lista_precio_unitario = []
lista_cantidades = []
lista_totales = []
flag = True

while flag == True:
    
    producto_ingresado = input("Ingrese el nombre del producto: ")
    
    if producto_ingresado == "xxx":
        flag = False
    else: 
        lista_productos.append(producto_ingresado)
    
        precio_unitario_ingresado = int(input("Ingrese el precio unitario: "))
        lista_precio_unitario.append(precio_unitario_ingresado)

        cantidad_ingresada = int(input("Ingrese la cantidad: "))
        lista_cantidades.append(cantidad_ingresada)
    
for i in range(len(lista_precio_unitario)):
    
    multiplicacion = lista_precio_unitario[i] * lista_cantidades[i]
    lista_totales.append(multiplicacion)
    
    nombre_producto = lista_productos[i]
    precio_unitario = lista_precio_unitario[i]
    cantidades = lista_cantidades[i]
    precio_total = lista_totales[i]
    
    print("{0}  {1}  ${2}  ${3}".format(nombre_producto, cantidades, precio_unitario, precio_total))




