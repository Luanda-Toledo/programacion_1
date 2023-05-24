# Ejercicio 1
# Crea un diccionario que represente los días de la semana, donde las claves
# son los nombres de los días y los valores son los números correspondientes
# (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al
# día "miércoles".
diccionario_dias = {"lunes": 1, "martes": 2, "miercoles": 3, "jueves": 4,
                    "viernes": 5, "sabado": 6, "domingo": 7}

print(diccionario_dias["miercoles"])

# Ejercicio 2
#  Crea un diccionario que represente los meses del año, donde las claves son
# los nombres de los meses y los valores son sus núm correspondientes
# (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el núm correspondiente
# al mes "julio"
diccionario_meses = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, 
                     "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9, 
                     "octubre": 10, "noviembre": 11, "diciembre": 12}

print(diccionario_meses["julio"])

# Ejercicio 3
# Crea un diccionario que contenga la información de una película, como título,
# director y año de estreno. Luego, imprime el título de la película.
diccionario_peliculas = {"titulo": "pelicula1", "director": "director1", "año de estreno": "año1"}

print(diccionario_peliculas["titulo"])        

# Ejercicio 4
# Crea un diccionario que contenga la información de una dirección: nombre de
# la calle, altura, localidad, código postal, partido y provincia. Luego, imprime el
# nombre de la calle, seguido de su altura.
dic_direccion = {"nombre": "nombre_calle", "altura": 1, "localidad": "localidad1",
                 "codigo postal": 1, "partido": "partido1", "provincia": "provincia1"}

nombre_calle = dic_direccion["nombre"]
altura_calle = dic_direccion["altura"]
print("El nombre de la calle es '{0}', y la altura es '{1}'.".format(
    nombre_calle, altura_calle))

# Ejercicio 5
# Crea un diccionario que represente los continentes, donde las claves son los
# nombres de los continentes y los valores son los números correspondientes
# (por ejemplo, {"América": 1, "Europa": 2, ...}). Imprime el valor correspondiente
# al continente "África".
dic_continentes = {"America": 1, "Europa": 2, "Africa": 3, "Asia": 4,
                   "Antartida": 5, "Oceania": 6}

print(dic_continentes["Africa"])

# Ejercicio 6
# Crea un diccionario que represente las estaciones del año, donde las claves
# son los nombres de las estaciones y los valores son los números
# correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el
# valor correspondiente a la estación "invierno".
dic_estaciones_del_año = {"verano": 1, "primavera": 2, "invierno": 3, "otoño": 4}

print(dic_estaciones_del_año["invierno"])

# Ejercicio 7
# Crea un diccionario que contenga la información de una canción: título, artista
# y duración. Luego, imprime la duración de la canción.
dic_cancion = {"tirulo": "titulo1", "artista": "artista1", "duracion": 100}

print(dic_cancion["duracion"])

# Ejercicio 8
# Crea un diccionario que represente las edades de varias personas, donde las
# claves son los nombres de las personas y los valores son sus edades.
# Imprime la edad de la persona más joven.
dic_personas = {"nombre1": 11, "nombre2": 22, "nombre3": 33, "nombre4": 44}

# min() para obtener el minimo
# .values() para obtener los valores de las claves
edad_mas_joven = min(dic_personas.values())
        
print(edad_mas_joven)

# Ejercicio 9
# Crea un diccionario que contenga las capitales de los países de América del
# Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su
# capital correspondiente
dic_capitales = {"pais1": "capital1", "pais2": "capital2", "pais3": "capital3",
                 "pais4": "capital4", "pais6": "capital6"}
pais_ingresado = input("Ingrese un pais: ")

if pais_ingresado in dic_capitales:
    print(dic_capitales[pais_ingresado])
    
# Ejercicio 10
# Crea un diccionario que represente las notas de un examen de varios
# estudiantes, donde las claves son los nombres de los estudiantes y los
# valores son sus notas. Imprime el promedio de las notas
dic_notas = {"estudiante1": 3, "estudiante2": 9, "estudiante3": 6}
acumulador_notas = 0

