def numero_es_par_o_no(numero:int):
    resultado = False
    if numero % 2 == 0:
        resultado = True
    return resultado

numero=int(input("ingrese un numero: "))
resultado2=numero_es_par_o_no(numero)
print(f"el numero es par {resultado2}")





        
    