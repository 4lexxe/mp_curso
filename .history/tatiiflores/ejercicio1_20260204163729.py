lista_de_nombres=[]
lista_de_edad=[]
lista_de_salarios=[]


def validar_empleado(nombre):
    pos=-1#no existe
    for i in range (len(lista_de_nombres)):
        if lista_de_nombres[i]==nombre:
            pos=i
            break
    return pos 
def agregar_empleado():
    nombre=input("ingrese el nombre para saber si existe")
    pos=validar_empleado(nombre)
    if pos==-1:
        edad=int(input("ingrese edad"))
        salario=int(input("ingrese el salario"))
        lista_de_nombres.append(nombre)
        lista_de_edad.append(edad)
        lista_de_salarios.append(salario)
    else:
        print("existe el empeado")

def busscar_un_empleado():
    nombre=input("ingrese el nombre para saber si existe")
    pos=validar_empleado(nombre)
    if pos!=-1:
        for i in range(len(lista_de_nombres)):
            print(f"{lista_de_nombres[i]},{lista_de_edad[i]},{lista_de_salarios[i]}")
    else:
        print("el empleado no existe")

def comparar_salario():
    max= lista_de_salarios[0]
    pos=0
    for i in range(len(lista_de_salarios)):
        if lista_de_salarios[i]>max:
            max=lista_de_salarios[i]
            pos=i
    print(f"el empleado con mayor salario es:{lista_de_nombres[pos]}, su edad es:{lista_de_edad[pos]}, salario:{max}")

#principal
agregar_empleado()
busscar_un_empleado()
comparar_salario()
comparar_salario()