estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"] 
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar(apellidos:list, estudiantes:list, nota:list):
    for i in range(len(apellidos) - 1):
        for j in range(i + 1, len(apellidos)):
            if apellidos[i] > apellidos[j]:
                aux_apellido = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux_apellido

                aux_estudiante = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux_estudiante

                aux_nota = nota[i]
                nota[i] = nota[j]
                nota[j] = aux_nota

            elif apellidos[i] == apellidos[j]:
                if estudiantes[i] > estudiantes[j]:                   
                    aux_apellido = apellidos[i]
                    apellidos[i] = apellidos[j]
                    apellidos[j] = aux_apellido

                    aux_estudiante = estudiantes[i]
                    estudiantes[i] = estudiantes[j]
                    estudiantes[j] = aux_estudiante

                    aux_nota = nota[i]
                    nota[i] = nota[j]
                    nota[j] = aux_nota

                elif estudiantes[i] == estudiantes[j]:
                    if nota[i] < nota[j]:
                        aux_apellido = apellidos[i]
                        apellidos[i] = apellidos[j]
                        apellidos[j] = aux_apellido

                        aux_estudiante = estudiantes[i]
                        estudiantes[i] = estudiantes[j]
                        estudiantes[j] = aux_estudiante

                        aux_nota = nota[i]
                        nota[i] = nota[j]
                        nota[j] = aux_nota

ordenar(apellidos, estudiantes, nota)

for i in range(len(apellidos)):
    print(apellidos[i],estudiantes[i], nota[i])


