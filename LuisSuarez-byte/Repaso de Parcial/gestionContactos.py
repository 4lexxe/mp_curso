"""
Diseñar un programa modular para gestionar contactos. El programa debe permitir al usuario realizar las siguientes operaciones: 

• Agregar un contacto: El usuario debe poder ingresar el nombre, número de teléfono y correo electrónico del contacto a agregar. Validar que el teléfono no se
repita.
• Ejemplo: 
        María, 984888999, maria@gmail.com 

• Antes de  guardar un contacto: debe validarse que tenga un formato válido. Esto significa que debe tener una "@" y la misma no puede estar ni al inicio ni
al final de la cadena de caracteres. Además, los dominios comunes tampoco son válidos, su longitud no puede ser menor a 7 caracteres. 
• También debe validar que el nombre no posea caracteres numéricos ni especiales; considere solo letras, espacios y (* - . /) 
• Buscar un contacto: El usuario debe poder buscar un contacto por su nombre. Si el contacto existe, se debe imprimir por pantalla el número de teléfono y su
correo. Si no existe, debe mostrarse un mensaje de que el contacto no se encontró. Para esto, se leerá el contenido del fichero en una lista.
"""

def validarEmail(email):
    if "@" not in email:
        return False
    
    if email.startswith("@") or email.endswith("@"):
        return False
    
    # Divide el texto en dos partes (por el 1), antes de @ y despues de este. El de antes de @ se asigna a usuario y el de despues de @ se asigna a dominio
    usuario, dominio=email.split("@",1)

    if email.count("@") != 1:
        return False

    if len(dominio)<7:
        print("Dominio demasiado corto.")
        return False

    return True

def validarNombre(nombre):
    caracteresPermitidos="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ *-./"

    if any(caracter not in caracteresPermitidos for caracter in nombre):
        print("Nombre no admitido. Tiene caracteres invalidos.")
        return True
    else:
        return False

def validarTelefono(telefono):
    try:
        with open("contactos.txt", "r") as archivo:
            for linea in archivo:
                if telefono in linea:
                    return True
    except FileNotFoundError:
        return False
    return False

def agregarContacto():
    with open("contactos.txt","a") as archivo:

        nombre=str(input("Ingrese su nombre: ")).title()
        while validarNombre(nombre):
            nombre=str(input("Ingrese un nombre válido: "))
        
        email=str(input("Ingrese su email: "))
        while not validarEmail(email):
            email=str(input("Email inválido. Ingreselo nuevamente:"))
        
        telefono=str(input("Ingresé su número de telefono: "))
        while validarTelefono(telefono):
            telefono=str(input("Ingresé un telefono válido: "))

        # Guardar contacto
        archivo.write(f"{nombre}, {telefono}, {email}\n")
        print("Contacto agregado correctamente.")

def buscarContacto():
    with open("contactos.txt","r") as archivo:
        listaContactos=[]
        nombre=str(input("Ingrese el nombre del contacto a buscar: ")).title()

        for linea in archivo:
            contacto=linea.strip().split(",")

            listaContactos.append(contacto) # Será una lista anidada de cada contacto
        
        for contacto in listaContactos:
            if contacto[0]==nombre:
                print(f"Contacto: {contacto[0]}; Teléfono: {contacto[1]}; Correo: {contacto[2]}")
                return
        
        print("El usuario no ha sido encontrado.")
            











    return

avanzar=True
while avanzar:
    print("--- Gestión de Contactos ---")
    print("1. Agregar un contacto.")
    print("2. Buscar un contacto.")
    print("3. Salir.")
    accion=int(input("Ingrese la acción a realizar: "))
    while accion not in [1,2,3]:
        accion=int(input("Ingrese una acción válida: "))

    if accion==1:
        agregarContacto()
    if accion==2:
        buscarContacto()
    else:
        avanzar=False
