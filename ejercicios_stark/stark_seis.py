




def ordenar_lista(lista_heroes:list, orden_ascendente:bool == True, clave:str):
    rango_lista = len(lista_heroes) - 1
    flag_ordenar = True

    while(flag_ordenar):
        flag_ordenar = False

        for indice_heroes in range(rango_lista):
            if orden_ascendente == False and lista_heroes[indice_heroes][clave] < lista_heroes[indice_heroes +1][clave] \
                or orden_ascendente == True and lista_heroes[indice_heroes][clave] > lista_heroes[indice_heroes +1][clave]:
                lista_heroes[indice_heroes], lista_heroes[indice_heroes +1][clave] = lista_heroes[indice_heroes +1, lista_heroes[indice_heroes]][clave]
                flag_ordenar = True

    return lista_heroes


def ordenar_por_altura(lista_heroes):
    '''
    Crear una función llamada ‘ordenar_por_altura’ que reciba como parámetro la lista 
    de héroes y devuelva la lista ordenada por la altura de cada personaje de menor a mayor. 
    '''
    clave = "altura"
    return ordenar_lista(lista_heroes, True, clave)

def ordenar_por_peso(lista_heroes):
    '''
    Crear una función llamada ‘ordenar_por_peso’ que reciba como parámetro 
    la lista de héroes y devuelva la lista ordenada por el peso de cada personaje mayor a mayor.
    '''
    clave = "peso"
    return ordenar_lista(lista_heroes, False, clave)

def ordenar_por_nombre(lista_heroes):
    '''
    Crear una función llamada ‘ordenar_por_nombre’ que reciba como parámetro la 
    lista de héroes y la devuelva la lista de héroes ordenada por nombres de 
    forma alfabética ascendente (de la A a la Z)
    '''
    




