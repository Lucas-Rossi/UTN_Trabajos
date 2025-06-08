from estudiantes import *
def ordenar_por_apellido_o_nombre(estudiantes:list):
    #ordena la lista de forma ascendente por apelidos si se repiten, oredena por nombre
    for i in range(len(estudiantes)-1):
        for j in range(i+1,len(estudiantes)):

            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"]:
                aux=estudiantes[i]
                estudiantes[i]=estudiantes[j]
                estudiantes[j]=aux

            elif estudiantes[i]["apellido"] == estudiantes[j]["apellido"]:
                if estudiantes[i]["nombre"] > estudiantes[j]["nombre"]:
                    aux_nombre=estudiantes[i]
                    estudiantes[i]=estudiantes[j]
                    estudiantes[j]=aux_nombre

    for i in estudiantes:
        print(i["legajo"],i["nombre"],i["apellido"],i["edad"])

def sacar_lista_promedio(estudiantes:list)->list:
    #retorna la lista con todos los promedios
    lista_promedio=[]
    for i in range(len(estudiantes)):
        total=0
        notas=estudiantes[i]["notas"]
        
        for j in range(len(notas)):
            total += notas[j]
        promedio = total / len(notas)
        lista_promedio.append(promedio)
    return lista_promedio


def promedio_estudiantes(estudiantes:list,list_promedio:list):
    #muestra el promedio de cada estudiante
    for i in range(len(list_promedio)):
        print(estudiantes[i]["nombre"], estudiantes[i]["apellido"], list_promedio[i])

def  estudiantes_ingenieria_en_informatica(estudiantes):
    #muestra datos de los estudiantes que cursan el programa de ingenieria en informatica
    for i in range(len(estudiantes)):
        lista=[]
        lista.append(estudiantes[i]["programa"]["nombre"])
        for j in range(len(lista)):
            if lista[j] == "Ingenieria en Informatica":
                print(lista,estudiantes[i]["legajo"],estudiantes[i]["nombre"],estudiantes[i]["apellido"],estudiantes[i]["edad"])

def promedio_de_edad(estudiantes:list):
    #muestra el promedio de edad
    total=0
    for i in range(len(estudiantes)):
        print(estudiantes[i]["nombre"],estudiantes[i]["apellido"])
        total += estudiantes[i]["edad"]

    promedio = total / len(estudiantes)   
    print("el promedio es: ",promedio)

def mostrar_mayor_promedio(estudiantes:list, list_promedio:list):
    #busca en la lista de promedios y muestra el mayor promedio con el nombre del estudiante
    posicion=0
    mayor=list_promedio[0]
    for i in range(len(list_promedio)):
        if list_promedio[i] > mayor:
            mayor=list_promedio[i]
            posicion=i 
    print(f"El estudiante con mayor promedio es: {estudiantes[posicion]['nombre']}, {estudiantes[posicion]['apellido']} con {mayor:.2f} de promedio")

def encontrar_miembros_del_club_de_informatica(estudiantes:list,list_promedio:list):
    #muestra los miembros del lub de informatica
    for i in range(len(estudiantes)):  
        if "grupos" in estudiantes[i]:      
            grupo = estudiantes[i]["grupos"]
            for j in range(len(grupo)):
                if grupo[j]["nombre"] == "Club de Informatica":
                    print("club de informatica: ",estudiantes[i]['nombre'],estudiantes[i]['apellido'],list_promedio[i])
                
                    
def listar(estudiantes:list):
    #-Lista legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.

    for i in range(len(estudiantes)):
        if estudiantes[i]["edad"] <= 24:
            print(f"legajo: {estudiantes[i]['legajo']}-estudiante: {estudiantes[i]['nombre']} {estudiantes[i]['apellido']}--- programa: {estudiantes[i]['programa']['nombre']}")
