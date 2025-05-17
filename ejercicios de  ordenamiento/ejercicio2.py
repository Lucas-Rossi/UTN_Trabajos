nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_nombres_descontar_puntos(nombres:list,puntos:list):
    for i in range(len(nombres)-1):
        for j in range(i+1,len(nombres)):
            if nombres[i]>nombres[j]:
                aux=nombres[i]
                nombres[i]=nombres[j]
                nombres[j]=aux

            elif nombres[i] == nombres[j]:
                if puntos[i]<puntos[j]:
                    aux_puntos=puntos[i]
                    puntos[i]=puntos[j]
                    puntos[j]=aux_puntos
    

ordenar_nombres_descontar_puntos(nombres,puntos)
for i in range(len(nombres)):
    print(nombres[i],puntos[i])


            