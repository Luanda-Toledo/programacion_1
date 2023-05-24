# Ejercicio 1
def pasaje_temperatura_fahrenheit(grados_celcius=int):
    '''
    Crear una función que convierta grados Celsius a grados Fahrenheit.
    Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
    Formula de C a F = (0 °C * 9 / 5) + 32 = 32 °F
    '''
    return (grados_celcius * 9/5) + 32

print(pasaje_temperatura_fahrenheit(0)) #32

# Ejercicio 2
def calcular_area_circulo(radio=int):
    '''
    Crear una función que calcule el área de un círculo.
    Recibe un parámetro (radio) y devuelve el área del círculo.
     Formula => A = π r²
    ''' 
    return 3.1416 * radio**2

print(calcular_area_circulo(2)) #12.5664

# Ejercicio 3
def calcular_descuento_producto(precio_original=int, precio_con_descuento=int):
    '''
    Crear una función que calcule el descuento aplicado a un producto.
    Recibe dos parámetros (precio original y precio con descuento) y 
    devuelve el porcentaje de descuento aplicado.
    ''' 
    return (precio_original - precio_con_descuento) * 100 / precio_original

print(calcular_descuento_producto(100, 75)) # 25% de descuento

# Ejercicio 4
def calcular_promedio_personas(lista_edades):
    '''
    Crear una función que calcule el promedio de edad de un grupo de personas. 
    Recibe una lista de edades y devuelve el promedio.
    ''' 
    acumulador_edades = 0
    for i in lista_edades:
        acumulador_edades += i

    return acumulador_edades / len(lista_edades)

print(calcular_promedio_personas([15, 25, 50, 10])) # 25

# Ejercicio 5
def verificar_numero_primo(numero_ingresado):
    '''
    Crear una función que determine si un número es primo o no. 
    Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
    '''
    if numero_ingresado < 2:
        return False
    
    for i in range(2, numero_ingresado):
        if numero_ingresado % i == 0:
            return True

    return True

print(verificar_numero_primo(3)) # True

# Ejercicio 6
def calcular_area_triangulo(base, altura):
    '''
    Crear una función que calcule el área de un triángulo. 
    Recibe dos parámetros (base y altura) y devuelve el área.
    Formula = base * altura / 2
    '''
    return base * altura / 2

print(calcular_area_triangulo(10, 6)) # 30

# Ejercicio 7
# Si el segundo número es cero, el MCD es el primer número
# Si no, calculamos el MCD de b y el resto de a/b recursivamente
def calcular_maximo_comun_divisor(primer_numero, segundo_numero):
    '''
    Crear una función que calcule el máximo común divisor de dos números. 
    Recibe dos parámetros (números) y devuelve el máximo común divisor.
    '''
    if segundo_numero == 0:
        return primer_numero
    else: 
        return calcular_maximo_comun_divisor(segundo_numero, primer_numero % segundo_numero)

print(calcular_maximo_comun_divisor(10, 6)) # 2

# Ejercicio 8
def verificar_paridad(numero_ingresado):
    '''
    Crear una función que verifique si un número es par o impar. 
    Recibe un número como parámetro y devuelve True si es par o False si es impar.
    '''
    if numero_ingresado % 2 == 0:
        return True
    else: 
        return False
    
print(verificar_paridad(10)) # True
print(verificar_paridad(9)) # False

# Ejercicio 9
def contador_elementos_en_lista(lista_ingresada, elemento=int):
    '''
    Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
    Recibe una lista y un elemento como parámetros 
    y devuelve la cantidad de veces que aparece en la lista.
    '''
    contador_elementos = 0
    
    for i in lista_ingresada: 
        if i == elemento:
            contador_elementos += 1
            
    return contador_elementos
    
print(contador_elementos_en_lista([3, 4, 3, 5, 3, 3], 3)) # 3

# Ejercicio 10
def longitud_palabra_mas_larga(lista_de_palabras):
    '''
    Crea una función que reciba como parámetros una lista
    de palabras y devuelva la palabra más larga.
    '''
    for i in range(len(lista_de_palabras)):
        if i == 0 or palabra_mas_larga < len(lista_de_palabras[i]):
            palabra_mas_larga = len(lista_de_palabras[i])

    return palabra_mas_larga
       
