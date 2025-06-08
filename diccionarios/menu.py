from estudiantes import *
from biblioteca import *

def menu():
    list_promedio = sacar_lista_promedio(estudiantes)
    seguir="s"
    while seguir == "s":
        print("\n----- MENÚ DE OPCIONES -----")
        print("1. Ordenar estudiantes por apellido o nombre")
        print("2. Mostrar promedio de cada estudiante")
        print("3. Listar estudiantes de Ingeniería en Informática")
        print("4. Mostrar promedio de edad de los estudiantes")
        print("5. Mostrar estudiante con mayor promedio")
        print("6. Listar estudiantes que pertenecen al Club de Informática")
        print("7. Listar estudiantes con edad menor o igual a 24")
        print("8. Salir")

        opcion = int(input("Ingrese una opción 1-8: "))
        while opcion < 1 or opcion > 8:
            opcion =int(input("vuelva a ingresar una opción 1-8: "))
        if opcion == 1:
            ordenar_por_apellido_o_nombre(estudiantes)
        elif opcion == 2:
            promedio_estudiantes(estudiantes, list_promedio)
        elif opcion == 3:
            estudiantes_ingenieria_en_informatica(estudiantes)
        elif opcion == 4:
            promedio_de_edad(estudiantes)
        elif opcion == 5:
            mostrar_mayor_promedio(estudiantes, list_promedio)
        elif opcion == 6:
            encontrar_miembros_del_club_de_informatica(estudiantes, list_promedio)
        elif opcion == 7:
            listar(estudiantes)
        elif opcion == 8:
            print("fin del programa")
            seguir="n"
menu()
