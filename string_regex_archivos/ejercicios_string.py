# Ejercicio 1
def convertir_string_mayusculas(cadena_de_texto):
    '''
    Escribir una funcion que reciba un string y devuelva el mismo string todo en mayusculas.
    '''
    return cadena_de_texto.upper()

cadena_ingresada = "Tengo hambre"
print(convertir_string_mayusculas(cadena_ingresada))

# Ejercicio 2
def convertir_string_minuscula(cadena_de_texto):
    '''
    Escribir una funcion que reciba un string y devuelva el mismo string todo en minusculas
    '''
    return cadena_de_texto.lower()

cadena_ingresada = "TENGO HAMBRE"
print(convertir_string_minuscula(cadena_ingresada))

# Ejercicio 3
def concatenar_strings(primera_cadena_de_texto, segunda_cadena_de_texto):
    '''
    Escribir una funcion que tome dos strings y devuelva un nuevo string 
    que contenga a ambos string concatenados, separado por un espacio.
    '''
    lista_strings_ingresados = [primera_cadena_de_texto, segunda_cadena_de_texto]
    return " ".join(lista_strings_ingresados)

primera_cadena_ingresada = "Tengo"
segunda_cadena_ingresada = "Hambre"
print(concatenar_strings(primera_cadena_ingresada, segunda_cadena_ingresada))

# Ejercicio 4
def calcular_cantidad_caracteres(cadena_de_texto):
    '''
    Funcion que tome un string y devuelva el numero de caracteres
    que tiene el string 
    '''
    return len(cadena_de_texto)

cadena_de_texto_ingresada = "Tengo hambre"
print(calcular_cantidad_caracteres(cadena_de_texto_ingresada))

# Ejercicio 5
def contador_coincidencias(cadena_de_texto, caracter_buscado):
    '''
    Funcion que toma un string y un caracter, y devuelve el numero de
    veces que aparece ese caracter en el string
    '''
    contador_caracteres = 0
    for palabra in cadena_de_texto:
        if palabra.find(caracter_buscado) >= 0:
            contador_caracteres +=1

    return contador_caracteres

cadena_ingresada = "Hola tengo hambre"
caracter_ingresado = "o"
print(contador_coincidencias(cadena_ingresada, caracter_ingresado))

# Ejercicio 6
def buscador_de_caracteres(cadena_de_texto, caracter_buscado):
    '''
    Funcion que tome un string y un caracter, y devuelva una lista
    con todas las palabras en el string que contienen ese caracter
    '''
    lista_coincidencias = []
    palabras = cadena_de_texto.lower().split()
    for palabra in palabras:
        if caracter_buscado in palabra:
            lista_coincidencias.append(palabra)

    return lista_coincidencias

cadena_ingresada = "Hola tengo hambre"
caracter_ingresado = "o"
print(buscador_de_caracteres(cadena_ingresada, caracter_ingresado))

