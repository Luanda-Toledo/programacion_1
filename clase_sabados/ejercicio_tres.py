animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 5, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 23, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 1, "personaje_principal": "Shinji Ikari"}
]

''' actividad:
1-Generar una sublista de los animes estrenados antes de 1995:
2-Generar una sublista de los animes con más de 1 temporada:
3-Buscar en la lista el anime con nombre "Pokemon" e imprimir su año de estreno:
4-Crear un nuevo diccionario con los nombres y años de estreno de los animes de la lista:
'''
# 1
lista_noventaycinco = []

for anime in animes_90s:

    if anime["año"] < 1995:
        lista_noventaycinco.append(anime)
        
print("Los animes estrenados antes de 1995 son: \n{0}".format(lista_noventaycinco))

# 2
lista_dos_temporadas = []

for anime in animes_90s:
    
    if anime["temporadas"] > 1:
        lista_dos_temporadas.append(anime)
        
print("Los animes con mas de dos temporadas son: \n{0}".format(lista_dos_temporadas))

# 3
for i in range(len(animes_90s)):
    nombre_anime = animes_90s[i]["nombre"]
    
    if nombre_anime == "Pokemon":
        año_estreno = animes_90s[i]["año"]
        print("{0} se estreno en el año: {1}".format(nombre_anime, año_estreno))
    
# 4 
nueva_lista = []

for i in range(len(animes_90s)):
    elemento_de_la_lista = {}
    elemento_de_la_lista["nombre"] = animes_90s[i]["nombre"]
    elemento_de_la_lista["año"] = animes_90s[i]["año"]
    nueva_lista.append(elemento_de_la_lista)

print("La nueva lista es: \n{0}".format(nueva_lista))