for i in dic_notas.values():
    acumulador_notas += i

promedio = acumulador_notas / len(dic_notas)
print("El promedio de notas es de: {0}".format(promedio))

# Ejercicio 11
# Crea un diccionario que represente una lista de tareas por hacer. Cada clave
# del diccionario debe ser el nombre de una tarea y cada valor debe ser su
# estado (los estados son: pendiente, en proceso, completada). Imprimir todas
# las tareas seguido de su estado   
lista_tareas = {"tarea1": "pendiente", "tarea2": "en proceso", "tarea3": "completada"}

for tarea, estado in lista_tareas.items():
    print("{0}: {1}".format(tarea, estado))
    
# Ejercicio 12
# Crea un diccionario que represente una lista de las compras. Cada clave del
# diccionario debe ser el nombre de un producto y cada valor debe ser su
# cant. Pedir al usuario que ingrese el nombre del producto e imprimir la cant.
lista_compras = {"producto1": 3, "producto2": 15, "producto3": 1, "producto4": 7}
producto_ingresado = input("Ingrese el nombre del producto: ")

for nombre, cantidad in lista_compras.items():
    
    if nombre == producto_ingresado:
        print(cantidad)

# Ejercicio 13
# Crea un diccionario que contenga el nombre y el nivel de dificultad de varios
# juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que
# coinciden e imprimir sus nombres
dic_juegos_de_mesa = {"juego1": "facil", "juego2": "intermedio", "juego3": "dificil",
                      "juego4": "facil"}
dificultad_ingresada = input("Ingrese el nivel de dificultad: ")

for nombre, dificultad in dic_juegos_de_mesa.items():
    
    if dificultad == dificultad_ingresada:
        print("Nombre del juego: {0}".format(nombre))

# Ejercicio 14
# Crea un diccionario que contenga el nombre como clave y el puntaje como
# valor de varios jugadores en un juego. Luego, pedirle al usuario el nombre del
# jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
dic_jugadores = {"jugador1": 100, "jugador2": 200, "jugador3": 300}
nombre_ingresado = input("Ingrese el nombre del jugador: ")
puntaje_ingresado = int(input("Ingrese el nuevo puntaje: "))

for nombre, puntaje in dic_jugadores.items():
    
    if nombre == nombre_ingresado:
        dic_jugadores[nombre_ingresado] = puntaje_ingresado
        print(dic_jugadores)

# Ejercicio 15
# Crea un diccionario que contenga el nombre y el sueldo de varios empleados.
# Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el
# valor correspondiente en el diccionario.
dic_empleados = {"nombre1": 100, "nombre2": 200, "nombre3": 300}
nombre_ingresado = input("Ingrese el nombre del empleado: ")
sueldo_actualizado = int(input("Ingrese el sueldo aumentado: "))

for nombre, sueldo in dic_empleados.items():
    sueldo = sueldo_actualizado
    
    if nombre == nombre_ingresado:
        dic_empleados[nombre] = sueldo
        print(nombre, sueldo)

# Ejercicio 16
# Crea un diccionario que represente una lista de tareas pendientes, donde las
# claves son las tareas y los valores son "True" si están completadas y "False" si
# no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para
# marcarla como completada. Imprimir el listado de tareas pendientes
dic_tareas_pendientes = {"tarea1": True, "tarea2": False, "tarea3": True,
                        "tarea4": False}
     
tarea_completada = input("Ingrese la tarea completada: ")

for tarea, estado in dic_tareas_pendientes.items():
    
    if tarea == tarea_completada:
        dic_tareas_pendientes[tarea] = True

print(dic_tareas_pendientes)

# Ejercicio 17
# Crea un diccionario que represente las películas de un cine, donde las claves
# son los nombres de las películas y los valores son los horarios
# correspondientes. Modifica el horario de la película "Avengers: Endgame" a las
# 19:30.
dic_peliculas = {"Avengers: Endgame": "15:00", "Jurassic Park": "18:00",
                "The Dark Knight": "21:00", "Titanic": "12:30",
                "Star Wars: A New Hope": "16:30"}

