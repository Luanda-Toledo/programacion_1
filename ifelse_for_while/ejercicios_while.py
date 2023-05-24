# Ejercicio 1 - Imprimir n numeros de manera descendente hasta 1
numero_n = input("Ingrese un numero: ")
numero_n = int(numero_n)

while numero_n > 0 :
    print(numero_n, end = " ")
    numero_n -= 1

# Ejercicio 2 - Imprimir numeros hasta n de manera ascendente
numero_n = input("Ingrese un numero: ")
numero_n = int(numero_n)
contador = 1

while contador < numero_n + 1 :
    print(contador, end = " ")
    contador += 1
    
# Ejercicio 3 - Dada una cadena de texto imprimir cada uno de los caracteres de la cadena
cadena_de_texto = input("Ingrese una cadena de texto: ")
indice = 0

while indice < len(cadena_de_texto) :
    print(cadena_de_texto[indice])
    indice += 1
    
# Ejercicio 4 - Dada una lista de num imprimir la suma de todos los elem de la lista
lista_de_numeros = []
respuesta = "si"
indice = 0
total = 0

while respuesta == "si":
    elemento = int(input("Ingrese un numero: "))
    lista_de_numeros.append(elemento)
    respuesta = input("Desea agregar otro numero a la lista? ( si / no ) ")
    
while indice < len(lista_de_numeros):
    total += lista_de_numeros[indice]
    indice += 1
    
print("Lista: {0} \n La suma de los elementos de la lista es: {1} ".format(lista_de_numeros, total))

# Ejercicio 5 (numeros primos)
# Dado un número entero n, imprimir si el número es primo o no.
numero_ingresado = int(input("Ingrese un numero: "))

if numero_ingresado < 2: # n mayor que 2, pq 0 y 1 no son primos
    
    print("El numero {0} no es primo".format(numero_ingresado))

else: 
    
    flag_numero_primo = True
    
    #Verificamos si es divisible por algun numer entre 2 y n-1
    i = 2
    while i < numero_ingresado:
        
        if numero_ingresado % i == 0:
            flag_numero_primo = False
            break
        
        i += 1
        
    if flag_numero_primo == True:
        print("Es numero primo")
    
    else:
        print("No es un numero primo")

# Ejercicio 6 - Dado un núm entero n, imprimir la suma de todos los núm pares menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
i = 0
acumulador_pares = 0

while i <= numero_ingresado:
    
    if i % 2 == 0:
        acumulador_pares += i
    i += 1

print("La suma de los numeros pares hasta el num ingresado es: {0}".format(acumulador_pares))

# Ejercicio 7 - Dada una lista de núm, imprimir todos los núm que son mayores que el promedio de la lista.
lista_numeros_ingresados = []
respuesta = "si"
acumulador_elementos = 0

while respuesta == "si":
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_numeros_ingresados.append(numero_ingresado)

    acumulador_elementos += numero_ingresado

    respuesta= input("Desea ingresar otro numero: (si/no) \n")
    
promedio_elementos = acumulador_elementos / len(lista_numeros_ingresados)

for i in lista_numeros_ingresados:
    
    if i > promedio_elementos:
        print(i)
        
# Ejercicio 8 - Dada una cadena de texto, imprimir la cantidad de vocales en la cadena
lista_vocales = ["a", "e", "i", "o", "u"]
texto_ingresado = input("Ingrese una cadena de texto: ")
i = 0

while i < len(texto_ingresado):
    letra_de_la_cadena = texto_ingresado[i]
        
    if letra_de_la_cadena in lista_vocales:
        print(letra_de_la_cadena)

    i += 1

# Ejercicio 9 - Dado un número entero n, imprimir todos los números impares menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
i = 0

while i <= numero_ingresado:

    if not(i % 2 == 0):
        print(i)

    i += 1 

# Ejercicio 10 - Dada una lista de números, imprimir la cantidad de números pares en la lista.
lista_de_numeros = []
contador_pares = 0
respuesta = "si"
i = 0

while respuesta == "si":
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_de_numeros.append(numero_ingresado)

    respuesta = input("Desea ingresar otro numero: (si/no) \n")

while i <= len(lista_de_numeros) - 1:
    elemento_de_la_lista = lista_de_numeros[i]
    
    if elemento_de_la_lista % 2 == 0:
        print(elemento_de_la_lista)
    
    i += 1
    
# Ejercicio 11 - Dada una lista de palabras, imprimir palabras que tengan una longitud mayor a 5 caracteres.
lista_de_palabras = []
respuesta = "si"
i = 0

while respuesta == "si":
    palabra_ingresada = input("Ingrese una palabra: ")
    lista_de_palabras.append(palabra_ingresada)
    
    respuesta = input("Desea ingresar otra palabra: (si/no) \n")

while i < len(lista_de_palabras):
    elemento_de_la_lista = lista_de_palabras[i]
    
    if len(elemento_de_la_lista) > 5:
        print("\n {0}".format(elemento_de_la_lista))   

    i += 1

print("\nLa lista de palabras ingresadas es: {0}".format(lista_de_palabras))

# Ejercicio 12 - Dado un núm entero n, imprimir la suma de todos los núm impares menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
acumulador_impares = 0
i = 0

