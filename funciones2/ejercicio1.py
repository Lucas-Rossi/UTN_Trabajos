#Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área
def calcular_area_rectangulo():
    base=int(input("ingrese la base: "))
    altura=int(input("ingrese la altura: "))
    calculo = base * altura
    return calculo
print("el area es: ",calcular_area_rectangulo())