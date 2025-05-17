from listas_personas import *
def ordenar_usuarios_edad(edades:list,nombres:list, ):
    for i in range(len(edades)-1):
        for j in range(i+1,len(edades)):
            if edades[i]> edades[j]:
                aux=edades[i]
                edades[i]=edades[j]
                edades[j]=aux
                
                aux_nombres=nombres[i]
                nombres[i]=nombres[j]
                nombres[j]=aux_nombres

                aux_country=country[i]
                country[i]=country[j]
                country[j]=aux_country

                aux_region=region[i]
                region[i]=region[j]
                region[j]=aux_region

                aux_telefonos=telefonos[i]
                telefonos[i]=telefonos[j]
                telefonos[j]=aux_telefonos

                aux_mails=mails[i]
                mails[i]=mails[j]
                mails[j]=aux_mails

                aux_postalZip=postalZip[i]
                postalZip[i]=postalZip[j]
                postalZip[j]=aux_postalZip

                aux_address=address[i]
                address[i]=address[j]
                address[j]=aux_address

            elif edades[i]==edades[j]:
                if nombres[i] > nombres[j]:
                    aux_nombres=nombres[i]
                    nombres[i]=nombres[j]
                    nombres[j]=aux_nombres

                    aux=edades[i]
                    edades[i]=edades[j]
                    edades[j]=aux
                       
                    aux_country=country[i]
                    country[i]=country[j]
                    country[j]=aux_country

                    aux_region=region[i]
                    region[i]=region[j]
                    region[j]=aux_region

                    aux_telefonos=telefonos[i]
                    telefonos[i]=telefonos[j]
                    telefonos[j]=aux_telefonos

                    aux_mails=mails[i]
                    mails[i]=mails[j]
                    mails[j]=aux_mails

                    aux_postalZip=postalZip[i]
                    postalZip[i]=postalZip[j]
                    postalZip[j]=aux_postalZip

                    aux_address=address[i]
                    address[i]=address[j]
                    address[j]=aux_address
                    
ordenar_usuarios_edad(edades,nombres,)
for i in range(len (edades)):
    print(edades[i],nombres[i],country[i],region[i],telefonos[i],mails[i],postalZip[i],address[i])
