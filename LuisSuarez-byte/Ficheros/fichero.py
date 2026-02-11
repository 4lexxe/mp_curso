"""""
Diseñar un programa modular para gestionar tareas. El programa debe permitir al usuario realizar las siguientes operaciones:

Agregar una tarea:
El usuario debe poder ingresar la fecha en formato dd-mm-yyyy, la hora en formato hh:mm, y la descripción de la tarea a agregar. También debe asignarse el
estado de la tarea, cuyo valor por defecto será "Registrada", y un número de tarea generado automáticamente de forma secuencial.
La información debe almacenarse en un archivo llamado tareas.txt. Cada tarea se debe guardar en una línea diferente, donde cada atributo estará separado por
punto y coma.

Ejemplo del archivo:
1; 10-05-2024; 10:30; Enviar instrucciones a 3 clientes; Registrada
2; 10-05-2024; 12:00; Consulta médico; Registrada
3; 11-05-2024; 14:00; Reunión con coordinadores; Completada

Validaciones:
Antes de guardar la tarea, deben realizarse las siguientes validaciones:
• Fecha y hora: Asegurarse de que la fecha tenga un formato válido ddmm-yyyy y que la hora esté en el formato hh:mm. Además, validar que el valor de la fecha
  y la hora se encuentre dentro de rangos posibles.
• Descripción: La descripción de la tarea no debe estar vacía.

Buscar una tarea:
El usuario debe poder buscar una tarea por su número de tarea (ID). Si la tarea existe, se debe imprimir por pantalla su descripción, fecha, hora y estado. Si
no existe, debe mostrarse un mensaje de que la tarea no se encontró. Para realizar esta búsqueda, se leerá el contenido del archivo tareas.txt y se procesará
en una lista.

Consideraciones:
• La solución entregada debe estar correctamente modularizada, siguiendo las características de Clean Code.
• El archivo tareas.txt no existe al inicio del programa y se debe crear al agregar la primera tarea.
"""

def agregarTarea():
    archivo=open("tareas.txt", "a", encoding="UTF-8")
    tarea=1

    dia=int(input("Ingrese fecha: "))
    while dia<1 or dia>31:
        dia=int(input("Ingrese nuevamente la fecha: "))
    mes=int(input("Ingrese el mes: "))
    while mes<1 or mes>12:
        mes=int(input("Ingrese nuevamente el mes: "))
    año=int(input("Ingrese el año: "))
    while año<1970:
        año=int(input("Ingrese nuevamente el año: "))
    fecha=f"{dia}-{mes}-{año}"

    hora=int(input("Ingrese la hora de la tarea: "))
    while hora<0 or hora>=24:
        hora=int(input("Ingrese nuevamente la hora de la tarea: "))
    minuto=int(input("Ingrese el minuto de la tarea: "))
    while minuto<0 or minuto>60:
        minuto=int(input("Ingrese nuevamente el minuto de la tarea: "))
    horario=f"{hora}:{minuto}"

    descripcion=str(input("Ingrese la tarea que realizó: ")).strip().capitalize()
    while descripcion=="":
        descripcion=str(input("Ingrese nuevamente la tarea que realizó: ")).strip().capitalize()


    archivo.write(str(tarea)+"; "+fecha+"; "+horario+"; "+descripcion+"; Registrada\n")

    tarea+=1
    archivo.close()
    return

def verTareas():

    return



def buscarTarea():
    buscarID=str(input("Ingrese el ID de la tarea a buscar: "))




    return





agregarTarea()