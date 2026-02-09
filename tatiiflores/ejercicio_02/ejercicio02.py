
def leer_contacto():
   archivo= open("contactos.txt","r",encoding="utf-8")
   contactos=[]
   for linea in archivo:
      datos=linea.strip().split(",")
      contacto=[]
      for dato in datos:
         contacto.append(dato.strip())
      contactos.append(contacto)
   archivo.close()

   return contactos

def validar_telefono(telefono,contactos):
   pos=-1
   for contacto in contactos:
      if telefono == contacto[1]:
         pos=contacto
   return pos

def validar_correo(correo):
      
   if len(correo)<7:
         return False
   if "@" not in correo:
         return False
   if correo[0]=="@" or correo[-1]=="@":
         return False
   return True  

def validar_nombre(nombre):
   for letra in nombre:
       if not letra.isalpha() and not ( letra.isspace()):
           return False
       if letra in "*-./":
           return False
   return True  
 

def agregar_un_contacto():
   archivo=open("contactos.txt","a",encoding="UTF-8")
   nombre=input("ingrese el nombre")
   if validar_nombre(nombre):
       telefono= input("ingrese el numero de telefono")
       pos=validar_telefono(telefono,contactos)
       if pos==-1:
         
           if validar_correo(correo):
            archivo.write(f"\n{nombre},{telefono},{correo}\n")
            print("se agrego el contacto con existo")
   archivo.close()

def buscar_contacto(contactos):
    nombre=input("ingrese el nombre para buscarlo/a")
    if not(not validar_nombre(nombre)):
        for contacto in contactos:
            print(contacto)
            if nombre.lower()==contacto[0].lower():
                print("el contacto se encontro perfectamente")
                print(f"nombre:{contacto[0]},telefono:{contacto[1]},correo:{contacto[2]}")
                

#primcipal
telefono=""
contactos=leer_contacto()
print(validar_telefono(telefono,contactos))
while not validar_telefono(telefono,contactos)==-1:
    print("telefono incorrecto escribalo de nuevo")
    telefono=input("ingrese el telefono")
correo=correo=input("ingrese el correo")
while not validar_correo(correo):
    print("correo incorrecto, ingrese el correo nuevamnete")  
    correo=input("ingrese el correo")
nombre=""
while not validar_nombre(nombre):
    print("nombre incorrecto ingrese nuevamente el nombre")
    nombre=input("ingrese el nombre")
   
leer_contacto()
agregar_un_contacto()
buscar_contacto(contactos)
