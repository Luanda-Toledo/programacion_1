# LUANDA TOLEDO VIERA - DIV: H

# 1. Crea una función que ordene una lista de números enteros de menor a mayor. 
# Puedes utilizar cualquier método de ordenamiento que conozcas.
lista_numeros = [5, 6, 0, 8, 9, 15, 1, 7]

def ordenar_lista_numerica(lista) -> list:
    '''
    Recibe una lista de números enteros y los ordena de menor a mayor. 
    '''
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for i in range(len(lista) - 1):
            
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag_swap = True

    return lista_numeros
        
print(ordenar_lista_numerica(lista_numeros))


# 2. Crea una función que ordene una lista de cadenas alfabéticamente de A a Z.
lista_palabras = ["tengo", "sueño", "y", "ahora", "mucho", "hambre"]

def ordenar_lista_palabras(lista) -> list:
    '''
    Recibe una lista y ordena alfabeticamente de la A a la Z las palabras de la lista.
    '''
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for i in range(len(lista)):

            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
                    flag_swap = True
    return lista

print(ordenar_lista_palabras(lista_palabras))


# 3. Crea una función que ordene un diccionario de estudiantes por calificación de mayor a menor.
estudiantes = {
    "Juan": 80,
    "Ana": 95,
    "Carlos": 70,
    "Sofía": 85,
    "María": 90
}

def ordenar_calificaciones(diccionario:dict) -> dict:
    '''
    Recibe un diccionario, y devuelve un diccionario con sus claves ordenadas de mayor a menor.
    '''
    lista_claves = list(diccionario.keys())
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for i in range(len(lista_claves) - 1):
            if diccionario[lista_claves[i]] < diccionario[lista_claves[i + 1]]:
                lista_claves[i], lista_claves[i + 1] = lista_claves[i + 1], lista_claves[i]
                flag_swap = True

    diccionario_ordenados = {}
    for clave in lista_claves:
        diccionario_ordenados[clave] = diccionario[clave]

    return diccionario_ordenados

print(ordenar_calificaciones(estudiantes))


# 4. Crea una función que ordene una lista de diccionarios con información sobre libros 
# (título, autor, año de publicación) por año de publicación de menor a mayor.
lista_libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"titulo": "La Iliada", "autor": "Homero", "año": -750},
    {"titulo": "1984", "autor": "George Orwell", "año": 1949},
    {"titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "año": 1925},
    {"titulo": "La Odisea", "autor": "Homero", "año": -720},
    {"titulo": "El Viejo y el Mar", "autor": "Ernest Hemingway", "año": 1952}
]

def ordenar_lista_diccionarios(lista:list, clave:str) -> list:
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

print(ordenar_lista_diccionarios(lista_libros, "año"))


# 5. Crea una función que ordene un diccionario que mapee nombres de frutas a su precio por kilogramo de menor a mayor.
diccionario_frutas = {
    "manzana": 2.5,
    "banana": 3.0,
    "naranja": 2.0,
    "uva": 4.5,
    "pera": 2.0
}

def ordenar_diccionario_ascendente(diccionario:dict) -> dict:
    '''
    Recibe un diccionario, y lo devuelve ordenado segun el precio.
    '''
    lista_claves = list(diccionario.items()) #tupla (clave-valor)
    flag_swap = True

    while flag_swap:
        flag_swap = False
        
        for i in range(len(lista_claves) - 1):
            if lista_claves[i][1] > lista_claves[i +1][1]:
                lista_claves[i], lista_claves[i + 1] = lista_claves[i + 1], lista_claves[i]
                flag_swap = True
    return dict(lista_claves)

print(ordenar_diccionario_ascendente(diccionario_frutas))


# 6. Crea una función que ordene una lista de tuplas 
# (nombre, edad, altura) primero por edad de menor a mayor y
#  luego por altura de menor a mayor.
personas = [("Juan", 25, 1.8), 
            ("María", 30, 1.6), 
            ("Carlos", 20, 1.75), 
            ("Sofía", 28, 1.65)]

def ordenar_lista_tuplas_ascendente(lista:list) -> list:
    '''
    Recibe una lista de tuplas, y la devuelve ordenada segun clave de menor a mayor
    '''
    flag_swap = True

    #Ordenar por edad
    while flag_swap:
        flag_swap = False
        
        for i in range(len(lista) - 1):
            if lista[i][1] > lista[i + 1][1]:
                lista[i], lista[i + 1] = lista[i + 1],lista[i]
                flag_swap = True

        # Ordenar por altura
        for i in range(len(lista) - 1):
            if lista[i][1] == lista[i + 1][1] and lista[i][2] > lista[i + 1][2]:
                lista[i], lista[i + 1] = lista[i + 1],lista[i]
                flag_swap = True
    
    return lista

print(ordenar_lista_tuplas_ascendente(personas))



