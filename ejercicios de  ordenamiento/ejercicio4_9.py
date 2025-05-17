#9-Listar los datos de los usuarios de México ordenados por nombre
#
from listas_personas import *  

def listar_mexicanos(nombres:list,country:list,):
    nombres_mexicanos=[]
    country_mexicano=[]
    region_mexicano=[]
    edades_mexicano=[]
    telefonos_mexicano=[]
    mails_mexicano=[]
    postalZip_mexicano=[]
    address_mexicano=[]
    for i in range(len(country)):
        if country[i]=="Mexico":
             nombres_mexicanos.append(nombres[i])
             country_mexicano.append(country[i])
             region_mexicano.append(region[i])
             edades_mexicano.append(edades[i])
             telefonos_mexicano.append(telefonos[i])
             mails_mexicano.append(mails[i])
             postalZip_mexicano.append(postalZip[i])
             address_mexicano.append(address[i])
        
    for i in range(len(nombres_mexicanos) - 1):
         for j in range(i + 1, len(nombres_mexicanos)):
                if nombres_mexicanos[i] > nombres_mexicanos[j]:
                    aux=nombres_mexicanos[i]
                    nombres_mexicanos[i]=nombres_mexicanos[j]
                    nombres_mexicanos[j]=aux

                    aux_country=country_mexicano[i]
                    country_mexicano[i]=country_mexicano[j]
                    country_mexicano[j]=aux_country

                    aux_edades=edades_mexicano[i]
                    edades_mexicano[i]=edades_mexicano[j]
                    edades_mexicano[j]=aux_edades

                    aux_region=region_mexicano[i]
                    region_mexicano[i]=region_mexicano[j]
                    region_mexicano[j]=aux_region

                    aux_postalZip=postalZip_mexicano[i]
                    postalZip_mexicano[i]=postalZip_mexicano[j]
                    postalZip_mexicano[j]=aux_postalZip

                    aux_address=address_mexicano[i]
                    address_mexicano[i]=address_mexicano[j]
                    address_mexicano[j]=aux_address

                    aux_mails=mails_mexicano[i]
                    mails_mexicano[i]=mails_mexicano[j]
                    mails_mexicano[j]=aux_mails

                    aux_telefonos=telefonos_mexicano[i]
                    telefonos_mexicano[i]=telefonos_mexicano[j]
                    telefonos_mexicano[j]=aux_telefonos

    for i in range(len(nombres_mexicanos)):
     print(nombres_mexicanos[i], country_mexicano[i], region_mexicano[i], edades_mexicano[i], telefonos_mexicano[i], mails_mexicano[i], postalZip_mexicano[i], address_mexicano[i])


listar_mexicanos(nombres,country)



            
                
