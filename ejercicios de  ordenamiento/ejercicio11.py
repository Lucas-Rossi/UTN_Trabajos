#11-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000, ordenado por nombre y edad de manera descendente

from listas_personas import *

def listar_usuarios_mexico_brasil(nombres:list, country:list):
    nombres_filtrados = []
    country_filtrados = []
    region_filtrados = []
    edades_filtradas = []
    telefonos_filtrados = []
    mails_filtrados = []
    postalZip_filtrados = []
    address_filtrados = []

    for i in range(len(country)):
        if (country[i] == "Mexico" or country[i] == "Brazil") and postalZip[i] > 8000:
            nombres_filtrados.append(nombres[i])
            country_filtrados.append(country[i])
            region_filtrados.append(region[i])
            edades_filtradas.append(edades[i])
            telefonos_filtrados.append(telefonos[i])
            mails_filtrados.append(mails[i])
            postalZip_filtrados.append(postalZip[i])
            address_filtrados.append(address[i])

    for i in range(len(nombres_filtrados) - 1):
        for j in range(i + 1, len(nombres_filtrados)):
            if nombres_filtrados[i] < nombres_filtrados[j]:
                
                aux = nombres_filtrados[i]
                nombres_filtrados[i] = nombres_filtrados[j]
                nombres_filtrados[j] = aux

                aux = country_filtrados[i]
                country_filtrados[i] = country_filtrados[j]
                country_filtrados[j] = aux

                aux = region_filtrados[i]
                region_filtrados[i] = region_filtrados[j]
                region_filtrados[j] = aux

                aux = edades_filtradas[i]
                edades_filtradas[i] = edades_filtradas[j]
                edades_filtradas[j] = aux

                aux = telefonos_filtrados[i]
                telefonos_filtrados[i] = telefonos_filtrados[j]
                telefonos_filtrados[j] = aux

                aux = mails_filtrados[i]
                mails_filtrados[i] = mails_filtrados[j]
                mails_filtrados[j] = aux

                aux = postalZip_filtrados[i]
                postalZip_filtrados[i] = postalZip_filtrados[j]
                postalZip_filtrados[j] = aux

                aux = address_filtrados[i]
                address_filtrados[i] = address_filtrados[j]
                address_filtrados[j] = aux

            elif edades[i] < edades[j]:

                aux = edades_filtradas[i]
                edades_filtradas[i] = edades_filtradas[j]
                edades_filtradas[j] = aux

                aux = nombres_filtrados[i]
                nombres_filtrados[i] = nombres_filtrados[j]
                nombres_filtrados[j] = aux

                aux = country_filtrados[i]
                country_filtrados[i] = country_filtrados[j]
                country_filtrados[j] = aux

                aux = region_filtrados[i]
                region_filtrados[i] = region_filtrados[j]
                region_filtrados[j] = aux

                aux = telefonos_filtrados[i]
                telefonos_filtrados[i] = telefonos_filtrados[j]
                telefonos_filtrados[j] = aux

                aux = mails_filtrados[i]
                mails_filtrados[i] = mails_filtrados[j]
                mails_filtrados[j] = aux

                aux = postalZip_filtrados[i]
                postalZip_filtrados[i] = postalZip_filtrados[j]
                postalZip_filtrados[j] = aux

                aux = address_filtrados[i]
                address_filtrados[i] = address_filtrados[j]
                address_filtrados[j] = aux


    for i in range(len(nombres_filtrados)):
        print(nombres_filtrados[i], country_filtrados[i], region_filtrados[i],
              edades_filtradas[i], telefonos_filtrados[i], mails_filtrados[i],
              postalZip_filtrados[i], address_filtrados[i])

listar_usuarios_mexico_brasil(nombres, country)
