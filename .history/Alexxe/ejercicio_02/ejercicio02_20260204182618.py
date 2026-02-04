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
      if contacto[1] == telefono:
         return False #que si existe
      
   return True #que no existe
#-----------------------------------------------------------

#-----------------------------------------------------------
#VALIDACIONES
def validar_correo(correo):
  #longitud del correo
   if len(correo) < 7:
     return False
   
  #contener un '@'
   if "@" not in correo:
     return False
    
  #métodos integrados de cadenas (strings) utilizados para validar si una cadena comienza o termina con una subcadena específica'''

   if correo.startwith("@") or correo.endswith("@"):
      return False
   
   return True
#-----------------------------------------------------------

#-----------------------------------------------------------
#VALIDACIONES
def validar_nombre(nombre):
   for caracter in nombre:
      if not(caracter.isalpha() or caracter in "*-./"):
         return False
   
   return True
#-----------------------------------------------------------

#-----------------------------------------------------------
def buscar_contacto(nombre_buscar, contactos):
   for contacto in contactos:
      if nombre_buscar.capitalize() == contacto[0].capitalize():
        print("Contacto encontrado")
        print(f"Nombre: {contacto[0]}")
        print(f"Telefono: {contacto[1]}")            
        print(f"Correo: {contacto[2]}")
        print("\n --------------------") #Alt GR + \

   print("El contacto no se encontró.")
#-----------------------------------------------------------

#principal

#1 leer el fichero
contactos = leer_contactos()
print(contactos)

#2. validar el nombre
nombre = input("ingrese el nombre: ")
es_valido = validar_nombre(nombre)
while not es_valido:
  nombre = input("ingrese el nombre valido: ")
  es_valido = validar_nombre(nombre)

#3. validar correo
correo = input("Ingrese el correo: ")
es_valiido_correo = validar_correo(correo)

while not es_valiido_correo:
   correo = input("Ingrese el correo valido: ")
   es_valiido_correo = validar_correo(correo)


#4. validar telefono
telefono = int(input("Ingrese el telefono: "))
es_valido_telefono = validar_telefono_unico(telefono, contactos)

while not es_valido_telefono:
   telefono = int(input("Ingrese el telefono unico: "))
   es_valido_telefono = validar_telefono_unico(telefono, contactos)


#5. agregar el contacto
agregar_contactos(nombre, telefono, correo)

#6. buscar el contacto
nombre_buscar = input("Ingrese el nombre a buscar del contacto: ")