print(longitud_palabra_mas_larga(["Hola", "Si", "tengo", "hambre"])) # "hambre"

# Ejercicio 11
def contador_de_vocales(cadena_de_texto):
    '''
    Crea una función que reciba como parámetro una cadena de texto
    y devuelva la cantidad de vocales que tiene.
    '''
    contador_vocales = 0
    for i in range(len(cadena_de_texto)):
        if cadena_de_texto[i] in ["a", "e", "i", "o", "u"]:
            contador_vocales += 1
                  
    return contador_vocales
       
print(contador_de_vocales("Tengo mucha hambre")) # 6

# Ejercicio 12
def crear_lista_elementos_en_comun(primera_lista, segunda_lista):
    '''
    Crea una función que reciba dos listas de nombres, 
    y devuelva una lista con los nombres que aparecen en ambas listas
    '''
    lista_elementos_en_comun = []
    for i in primera_lista:
        if i in segunda_lista:
            lista_elementos_en_comun.append(i)
    
    return lista_elementos_en_comun
       
print(crear_lista_elementos_en_comun(["Hola", "Tengo", "hambre", "Si"],
                                     ["Chau", "Tengo", "hambre", "No"])) # "Tengo" "hambre"

# Ejercicio 13
def crear_diccionario_logitud_de_palabras(lista_de_palabras):
    '''
    Crear una función que recibe una lista de palabras 
    y devuelve un diccionario con las palabras como llaves 
    y su longitud como valores.
    '''
    longitud_de_palabras = {}
    for i in lista_de_palabras:
        longitud_de_palabras[i] = len(i)

    return longitud_de_palabras
       
print(crear_diccionario_logitud_de_palabras(["Hola", "Tengo", "hambre", "Si"])) 
# En consola: {"Hola": 4, "Tengo": 5, "hambre": 6, "Si":2}

# Ejercicio 14
def crear_diccionario_minimo_maximo_promedio(lista_de_numeros):
    '''
    Crear una función que recibe una lista de números 
    y devuelve un diccionario con el valor mínimo, el valor máximo 
    y el promedio de los números en la lista.
    '''
    diccionario_valores = {}
    acumulador_numeros = 0
    numero_maximo = lista_de_numeros[0]
    numero_minimo = lista_de_numeros[0]
    
    for i in range(len(lista_de_numeros)):
        
        if i == 0 or numero_maximo < lista_de_numeros[i]:
            numero_maximo = lista_de_numeros[i]
            
            if numero_minimo > lista_de_numeros[i]:
                numero_minimo = lista_de_numeros[i]
                
        acumulador_numeros += lista_de_numeros[i]
        
    promedio = acumulador_numeros / len(lista_de_numeros)
    
    diccionario_valores["Maximo"] = numero_maximo
    diccionario_valores["Minimo"] = numero_minimo
    diccionario_valores["Promedio"] = promedio
    
    return diccionario_valores
       
print(crear_diccionario_minimo_maximo_promedio([6, 3, 4, 22, 15])) 
# Min: 3 - Max: 22 - Promedio: 10

# Ejercicio 15
def crear_diccionario_contador_generos(lista_peliculas):
    '''
    Crear una función que recibe una lista de diccionarios con información
    de películas (título, género, director) y devuelve un diccionario
    con la cantidad de películas por género.
    '''
    diccionario_generos = {}
    contador_terror = 0
    contador_comedia = 0
    contador_drama = 0
    
    for i in range(len(lista_peliculas)):
        
        if lista_peliculas[i]["Genero"] == "terror":
            contador_terror += 1
        elif lista_peliculas[i]["Genero"] == "drama":
            contador_drama += 1
        elif lista_peliculas[i]["Genero"] == "comedia":
            contador_comedia += 1
            
    diccionario_generos["terror"] = contador_terror
    diccionario_generos["drama"] = contador_drama
    diccionario_generos["comedia"] = contador_comedia
    
    return diccionario_generos
       
print(crear_diccionario_contador_generos([{"Titulo": "Titulo1", "Genero": "terror", "Director": "Directo1"},
                                          {"Titulo": "Titulo2", "Genero": "comedia", "Director": "Directo2"},
                                          {"Titulo": "Titulo3", "Genero": "drama", "Director": "Directo3"},
                                          {"Titulo": "Titulo4", "Genero": "terror", "Director": "Directo4"}]))




