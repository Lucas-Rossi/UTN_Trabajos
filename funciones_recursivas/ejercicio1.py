#Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_numeros_naturales(num):
    if num == 0:
        return num
    else:
        return num + sumar_numeros_naturales(num-1)

print(sumar_numeros_naturales(10))