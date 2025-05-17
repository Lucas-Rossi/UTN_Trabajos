nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_nombres_ascendente(edades:list,nombres:list):
    
    for i in range(len(nombres)-1):
        for j in range(i+1,len(nombres)):
            if nombres[i]>nombres[j]:
                aux=nombres[i]
                nombres[i]=nombres[j]
                nombres[j]=aux

                aux_edades = edades[i]
                edades[i] = edades[j]
                edades[j] = aux_edades
        

ordenar_nombres_ascendente(edades,nombres)
for i in range(len(nombres)):
    print(nombres[i],edades[i])
        
        
        




