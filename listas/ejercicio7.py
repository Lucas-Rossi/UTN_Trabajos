from listas_personas import *
def listar_usuarios_mexico(country: list, region: list, nombres: list, edades: list, postalZip: list, mails: list, address: list, telefonos: list):
    for i in range(len(country)):
        if country[i] == "Mexico":               
            print(f"pais:{country[i]}, region:{region[i]}, nombre:{nombres[i]}, edad:{edades[i]}, postalzip:{postalZip[i]}, mail:{mails[i]}, adress:{address[i]}, telefono:{telefonos[i]} ")

#listar_usuarios_mexico(country, region, nombres, edades, postalZip, mails, address, telefonos)

def listar_usuarios_brazil(country: list, nombres:list,  mails: list,  telefonos: list):
    for i in range(len(country)):
        if country[i] == "Brazil":               
            print(f"pais:{country[i]}, nombre:{nombres[i]}, mail:{mails[i]}, telefono:{telefonos[i]} ")

#listar_usuarios_brazil(country, nombres, mails, telefonos)

def listar_usuarios_mas_jovenes(country: list, region: list, nombres: list, edades: list, postalZip: list, mails: list, address: list, telefonos: list):
    menor=edades[0]
    for i in range(len(edades)):
        if edades[i] <= menor:
            menor=edades[i]
            print(f"edad:{edades[i]}, pais:{country[i]}, region:{region[i]}, nombre:{nombres[i]}, postalzip:{postalZip[i]}, mail:{mails[i]}, adress:{address[i]}, telefono:{telefonos[i]} ")

#listar_usuarios_mas_jovenes(country, region, nombres, edades, postalZip, mails, address, telefonos)

def promediar_edad(edades:list):
    contador=0
    suma=0
    for i in range(len(edades)):
        suma+=edades[i]
        contador+=1
    promedio=suma/contador
    print("el promedio de edad es:", promedio)

#promediar_edad(edades)

def encontrar_mayor_edad_brazil(edades:list,country: list, region: list, nombres: list, postalZip: list, mails: list, address: list, telefonos: list):
    for i in range(len(country)):   
        if country[i] == "Brazil":
            mayor = edades[i]
            if edades[i]> mayor:
                mayor=edades[i]
    print(f"el mayor es :{nombres[i]} tiene {mayor}, pais:{country[i]}, region:{region[i]},postalzip:{postalZip[i]}, mail:{mails[i]}, adress:{address[i]}, telefono:{telefonos[i]} ")

#encontrar_mayor_edad_brazil(country, edades, region, nombres, postalZip, mails, address, telefonos)


def encontrar_codigo_postal(country:list, postalZip:list):
    for i in range(len(country)):
        if country[i]=="Mexico" or country[i]=="Brazil":
            if postalZip[i] > 8000:
                print(f" pais:{country[i]}, postalzip:{postalZip[i]}, edad:{edades[i]}, region:{region[i]}, nombre:{nombres[i]}, mail:{mails[i]}, adress:{address[i]}, telefono:{telefonos[i]} ")
#encontrar_codigo_postal(country,postalZip)

def listar_italianos(country:list,edades:list):
    for i in range(len(country)):
        if country[i] == "Italy":
            if edades[i]>40:
                print(f"{nombres[i]}, {edades[i]}, {mails[i]}, {telefonos[i]}")
#listar_italianos(country,edades)

def buscar_datos():
    print("seleccione una opcion")
    seguir="s"
    while seguir =="s":
        print("1- Listar los datos de los usuarios de México")
        print("2- Listar los nombre, mail y teléfono de los usuarios de Brasil")
        print("3- Listar los datos del/los usuario/s más joven/es")
        print("4- Obtener un promedio de edad de los usuarios")
        print("5- De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("6- Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("7- Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
    
        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_usuarios_mexico(country, region, nombres, edades, postalZip, mails, address, telefonos)
        elif opcion == "2":
            listar_usuarios_brazil(country, nombres, mails, telefonos)
        elif opcion == "3":
            listar_usuarios_mas_jovenes(country, region, nombres, edades, postalZip, mails, address, telefonos)
        elif opcion == "4":
            promediar_edad(edades)
        elif opcion == "5":
            encontrar_mayor_edad_brazil(country, edades, region, nombres, postalZip, mails, address, telefonos)
        elif opcion == "6":
            encontrar_codigo_postal(country,postalZip)
        elif opcion == "7":
            listar_italianos(country,edades)
        seguir=input("quiere buscar mas datos? s/n")

buscar_datos()
        
