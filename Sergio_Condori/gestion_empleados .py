"""
Sistema de Gestión de Empleados
Maneja información de empleados usando listas paralelas

Autor: Sergio Condori
"""

# Listas paralelas para almacenar datos de empleados
nombres_empleados = []
edades_empleados = []
salarios_empleados = []


def existe_empleado(nombre):
    """Verifica si un empleado ya existe en el sistema"""
    return nombre.lower() in [n.lower() for n in nombres_empleados]


def obtener_indice_empleado(nombre):
    """Obtiene el índice de un empleado en las listas"""
    for i, nombre_almacenado in enumerate(nombres_empleados):
        if nombre_almacenado.lower() == nombre.lower():
            return i
    return -1


def agregar_empleado():
    """Agrega un nuevo empleado al sistema"""
    print("\n--- AGREGAR EMPLEADO ---")
    
    nombre = input("Ingrese el nombre del empleado: ").strip()
    
    if existe_empleado(nombre):
        print(f"Error: El empleado '{nombre}' ya existe en el sistema.")
        return
    
    # Validar y obtener edad
    while True:
        try:
            edad = int(input("Ingrese la edad del empleado: "))
            if edad < 18 or edad > 100:
                print("Error: La edad debe estar entre 18 y 100 años.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido para la edad.")
    
    # Validar y obtener salario
    while True:
        try:
            salario = float(input("Ingrese el salario del empleado: "))
            if salario <= 0:
                print("Error: El salario debe ser un valor positivo.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido para el salario.")
    
    # Agregar a las listas
    nombres_empleados.append(nombre)
    edades_empleados.append(edad)
    salarios_empleados.append(salario)
    
    print(f"Empleado '{nombre}' agregado exitosamente.")


def buscar_empleado():
    """Busca y muestra la información de un empleado"""
    print("\n--- BUSCAR EMPLEADO ---")
    
    nombre = input("Ingrese el nombre del empleado a buscar: ").strip()
    indice = obtener_indice_empleado(nombre)
    
    if indice == -1:
        print(f"El empleado '{nombre}' no existe en el sistema.")
    else:
        print(f"\nInformación del empleado:")
        print(f"  Nombre: {nombres_empleados[indice]}")
        print(f"  Edad: {edades_empleados[indice]} años")
        print(f"  Salario: ${salarios_empleados[indice]:,.2f}")


def comparar_salarios():
    """Compara salarios y muestra el empleado con mayor salario"""
    print("\n--- COMPARAR SALARIOS ---")
    
    if not nombres_empleados:
        print("No hay empleados en el sistema.")
        return
    
    # Encontrar el índice del salario máximo
    salario_maximo = salarios_empleados[0]
    indice_maximo = 0
    
    for i, salario in enumerate(salarios_empleados):
        if salario > salario_maximo:
            salario_maximo = salario
            indice_maximo = i
    
    print(f"El empleado con mayor salario es:")
    print(f"  Nombre: {nombres_empleados[indice_maximo]}")
    print(f"  Edad: {edades_empleados[indice_maximo]} años")
    print(f"  Salario: ${salario_maximo:,.2f}")


def mostrar_estadisticas():
    """Muestra estadísticas generales del sistema"""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    
    total_empleados = len(nombres_empleados)
    
    if total_empleados == 0:
        print("No hay empleados en el sistema.")
        return
    
    # Calcular promedios
    promedio_edades = sum(edades_empleados) / total_empleados
    promedio_salarios = sum(salarios_empleados) / total_empleados
    
    # Encontrar salario mínimo
    salario_minimo = min(salarios_empleados)
    indice_minimo = salarios_empleados.index(salario_minimo)
    
    print(f"Total de empleados: {total_empleados}")
    print(f"Edad promedio: {promedio_edades:.1f} años")
    print(f"Salario promedio: ${promedio_salarios:,.2f}")
    print(f"Empleado con menor salario: {nombres_empleados[indice_minimo]} (${salario_minimo:,.2f})")


def mostrar_todos_empleados():
    """Muestra todos los empleados en el sistema"""
    print("\n--- LISTA DE EMPLEADOS ---")
    
    if not nombres_empleados:
        print("No hay empleados en el sistema.")
        return
    
    for i in range(len(nombres_empleados)):
        print(f"\n{i+1}. {nombres_empleados[i]}")
        print(f"   Edad: {edades_empleados[i]} años")
        print(f"   Salario: ${salarios_empleados[i]:,.2f}")


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("="*50)
    print("1. Agregar empleado")
    print("2. Buscar empleado")
    print("3. Comparar salarios (mostrar mayor)")
    print("4. Mostrar estadísticas")
    print("5. Mostrar todos los empleados")
    print("6. Salir")
    print("="*50)


def ejecutar_sistema():
    """Función principal que ejecuta el sistema"""
    print("Bienvenido al Sistema de Gestión de Empleados")
    
    while True:
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            buscar_empleado()
        elif opcion == "3":
            comparar_salarios()
        elif opcion == "4":
            mostrar_estadisticas()
        elif opcion == "5":
            mostrar_todos_empleados()
        elif opcion == "6":
            print("\n¡Gracias por usar el Sistema de Gestión de Empleados!")
            print("Saliendo del sistema...")
            break
        else:
            print("\nError: Opción inválida. Por favor seleccione una opción del 1 al 6.")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    ejecutar_sistema()