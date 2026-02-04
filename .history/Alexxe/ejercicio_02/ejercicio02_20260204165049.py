#Agregar un contacto

#Antes  de  guardar  un  contacto

#También debe validar que el nombre no posea caracteres numéricos ni especiales

#Buscar un contacto

def leer_contactos():
    archivo = open("contactos.txt", "r", encoding="utf-8")
    contactos = []
    
    #Recorrer cada línea del archivo

