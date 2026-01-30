"""
La empresa necesita un sistema simple para gestionar datos de sus empleados. Para ello, se deberán utilizar tres
listas paralelas, donde cada posición representa a un mismo empleado.

Lista de nombres de empleados
Lista de edades
Lista de salarios

El sistema deberá permitir:

1.Agregar un empleado
Antes de agregar, se debe validar que el empleado no exista previamente en la lista de nombres.
Si existe, se debe informar al usuario y no agregarlo.
Si no existe, se agregan los datos en las tres listas respetando la posición.

2.Buscar un empleado
Se debe validar si el empleado existe antes de mostrar su información.
Si no existe, se debe informar correctamente.

3.Comparar salarios
El sistema deberá filtrar y mostrar cuál de los empleados tiene el salario mayor.
La comparación debe realizarse recorriendo las listas y respetando la relación entre ellas.
"""

lista_nombres=[]
lista_edades=[]
lista_salarios=[]

def agregarEmpleado():
    nombre=str(input("Ingrese el nombre del empleado: ")).upper()

    for empleado in lista_nombres:
        if empleado==nombre:
            print("El empleado ya existe, no se puede agregar.")
            return
        
    edad=int(input("Ingrese la edad del empleado: "))
    while edad<17:                
        print("Error. Edad no válida para la empresa.")
        edad=int(input("Ingrese nuevamente la edad del empleado: "))
    
    salario=float(input("Ingrese el salario del empleado: "))
    while salario<=0:
        print("Error. Salario negativo o nulo.")
        salario=float(input("Ingrese nuevamente el salario: "))

    lista_nombres.append(nombre)
    lista_edades.append(edad)
    lista_salarios.append(salario)

    return

def buscarEmpleado():
    empleado=str(input("Ingrese el nombre del empleado a buscar: ")).upper()
    pos=-1

    for i in range(len(lista_nombres)):
        if lista_nombres[i]==empleado:
            pos=i
            break
    
    if pos==-1:
        print("El empleado no existe.")
    else:
        print(f"Empleado: {empleado} | Edad: {lista_edades[pos]} | Salario: ${lista_salarios[pos]}")

    return

def compararSalarios():
    salarioMaximo=0
    posicionMayor=0

    for i in range(len(lista_salarios)):
        if lista_salarios[i]>salarioMaximo:
            salarioMaximo=lista_salarios[i]
            posicionMayor=i
    
    print(f"El empleado {lista_nombres[posicionMayor]} de {lista_edades[posicionMayor]} años tiene el mayor salario de {salarioMaximo}")
    
    return

while True:
    print("--- Menú de Opciones ---")
    print("1. Agregar empleado.")
    print("2. Buscar Empleado.")
    print("3. Comparar Salarios.")
    accion=int(input("Ingrese la acción a realizar: "))
    while accion<=0 or accion>3:
        print("Accion Inválida.")
        accion=int(input("Ingrese la acción a realizar: "))
    
    if accion==1:
        agregarEmpleado()
    elif accion==2:
        if len(lista_edades)==0:
            print("No es posible realizar esta acción porque no hay nadie registrado.")
        else:
            buscarEmpleado()
    elif accion==3:
        if len(lista_edades)==0:
            print("No es posible realizar esta acción porque no hay nadie registrado.")
        else:
            compararSalarios()
