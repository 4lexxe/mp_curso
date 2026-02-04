#Agregar un contacto

#Antes  de  guardar  un  contacto

#También debe validar que el nombre no posea caracteres numéricos ni especiales

#Buscar un contacto


#-----------------------------------------------------------
def leer_contactos():
    archivo = open("contactos.txt", "r", encoding="utf-8")
    contactos = []

    #Recorrer cada línea del archivo
    for linea in archivo:
      #separar la lineas por comas (nombre, telefono, email)
      #strip -> (strings) que elimina caracteres, por defecto espacios en blanco ( ), tabulaciones (\t) y saltos de línea (\n)

      #María García, 987654321, maria.garcia@email.com


      datos = linea.strip.split(",")
      #datos = [Maria garcia, 98762323, correo@4lexxe.com]

      contacto = []

      #limpiar los espacios cada datos
      for dato in datos:
         contacto.append(dato.strip())

