#Desarrollar una función que reciba por parámetro la lista de edades, busque a las
#personas de menor edad (puede ser más de una) y las retorne. El programa
#principal deberá mostrar nombre y edad de los menores.

def encotrar_al_menor(edades:list,nombres:list):
    edad_minima = edades[0]
    for i in range(len(edades)):    
        if edades[i]< edad_minima:
            edad_minima = edades[i]
      
    for i in range(len(edades)):
        if edades[i]==edad_minima:
            print(f"{nombres[i]} tiene {edades[i]}")
            
nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

encotrar_al_menor(edades,nombres)

