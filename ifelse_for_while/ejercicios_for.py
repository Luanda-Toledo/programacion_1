# Ejercicio 1
# Dada una lista de números, imprimir el número más grande de la lista.
lista_de_numeros = [1, 6, 5, 6, 9]
flag_primera_vez = True

for i in lista_de_numeros:
    
    if flag_primera_vez == True:
        numero_mayor = i
        flag_primera_vez = False
    else:
        if numero_mayor < i:
            numero_mayor = i

print(numero_mayor)

# Ejercicio 2
# Dada una lista de palabras, imprimir la palabra más larga de la lista.
lista_de_palabras = ["hola", "no", "dormir", "comer"]
flag_primera_vez = True

for i in range(len(lista_de_palabras)):
    
    if flag_primera_vez == True:
        palabra_mas_larga = len(lista_de_palabras[i])
        indice_palabra_mas_larga = i
        flag_primera_vez = False
    else:
        if len(lista_de_palabras[i]) > palabra_mas_larga:
            palabra_mas_larga = len(lista_de_palabras[i])
            indice_palabra_mas_larga = i

print("La palabra mas larga es: ")
print(lista_de_palabras[indice_palabra_mas_larga])

# Ejercicio 3
# Dado un núm entero n, imprimir la secuencia de núm pares menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
lista_numeros_pares = []

for i in range(numero_ingresado):
    if i % 2 == 0 and i > 0:
        lista_numeros_pares.append(i)

print(lista_numeros_pares)

# Ejercicio 4
# Dado un núm entero n, imprimir la suma de los núm impares menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
acumulador_impares = 0

for i in range(numero_ingresado + 1):
    if not(i % 2 == 0):
        acumulador_impares += i

print("La suma de numeros impares es: {0}".format(acumulador_impares))

# Ejercicio 5
# Dada una lista de números, imprimir el número más pequeño de la lista.
lista_de_numeros = [3, 5, 6, 2, 8, 9]
flag_primera_vez = True

for i in range(len(lista_de_numeros)):
    
    if flag_primera_vez == True:
        numero_menor = lista_de_numeros[i]
        flag_primera_vez = False
    else:
        if lista_de_numeros[i] < numero_menor:
            numero_menor = lista_de_numeros[i]
            
print("El numero menor de la lista es: {0}".format(numero_menor))

# Ejercicio 6
# Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.
lista_de_palabras = ["Hola", "No", "Dormir", "Comer"]
lista_de_vocales = ["a", "e", "i", "o", "u"]
contador_vocales = 0

for palabra in lista_de_palabras:
    
    for letra in palabra:
        
        if letra in lista_de_vocales:
            contador_vocales += 1

print("La cantidad de vocales de la lista es: {0}".format(contador_vocales))

# Ejercicio 7
# Dado un núm entero n, imprimir la secuencia de núm impares menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))

for i in range(numero_ingresado):
    
    if not(i % 2 == 0):
        if i <= numero_ingresado:
            print(i)
            
# Ejercicio 8
# Dado un núm entero n, imprimir la suma de los núm pares menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
acumulador_pares = 0

for i in range(numero_ingresado + 1):
    
    if i % 2 == 0:
        acumulador_pares += i

print("La suma de numeros pares hasta '{0}' es: {1}".format(
    numero_ingresado, acumulador_pares))

# Ejercicio 9
# Dada una lista de núm, imprimir la cant de núm negativos en la lista.
lista_de_numeros = [1, 3, -5, -6, 4]
contador_negativos = 0

for i in range(len(lista_de_numeros)):
    
    if lista_de_numeros[i] < 0:
        contador_negativos += 1

print("La cantidad de numeros negativos de la lista es: {0}".format(contador_negativos))

# Ejercicio 10
# Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.
lista_de_palabras = ["hola", "anana", "comer", "ahora"]

for palabra in lista_de_palabras:
    
    primera_letra = palabra[0]
    ultima_letra = palabra[len(palabra) - 1]
    if primera_letra == ultima_letra:
        print(palabra)
        
# Ejercicio 11
# Dado un núm entero n, imprimir la secuencia de núm primos menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
lista_numeros_primos = []

if numero_ingresado < 2: # n mayor que 2, pq 0 y 1 no son primos
    print("Ingrese numeros mayores a 2.")

