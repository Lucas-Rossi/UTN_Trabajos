import copy

def procesar_peliculas(lista:list, funcion:callable):
    return funcion(lista)

def ordenar_descendente(lista):
    lista_copiada=copy.deepcopy(lista)
    for i in range(len(lista_copiada)-1):
        for j in range(i+1,len(lista_copiada)):
            if lista_copiada[i]["puntaje"] < lista_copiada[j]["puntaje"]:
                aux=lista_copiada[j]
                lista_copiada[j]=lista_copiada[i]
                lista_copiada[i]=aux
    return lista_copiada

def ordenar_ascendente(lista):
    lista_copiada=copy.deepcopy(lista)
    for i in range(len(lista_copiada)-1):
        for j in range(i+1,len(lista_copiada)):
            if lista_copiada[i]["anio"] > lista_copiada[j]["anio"]:
                aux=lista_copiada[j]
                lista_copiada[j]=lista_copiada[i]
                lista_copiada[i]=aux
    return lista_copiada

peliculas = [
 {"titulo": "Inception", "anio": 2010, "puntaje": 8.8},
 {"titulo": "The Matrix", "anio": 1999, "puntaje": 8.7},
 {"titulo": "Interstellar", "anio": 2014, "puntaje": 8.6},
 {"titulo": "Avatar", "anio": 2009, "puntaje": 7.8},
 {"titulo": "The Batman", "anio": 2022, "puntaje": 7.9}
]

peliculas_ordenadas_descendente=procesar_peliculas(peliculas, ordenar_descendente)
print(peliculas_ordenadas_descendente)

peliculas_ordenadas_asecendente=procesar_peliculas(peliculas, ordenar_ascendente)
print(peliculas_ordenadas_asecendente)