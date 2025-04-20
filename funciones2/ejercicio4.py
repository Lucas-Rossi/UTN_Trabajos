def verificar_par_o_impar(numero):
    #recibe un numero en el parametro numero, si es par guarda True en la variable valor y si es impar guarda False y luego retorna valor
    if numero % 2 == 0:
        valor=True
    else:
        valor=False
    return valor
print(verificar_par_o_impar(1))