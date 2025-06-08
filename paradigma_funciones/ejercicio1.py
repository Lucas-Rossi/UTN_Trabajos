def procesar_productos(lista:list, funcion:callable):
    return funcion(lista)

def filtrar_por_categoria(campo:str,valor:str):
    def filtrar(lista:str):   
        productos_filtrados = []
        for producto in lista:
            if producto[campo] == valor:
                productos_filtrados.append(producto)
        return productos_filtrados
    return filtrar

def calcular_precio_promedio(lista:list):
    total = 0
    for producto in lista:
        total += producto["precio"]
    promedio = total / len(lista)
    return promedio

productos = [
 {"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"},
 {"nombre": "Silla", "precio": 150, "categoria": "hogar"},
 {"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"},
 {"nombre": "Mesa", "precio": 300, "categoria": "hogar"},
 {"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"}
]

campo = "nombre"
valor = "Laptop"
filtro= filtrar_por_categoria(campo, valor)
filtrar=procesar_productos(productos, filtro)
print(filtrar)

promedio=procesar_productos(productos, calcular_precio_promedio)
print(promedio)
