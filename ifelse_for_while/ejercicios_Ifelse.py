# Ejercicio 1
numero_ingresado = int(input("Ingrese un numero:"))

if numero_ingresado > 0:
    print("El numero ingresado es positio")
else:
    print("El numero ingresado es cero o negarivo")
    
# Ejercicio 2
edad = int(input("Ingrese su edad:"))

if edad > 17:
    print("Eres mayor de edad")
else: 
    print("Eres menor de edad")

# Ejercicio 3
numero_entero_ingresado = int(input("Ingrese un numero entero:"))

if (numero_entero_ingresado % 2) == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar") 
    
    
# Ejercicio 4
primer_numero_ingresado = int(input("Ingrese el primer numero:"))
segundo_numero_ingresado = int(input("Ingrese el segundo numero:"))

if primer_numero_ingresado > segundo_numero_ingresado:
    print("El primer numero ingresado es mayor")
elif primer_numero_ingresado < segundo_numero_ingresado: 
    print("El segundo numero ingresado es mayor")
else: 
    print("Los dos numeros son iguales")

# Ejercicio 5
nombre_ingresado = input("Ingrese su nombre: ")

if (nombre_ingresado == "Juan") or (nombre_ingresado == "Maria") or (nombre_ingresado == "Pedro"):
    print("Hola {0}".format(nombre_ingresado))
else: 
    print("Hola desconocido")

# Ejercicio 6
nombre_ingresado = input("Ingrese su nombre: ")
edad_ingresada = int(input("Ingrese su edad: "))

if (edad_ingresada > 17):
    
    if edad_ingresada < 65:
        print("Puedes votar {0}".format(nombre_ingresado))
    else:
        print("No puedes votar {0}".format(nombre_ingresado))
    
else:
    print("No puedes votar {0}".format(nombre_ingresado))
    
# Ejercicio 7 ******************************* CHEQUEAR ***********************************************
numero_entero_positivo = int(input("Ingrese un numero entero positivo: "))

if ((numero_entero_positivo % 2 ) == 0 ) or ((numero_entero_positivo % 3 ) == 0 ):
    print("El numero no es primo")
else: 
    print("El numero es primo")

# Ejercicio 8
numero_entero_positivo = int(input("Ingrese un numero entero positivo: "))

if numero_entero_positivo > 0 and int(numero_entero_positivo ** 0.5)**2 == numero_entero_positivo:
    print("El numero {0} es un cuadrado perfecto".format(numero_entero_positivo))
else:
    print("El numero {0} NO es un cuadrado perfecto".format(numero_entero_positivo))
    
# Ejercicio 9
letra_ingresada = input("Ingrese una letra: ")

if letra_ingresada in ["a", "e", "i", "o", "u"]:
    print("Es una vocal")
else:
    print("Es una consonante")

# Ejercicio 10
numero_entero_y_par = int(input("Ingrese un numero entero positivo: "))

if (numero_entero_y_par % 2) == 0 and (numero_entero_y_par > 0):
    print("El numero es positivo y par")
else:
    print("El numero no cumple ninguna condicion")
    
# Ejercicio 11
edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada < 12:
    print("Eres un niño")
elif edad_ingresada < 18:
    print("Eres un adolescente")
else:
    print("Eres un adulto")
    
# Ejercicio 12
primer_numero_ingresado = int(input("Ingrese el primer numero: "))
segundo_numero_ingresado = int(input("Ingrese el segundo numero: "))

if primer_numero_ingresado > 0:
    print("El primer numero es positivo")
elif segundo_numero_ingresado > 0:
    print("El segundo numero es positivo")
else:
    print("Ambos numeros son negativos")
    
# Ejercicio 13
numero_entero_ingresado = int(input("Ingrese un numero entero: "))

if (numero_entero_ingresado % 3) == 0 and (numero_entero_ingresado % 5) == 0:
    print("El numero es divisible por 3 y por 5")
else:
    print("El numero NO es divisible por 3 y por 5") 

# Ejercicio 14
numero_entero_ingresado = int(input("Ingrese un numero entero: "))

if (numero_entero_ingresado % 4) == 0 and (numero_entero_ingresado % 6) == 0:
    print("El numero es multiplo por 4 y por 6")
else:
    print("El numero NO es multiplo por 4 y por 6")

# Ejercicio 15 (ES EL MISMO QUE EL 7) *********************************************************
numero_entero_positivo = int(input("Ingrese un numero entero positivo: "))

if ((numero_entero_positivo % 2 ) == 0 ) or ((numero_entero_positivo % 3 ) == 0 ):
    print("El numero no es primo")
else: 
    print("El numero es primo")

# Ejercicio 16
nombre_ingresado = input("Ingrese su nombre: ")
edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada > 12 and edad_ingresada < 18:
    
    print("{0}. Eres adolescente".format(nombre_ingresado))
    
elif edad_ingresada > 17 and edad_ingresada < 65:
    
    print("{0}. Eres adulto".format(nombre_ingresado))
    
elif edad_ingresada > 64:
    print("{0}. Eres adulto mayor".format(nombre_ingresado))

# Ejercicio 17
numero_entero_ingresado = int(input("Ingrese un numero entero: "))

if numero_entero_ingresado < 0:
    print("El número es negativo")
    
elif numero_entero_ingresado == 0:
    print("El número es cero")
    
else:
    print("El número es positivo") 

# Ejercicio 18
numero_entero_ingresado = int(input("Ingrese un numero entero: "))

if numero_entero_ingresado % 2 == 0 and numero_entero_ingresado % 3 == 0:
   print("El numero {0} es par y es multiplo de 3".format(numero_entero_ingresado))
else:
    print("El numero no cumple ninguna de las dos condiciones")
    
# Ejercicio 19
edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada > 17:
    print("Eres mayor de edad")
    
elif edad_ingresada > 12:
    print("Eres adolescente")
    
else: 
    print("Eres menor de edad")
    
# Ejercicio 20
primer_numero_ingresado = int(input("Ingrese el primer numero: "))
segundo_numero_ingresado = int(input("Ingrese el segundo numero: "))

if primer_numero_ingresado == segundo_numero_ingresado:
    print("Los dos numeros son iguales")
    
elif primer_numero_ingresado > segundo_numero_ingresado:
    print("El primer numero es mayor")
    
else: 
    print("El segundo numero es mayor")
























# https://onlinegdb.com/6fBWD9X31 -> spd 1ra clase