else:    
    #Verificamos si es divisible por algun numer entre 2 y n-1
    for i in range(2, numero_ingresado + 1):
        flag_es_primo = True
    
        for j in range(2, i):
        
            if i % j == 0:
                flag_es_primo = False
                break
            
            j += 1 
            
        if flag_es_primo == True:
            lista_numeros_primos.append(i)
        
        i += 1
        
print("Los numeros primos hasta {0} son: {1}".format(numero_ingresado, lista_numeros_primos))

# Ejercicio 12
# Dada una lista de núm, imprimir la cantidad de núm pares en la lista.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador_pares = 0

for i in range(len(lista_de_numeros)):
    numero_lista = lista_de_numeros[i]
    if numero_lista % 2 == 0:
        contador_pares += 1
        
print("La cantidad de numeros pares de la lista es: {0}".format(contador_pares))

# Ejercicio 13
# Dada una lista de palabras, imprimir las palabras que tienen una longitud impar
lista_de_palabras = ["hola", "comer", "dormir", "lapiz"]

for i in range(len(lista_de_palabras)):
    palabra = lista_de_palabras[i]
    
    if not(len(palabra) % 2 == 0):
        print(palabra)
        
# Ejercicio 14
# Dado un núm entero n, imprimir la secuencia de núm perfectos menores o iguales a n.

numero_ingresado = int(input("Ingrese un numero: "))

for i in range(1, numero_ingresado):
    acumulador_divisores = 0
    
    for j in range(1, i):
        
        if i % j == 0:
            acumulador_divisores += j
        
    if acumulador_divisores == i:
        print(i)
        
# Ejercicio 15
# Dada una lista de núm, imprimir la cant. de núm impares en la lista.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador_impares = 0

for i in range(len(lista_de_numeros)):
    numero_lista = lista_de_numeros[i]
    
    if not( numero_lista % 2 == 0 ):
        contador_impares += 1
        
print("La cantidad de numeros impares es: {0}".format(contador_impares))

# Ejercicio 16
# Dada una lista de palabras, imprimir las palabras que tienen una letra específica.
lista_de_palabras = ["hola", "no", "comer", "dormir"]
letra_ingresada = input("Ingrese una letra: ")

for i in range(len(lista_de_palabras)):
    palabra = lista_de_palabras[i]
    
    for j in range(len(palabra)):
        letra = palabra[j]
        
        if letra_ingresada == letra:
            print(palabra)
            
# Ejercicio 17
# Dado un núm entero n, imprimir la secuencia de núm de Harshad menores o iguales a n.
# Harshad = entero divisible entre la suma de sus dígitos en una base dada
numero_ingresado = int(input("Ingrese un numero: "))

for i in range(1, numero_ingresado + 1):
    suma_digitos = 0
    numero = i
    
    while numero > 0:
        suma_digitos += numero % 10
        numero //= 10
        
    if i % suma_digitos == 0:
        print(i)

# Ej: 10 - 12 - 18 - 20


# Ejercicio 18
# Dada una lista de núm, imprimir la suma de los núm en la lista que
# son mayores que el promedio de la lista
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
acumulador_numeros = 0

for i in range(len(lista_de_numeros)):
    acumulador_numeros += lista_de_numeros[i]

promedio_numeros = acumulador_numeros / len(lista_de_numeros)
print(promedio_numeros)

for i in range(len(lista_de_numeros)):
    if lista_de_numeros[i] > promedio_numeros:
        print(lista_de_numeros[i])
        
# Ejercicio 19
# Dada una lista de palab, imprimir las palab que tienen una letra mayuscula.
lista_de_palabras = [ "Hola", "Nombre", "No", "comer", "dormir"]

for i in range(len(lista_de_palabras)):
    palabra = lista_de_palabras[i]
    
    for j in range(len(palabra)):
        letra = palabra[j]
        
        if letra.isupper():
            print(palabra)
            
# Ejercicio 20
# Dado un núm ent. n, imprimir la secuencia de núm triangulares men o iguales a n
# Un núm triangular es un núm que se obtiene al sumar n núm naturales consecutivos.
numero_ingresado = int(input("Ingrese un numero entero: "))
acumulador_numeros = 0

for i in range(numero_ingresado):
    acumulador_numeros += i
    numero_triangular = 0
    numero_triangular += acumulador_numeros
    
    if numero_triangular <= numero_ingresado and numero_triangular > 0:
        print(acumulador_numeros)