while i < numero_ingresado:
    
    if not(i % 2 == 0):
        acumulador_impares += i
        
    i += 1 

print("La suma de los impares hasta el numero {0} es: {1}".format(numero_ingresado, acumulador_impares))

# Ejercicio 13 - Dada una lista de números, imprimir la cantidad de números negativos en la lista.
lista_de_numeros = []
respuesta = "si"
i = 0
acumulador_numeros_negativos = 0

while respuesta == "si":
    
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_de_numeros.append(numero_ingresado)
    
    respuesta = input("Desea seguir ingresando numeros: (si/no) \n")

while i < len(lista_de_numeros):
    numero_de_la_lista = lista_de_numeros[i]
    
    if numero_de_la_lista < 0:
        acumulador_numeros_negativos += 1

    i += 1

print("La cantidad de numeros negativos ingresados en la lista es: {0}".format(acumulador_numeros_negativos))

# Ejercicio 14 - Dada una cadena de texto, imprimir la cant. de veces que aparece una letra específica en la cadena
texto_ingresado = input("Ingrese una cadena de texto: ")
letra_especifica = input("ingrese una letra: ")
i = 0
contador_coincidencias = 0

while i < len(texto_ingresado):
    
    letra_en_el_texto = texto_ingresado[i]
    
    if letra_en_el_texto == letra_especifica:
        contador_coincidencias += 1 
    
    i += 1

print("La cantidad de veces que se repite la letra '{0}', en el texto: '{1}', es de: {2}".format(
    letra_especifica, texto_ingresado, contador_coincidencias))

# Ejercicio 15 - Dado un núm entero n, imprimir todos los núm primos menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
lista_numeros_primos = []

if numero_ingresado < 2: # n mayor que 2, pq 0 y 1 no son primos
    print("Ingrese numeros mayores a 2.")

else: 
    
    #Verificamos si es divisible por algun numer entre 2 y n-1
    i = 2
    while i <= numero_ingresado:
        flag_es_primo = True
        j = 2
    
        while j < i:
        
            if i % j == 0:
                flag_es_primo = False
                break
            
            j += 1 
            
        if flag_es_primo == True:
            lista_numeros_primos.append(i)
        
        i += 1
        
print("Los numeros primos hasta {0} son: {1}".format(numero_ingresado, lista_numeros_primos))

# Ejercicio 16 - Dada una lista de núm, imprimir todos los núm que son múltiplos de 3.
lista_de_numeros = []
respuesta = "si"
while respuesta == "si":
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_de_numeros.append(numero_ingresado)
    
    respuesta = input("Desea ingresar otro numero: (si/no) \n")

i = 0
while i < len(lista_de_numeros):
    multiplo = lista_de_numeros[i]
    
    if multiplo % 3 == 0:
        print(multiplo)
        
    i += 1
    
# Ejercicio 17 - Dada una cadena de texto, imprimir la cadena al revés
texto_ingresado = input("Ingrese una cadena de texto: ")
i = len(texto_ingresado) - 1
lista_texto_al_reves = []

while i >= 0:
    caracter_del_texto = texto_ingresado[i]
    lista_texto_al_reves.append(caracter_del_texto)
    i -= 1
    
print(lista_texto_al_reves)

# Ejercicio 18 - Dado un núm entero n, imprimir la suma de todos los múltiplos de 5 menores o iguales a n.
numero_ingresado = int(input("Ingrese un numero: "))
acumulador_multiplos = 0
i = 0

while i <= numero_ingresado:
    if i % 5 == 0:
        acumulador_multiplos += i
    i += 1
    
print("La suma de los numeros multiplos de 5 hasta '{0}', es de: {1}".format(
    numero_ingresado, acumulador_multiplos))

# Ejercicio 19 - Dada una lista de núm, imprimir todos los mayores que el núm anterior en la lista.
lista_numeros = []
respuesta = "si"

while respuesta == "si":
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_numeros.append(numero_ingresado)
    
    respuesta = input("Desea ingresar otro numero? (si/no) \n")
   
i = 0
while i < len(lista_numeros):
    
    if lista_numeros[i] > len(lista_numeros) - 1:
        print(lista_numeros[i])
    i += 1

# Ejercicio 20
# Dado un núm entero n, imprimir todos los núm perfectos menores o iguales a n.
# Los números perfectos son aquellos números enteros positivos
# que son iguales a la suma de sus divisores propios (excluyendo al propio
# número). En otras palabras, si sumamos todos los divisores propios de un
# número (excluyendo el número en sí mismo) y el resultado es igual al número,
# entonces ese número se considera un número perfecto.
# Por ejemplo, el primer número perfecto es 6, ya que sus divisores propios son
# 1, 2 y 3, y 1 + 2 + 3 = 6.

numero_ingresado = int(input("Ingrese un numero: "))
acumulador_divisores = 0
i = 1
while i <= numero_ingresado:
    j = 1
    acumulador_divisores = 0
    
    while j < i:
        if i % j == 0:
            acumulador_divisores += j
        j += 1
            
    if acumulador_divisores == i:
        print(i)
        
    i += 1


