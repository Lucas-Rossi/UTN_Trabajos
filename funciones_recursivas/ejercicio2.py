#Realizar una función recursiva que calcule la potencia de un número:
def potencia(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base,exponente - 1)

base=2
exponente=3
print(f"{base}**{exponente}={potencia(base,exponente)}")