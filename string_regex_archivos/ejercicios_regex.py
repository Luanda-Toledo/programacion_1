import re

# 1- 
def es_mayuscula(cadena_texto):
    '''
    Recibe un string, devuelve True en caso de que todas las letras sean mayusculas 
    o False en caso contrario
    '''
    # desde el principio (^) hasta el final ($) de la cadena
    # La función bool() se utiliza para convertir el objeto "Match" en True o Fals
    coincidencia_buscada =  bool(re.match("^[A-Z]*$", cadena_texto))
    print(coincidencia_buscada)

es_mayuscula("TENGOHAMBRE")
es_mayuscula("Tengohambre")
es_mayuscula("tengohambre")

# 2-
def es_minuscula(cadena_texto):
    '''
    Recibe un string, devuelve True en caso de que todas las letras sean minusculas
    o False en caso contrario
    '''
    coincidencia_buscada =  bool(re.match("^[a-z]*$", cadena_texto))
    print(coincidencia_buscada)

es_minuscula("TENGOHAMBRE")
es_minuscula("Tengohambre")
es_minuscula("tengohambre")

#3-
def es_entero(cadena_texto):
    '''
    Recibe un string y devuelve True en caso de que sea un numero entero, en caso 
    contrario devuelve false
    '''
    coincidencia_buscada = bool(re.match("^[0-9]*$", cadena_texto))
    print(coincidencia_buscada)

es_entero("1234566")
es_entero("123Lalala")
es_entero("TENGOHAMBRE")

# 4-
def es_solo_texto(cadena_texto):
    '''
    Recibe un string y devuelve True en caso de que se trate solo de caracteres alfabeticos
    y el espacio, en caso contrario devuelve False
    '''
    coincidencia_buscada = bool(re.match("^[a-zA-Z ]*$", cadena_texto)) 
    print(coincidencia_buscada)

es_solo_texto("1234566")
es_solo_texto("123Lalala")
es_solo_texto("TENGO hambre")

# 5- 
def es_decimal(primer_texto, segundo_texto):
    '''
    Recibe 2 string, el 1ro representa la expresion a evaluar y el 2do el
    separador decimal (punto o coma). Devuelve True en caso de ser un 
    numero decimal, y False en caso contrario.
    '''
    coincidencia_buscada = bool(re.match("^[0-9{0}]*$".format(segundo_texto), primer_texto)) 
    print(coincidencia_buscada)

es_decimal("902.36", ".")
es_decimal("902,36", ",")
es_decimal("1tengo2.hambre3", ".")

# 6- 
def es_alfanumerico(cadena_texto):
    '''
    Recibe un string, devuelve True en caso de tratarse de solo letras y numeros, 
    y False en el caso contrario (que contenga caracteres especiales)
    '''
    coincidencia_buscada = bool(re.match("^[0-9a-zA-z]*$", cadena_texto)) 
    print(coincidencia_buscada)

es_alfanumerico("T3ng0H4mbr3")
es_alfanumerico("123Tengo Hambre")
es_alfanumerico("Tengo  $%&/ hambre")

# 7-
def es_binario(cadena_texto):
    '''
    Recibe un string, y devuelve True en caso de que sea un numero binario,
    en caso contrario devuelve False
    '''
    coincidencia_buscada = bool(re.match("^[0-1]*$", cadena_texto)) 
    print(coincidencia_buscada)

es_binario("1001")
es_binario("Tnego1010Hambre")
es_binario("1234556")

# 8-
def imprimir_coincidencia(lista_palabras, caracter_buscado):
    '''
    Recbe una lista de palabras y devuelva otra lista con las palabras 
    que comienzan con el caracter buscado que es el segundo parametro.
    (En este caso, la letra U)
    '''
    concidencias = []
    for palabra in lista_palabras:
        if bool(re.match(caracter_buscado, palabra)) == True:
            concidencias.append(palabra)
    print(concidencias)

imprimir_coincidencia(["Hola", "Uno", "Uruguay", "Tengo", "hambre", "Ukelele"], "U")

# 9- <>
def imprimir_palabras_segun_longitud(cadena_texto):
    '''
    Recibe un texto y devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo
    '''
    lista_palabras = []
    cadena_ingresada = re.split(" ", cadena_texto)
    for palabra in cadena_ingresada:
        if len(palabra) >= 3 and len(palabra) <= 6:
            lista_palabras.append(palabra)
    
    print(lista_palabras)

imprimir_palabras_segun_longitud("Hola tengo mucha hambre y muchisimo sueño")
#                                  4     5     5     6     1      9       5

# 10-
def imprimir_coincidencia_segun_terminacion(cadena_texto, coincidencia_buscada):
    '''
    Recibe un texto y devuelve una lista con todas las palabras que terminan
    en la coincidencia buscada (En este caso "ción")
    '''

texto = "La tecnologia de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización"