dic_peliculas["Avengers: Endgame"] = "19:30"
print(dic_peliculas)

# Ejercicio 18
# Crea un diccionario que represente los juegos de una consola, donde las
# claves son los nombres de los juegos y los valores son las puntuaciones
# correspondientes. Solicita al usuario el nombre de un juego y luego su
# puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación
dic_juegos_consola = {"juego1": 100, "juego2": 200, "juego3": 300}

nombre_ingresado = input("Ingrese el nombre del juego: ")
puntuacion_ingresada = int(input("Ingrese la puntuacion: "))

if nombre_ingresado in dic_juegos_consola:
    dic_juegos_consola[nombre_ingresado] = puntuacion_ingresada
else:
    dic_juegos_consola[nombre_ingresado] = puntuacion_ingresada
    
print(dic_juegos_consola)

# Ejercicio 19
# Crea un diccionario que represente las temperaturas de una ciudad durante
# una semana, donde las claves son los días de la semana y los valores son las
# temperaturas correspondientes. Calcula la temperatura promedio de la
# semana.
temperaturas_semanales = {"ciudad1": 30, "ciudad2": 5, "ciudad3": 25}
acumulador_temperaturas = 0

for i in temperaturas_semanales.values():
    acumulador_temperaturas += i

promedio_temperaturas = acumulador_temperaturas / len(temperaturas_semanales)

print("El promedio de temperaturas es: {0}".format(promedio_temperaturas))

# Ejercicio 20
# Crea un diccionario que represente los asientos de un avión, donde las claves
# son los números de asientos y los valores son "True" si están ocupados y
# "False" si no lo están. Solicita al usuario un número de asiento y modifica su
# valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres
dic_asientos_avion = {123: True, 456: False, 789: False, 321: True}

asiento_ingresado = int(input("Ingrese el numero de asiento: "))

if asiento_ingresado in dic_asientos_avion:
    dic_asientos_avion[asiento_ingresado] = False

for numero_asiento, estado in dic_asientos_avion.items():
    
    if estado == True:
        print(numero_asiento)

# Ejercicio 21
# Crea un diccionario que represente los gastos de una persona en diferentes
# categorías, donde las claves son los nombres de las categorías y los valores
# son los gastos correspondientes. Calcula el total de gastos de la persona
dic_gastos = {"categoria1": 300, "categoria2": 500, "categoria3": 700}
acumulador_gastos = 0

for i in dic_gastos.values():
    acumulador_gastos += i

print("El total de gastos es: ${0}".format(acumulador_gastos))

# Ejercicio 22 (Es igual al ejercicio 21)
# Crea un diccionario que represente los gastos de una persona en diferentes
# categorías, donde las claves son los nombres de las categorías y los valores
# son los gastos correspondientes. Calcula el total de gastos de la persona en el mes.
dic_gastos = {"categoria1": 300, "categoria2": 500, "categoria3": 700}
acumulador_gastos = 0

for i in dic_gastos.values():
    acumulador_gastos += i

print("El total de gastos es: ${0}".format(acumulador_gastos))

# Ejercicio 23
# Crea un diccionario que represente los contactos de un teléfono, donde las
# claves son los nombres de las personas y los valores son los números de
# teléfono correspondientes. Solicitar al usuario el nombre de un contacto:
# agregarlo al diccionario en caso de que no exista. En caso de que exista
# modificar el número de teléfono del contacto
dic_contactos = {"nombre1": "11 22334455", "nombre2": "11 22334456", "nombre3": "11 22334457"}

nombre_ingresado = input("Ingrese un nombre: ")
telefono_ingresado = input("Ingrese el numero de telefono: ")

if nombre_ingresado in dic_contactos:
    dic_contactos[nombre_ingresado] = telefono_ingresado
else:
    dic_contactos[nombre_ingresado] = telefono_ingresado

print(dic_contactos)

