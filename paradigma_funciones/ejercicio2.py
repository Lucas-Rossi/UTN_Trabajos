def procesar_estudiantes(lista:list, funcion:callable):
    return funcion(lista)

def estudiantes_aprobados(campo):
    def aprobados(lista):
        estudiantes=[]
        for estudiante in lista:
            if estudiante[campo] >= 6.0:
                estudiantes.append(estudiante)
        return estudiantes
    return aprobados

def calcular_promedio(campo):
    def sacar_promedio(lista):
        suma=0
        for estudiante in lista:
            suma+=estudiante[campo]
        promedio= suma / len(lista)
        return promedio
    return sacar_promedio

estudiantes = [
 {"nombre": "Sofía", "curso": "Matemáticas", "calificacion": 7.5},
 {"nombre": "Tomás", "curso": "Historia", "calificacion": 5.5},
 {"nombre": "Valentina", "curso": "Ciencias", "calificacion": 9.0},
 {"nombre": "Lucas", "curso": "Literatura", "calificacion": 4.0},
 {"nombre": "Martina", "curso": "Física", "calificacion": 6.8}
]

campo="calificacion"
filtro=estudiantes_aprobados(campo)
aprobados= procesar_estudiantes(estudiantes,filtro)
print(aprobados)

filtro_promedio=calcular_promedio(campo)
promedio=procesar_estudiantes(estudiantes,filtro_promedio)
print(promedio)
