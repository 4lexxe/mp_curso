#Agregar un contacto

#Antes  de  guardar  un  contacto: validar

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
         contacto.append(dato.strip())#contacto = [maria, 123, a@a]

      #agregar el contacto a la lista de contactos

      contactos.append(contacto)

    archivo.close()
    return contactos
#-----------------------------------------------------------

#-----------------------------------------------------------
def agregar_contactos(nombre, telefono, correo):
   archivo = open("contactos.txt", "a", encoding="UTF-8")

   archivo.write(f"{nombre}, {telefono}, {correo}")
   archivo.close()
   print("el contacto se agregó exitosamente")
#-----------------------------------------------------------

#-----------------------------------------------------------
#VALIDACIONES
def validar_telefono_unico(telefono, contactos):
   for contacto in contactos:
      if len(contacto >= 2 and contacto[1])
#-----------------------------------------------------------

