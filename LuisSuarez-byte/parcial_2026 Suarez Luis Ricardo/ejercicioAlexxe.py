"""
================================================================================
CONSIGNA DEL EJERCICIO - EXAMEN PARCIAL 2026 (EMC)
================================================================================

Duración: 4 horas  
Horario: 16:15 hs a 20:15 hs  
Modalidad: Individual  
Lenguaje: Python  

IMPORTANTE:
• Para rendir el examen puede hacerlo en computadora o en papel.
• El desarrollo completo es obligatorio.
• Luego debe subir el código al repositorio respetando la estructura indicada.

================================================================================
SITUACIÓN PROBLEMA
================================================================================

Una empresa de venta de electrodomésticos llamada "TECNOHOGAR" almacena la 
información de sus ventas en un archivo de texto llamado:

electrodomesticos.txt

Cada línea del archivo tiene el siguiente formato:

codigo;fecha;producto;marca;cliente;estado;precio

Donde:
• codigo: código único del electrodoméstico vendido (ej: E001)
• fecha: fecha de venta (formato YYYY-MM-DD)
• producto: nombre del producto (Heladera, Lavarropas, Microondas, etc.)
• marca: marca del electrodoméstico
• cliente: nombre del cliente
• estado: "entregado", "pendiente" o "cancelado"
• precio: precio del producto (valor numérico)

Ejemplo de línea:
E001;2026-03-10;Heladera;Samsung;Maria Lopez;entregado;350000

================================================================================
CONDICIÓN SOBRE EL ARCHIVO
================================================================================

Si el archivo electrodomesticos.txt NO existe:

• Se debe lanzar una excepción.
• Capturar la excepción con try-except.
• Crear automáticamente el archivo.
• Cargar al menos 5 registros de ejemplo.
• Luego realizar nuevamente la lectura del archivo.

================================================================================
NOTA IMPORTANTE
================================================================================

Para aprobar el examen el alumno debe:

✔ Resolver los puntos obligatorios.
✔ Resolver al menos 4 consignas adicionales.
✔ Utilizar funciones correctamente modularizadas.
✔ Trabajar con archivos.
✔ Aplicar buenas prácticas de programación.

================================================================================
CONSIGNAS
================================================================================

1) Implementar la función que lea el archivo electrodomesticos.txt y devuelva 
   una lista con todos los registros.

--------------------------------------------------------------------------------

2) Listar todos los electrodomésticos vendidos en un año y mes ingresado por 
   el usuario (formato YYYY y MM), excluyendo las ventas realizadas al cliente 
   llamado "administrador".

   Mostrar:
   Producto - Cliente - Estado

--------------------------------------------------------------------------------

3) Solicitar una marca al usuario y mostrar cuántos productos de esa marca 
   fueron vendidos en total.

--------------------------------------------------------------------------------

4) Mostrar todos los electrodomésticos que no hayan sido entregados 
   (estado distinto a "entregado").

   Mostrar:
   Código - Producto - Cliente - Estado

--------------------------------------------------------------------------------

5) Listar los 3 clientes con mayor cantidad de compras realizadas.
   Debe ordenarse de mayor a menor utilizando el método burbuja.

   Mostrar:
   Cliente - Cantidad de compras

--------------------------------------------------------------------------------

6) Permitir eliminar un registro según su código.
   El usuario debe ingresar el código del electrodoméstico y el programa debe:

   • Verificar si el código existe.
   • Si existe, eliminarlo de la lista.
   • Guardar nuevamente el archivo sin ese registro.
   • Informar si la eliminación fue exitosa.
   • Si no existe, mostrar mensaje correspondiente.

--------------------------------------------------------------------------------

7) (PUNTO OBLIGATORIO)

   Generar un informe por cada marca existente en el archivo.
   Se debe crear un archivo con nombre:

   informe_[marca].txt

   Cada archivo debe contener:

   Marca: ________
   Total de productos vendidos: ___
   Total entregados: ___
   Total pendientes: ___
   Total cancelados: ___
   Producto más vendido: ___
   Recaudación total de la marca: ___

--------------------------------------------------------------------------------

8) Calcular la recaudación total general de la empresa considerando únicamente
   los productos con estado "entregado".

   Mostrar:
   Total general recaudado

--------------------------------------------------------------------------------

9) (PUNTO OBLIGATORIO)

   Implementar una función que permita modificar el estado de un producto 
   según su código.

   El usuario deberá ingresar:
   • Código del producto
   • Nuevo estado ("entregado", "pendiente" o "cancelado")

   El programa debe:
   • Verificar que el código exista.
   • Validar que el nuevo estado sea correcto.
   • Actualizar el registro en la lista.
   • Guardar nuevamente el archivo con la modificación.
   • Informar si la operación fue exitosa o no.

================================================================================
BUENAS PRÁCTICAS Y CLEAN CODE (OBLIGATORIO)
================================================================================

El examen será evaluado también por la calidad del código.

Se debe cumplir con:

• No repetir código innecesariamente.
• Evitar funciones con más de 1 o 2 responsabilidades.
• Usar nombres claros y descriptivos en variables y funciones.
• Escribir comentarios que expliquen bloques importantes de lógica.
• Evitar funciones excesivamente largas.
• Validar correctamente los datos ingresados por el usuario.
• Utilizar correctamente métodos de listas y cadenas.
• Mantener el código ordenado y legible.
• Separar lógica de negocio de la interacción con el usuario cuando sea posible.

El mal uso de estructuras, código repetido, funciones demasiado extensas,
mala organización o falta de claridad puede descontar puntos.

================================================================================
ENTREGA Y REPOSITORIO
================================================================================

El examen debe subirse a un repositorio siguiendo estas condiciones:

• Crear una carpeta llamada: parcial_2026 dentro de sus carpetas personales
• Dentro de ella colocar el archivo .py y generaciones de archivos
• La carpeta debe estar identificada con su nombre y apellido.
• Subir los cambios utilizando las técnicas recomendadas en el curso sobre 
  Git y GitHub.
• Realizar commits correctamente descriptivos.
• Verificar que el repositorio esté actualizado antes de finalizar.

================================================================================
CRITERIOS DE EVALUACIÓN - PARCIAL EMC 2026
================================================================================

Marcar con una X según corresponda.

| N° | CRITERIO                                   | NO CUMPLE | PARCIAL | CORRECTO |
|----|--------------------------------------------|-----------|---------|----------|
| 1  | Lectura correcta del archivo               | [   ]     | [   ]   | [   ]    |
| 2  | Manejo adecuado de excepciones             | [   ]     | [   ]   | [   ]    |
| 3  | Creación automática si no existe archivo   | [   ]     | [   ]   | [   ]    |
| 4  | Eliminación correcta por código            | [   ]     | [   ]   | [   ]    |
| 5  | Modificación correcta de estado            | [   ]     | [   ]   | [   ]    |
| 6  | Generación correcta de informes por marca  | [   ]     | [   ]   | [   ]    |
| 7  | Uso de algún método de ordenamiento        | [   ]     | [   ]   | [   ]    |
| 8  | Ordenamiento correctamente implementado    | [   ]     | [   ]   | [   ]    |
| 9  | Cálculos correctos (conteos y totales)     | [   ]     | [   ]   | [   ]    |
| 10 | Modularización adecuada                    | [   ]     | [   ]   | [   ]    |
| 11 | Funciones con responsabilidad clara        | [   ]     | [   ]   | [   ]    |
| 12 | No repetición de código innecesario        | [   ]     | [   ]   | [   ]    |
| 13 | Nombres claros en variables y funciones    | [   ]     | [   ]   | [   ]    |
| 14 | Validaciones correctas de datos            | [   ]     | [   ]   | [   ]    |
| 15 | Manejo correcto de archivos                | [   ]     | [   ]   | [   ]    |
| 16 | Uso correcto de with open() o close()      | [   ]     | [   ]   | [   ]    |
| 17 | Código ordenado y legible                  | [   ]     | [   ]   | [   ]    |
| 18 | Comentarios claros y útiles                | [   ]     | [   ]   | [   ]    |
| 19 | Uso correcto de métodos de listas          | [   ]     | [   ]   | [   ]    |
| 20 | Separación lógica / interacción            | [   ]     | [   ]   | [   ]    |
| 21 | Subida correcta al repositorio             | [   ]     | [   ]   | [   ]    |

================================================================================
OBSERVACIONES:
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________

PUNTAJE FINAL: ____________________
================================================================================
"""

"1) Implementar la función que lea el archivo electrodomesticos.txt y devuelva una lista con todos los registros."
def leerYlistar():
    try:
        # Intenta abrir el archivo en modo lectura
        archivo=open("electrodomesticos.txt","r", encoding="UTF-8")
    except FileNotFoundError:
        # Si no existe lo creamos
        archivo=open("electrodomesticos.txt","w", encoding="UTF-8")

        # Cargamos los 5 registros de ejemplo
        archivo.write("E001;2026-03-10;Heladera;Samsung;Maria Lopez;entregado;350000\n")
        archivo.write("E002;2026-03-15;Microondas;LG;Juan Perez;pendiente;120000\n")
        archivo.write("E003;2026-12-01;Lavarropas;Whirlpool;Ana Gomez;entregado;280000\n")
        archivo.write("E004;2026-04-05;Televisor;Sony;administrador;cancelado;450000\n")
        archivo.write("E005;2026-05-10;Heladera;LG;Carlos Ruiz;entregado;390000\n")

        archivo.close()
    
    registrosExistentes=[]

    archivo=open("electrodomesticos.txt","r", encoding="UTF-8")

    for linea in archivo:
        unidad=linea.strip().split(";")
        registrosExistentes.append(unidad)

    archivo.close()

    return registrosExistentes
    
    




    return

"2) Listar los electrodomesticos vendidos en un año y mes ingresado por usted. Los clientes llamados administrador no se listan. Mostrar: "
"   Producto - Cliente - Estado"
def vendidosEnAnioYMes(listaRegistros):
    anio=int(input("Ingrese el año a buscar: "))
    while anio<1950 or anio>2026:
        anio=int(input("Año inválido. Ingrese el año a buscar: "))
    mes=int(input("Ingrese el mes a buscar: "))
    while mes<=0 or mes>12:
        mes=int(input("Mes inválido. Ingrese el mes a buscar: "))
    
    anio_mes=f"{anio}-{mes:02d}"
    
    for producto in listaRegistros:
        if producto[1].startswith(anio_mes):
            if producto[4]!="administrador":
                print(f"{producto[2]} - {producto[4]} - {producto[5]}")

    return

"3) Solicitar una marca al usuario y mostrar cuántos productos de esa marca fueron vendidos en total."
def vendidosSegunMarca(listaRegistros, marca):
    contador=0

    for producto in listaRegistros:
        if producto[3]==marca:
            contador+=1

    return contador

"4) Mostrar todos los electrodomésticos que no hayan sido entregados (estado distinto a entregado). Mostrar: "
"   Código - Producto - Cliente - Estado"
def productosNoEntregados(listaRegistros):

    print("Los electrodomesticos que no han sido entregados hasta ahora=")
    for producto in listaRegistros:
        if producto[5]!="entregado":
            print(f"{producto[0]} - {producto[2]} - {producto[4]} - {producto[5]}")
    
    return

"5) Listar los 3 clientes con mayor cantidad de compras realizadas. Debe ordenarse de mayor a menor utilizando el método burbuja. Mostrar: "
"   Cliente - Cantidad de compras"
def listarClientes(listaRegistros):
    
    # Se contara las compras por cliente con un diccionario
    clientes = {}

    for producto in listaRegistros:
        cliente = producto[4]  # posición del cliente

        if cliente in clientes:
            clientes[cliente] += 1
        else:
            clientes[cliente] = 1

    # Lo pasamos a una lista para poder ordenar con el Método Burbuja
    listaClientes = list(clientes.items())
    
    # bubbleSort
    n = len(listaClientes)

    for i in range(n):
        for j in range(0, n-i-1):
            if listaClientes[j][1]<listaClientes[j+1][1]:
                listaClientes[j], listaClientes[j+1] = listaClientes[j+1], listaClientes[j]

    # Mostramos los 3 primeros
    print("Cliente - Cantidad de compras")
    for i in range(min(3, len(listaClientes))):
        print(f"{listaClientes[i][0]} - {listaClientes[i][1]}")
    
    return

"""
 6) Permitir eliminar un registro según su código. El usuario debe ingresar el código del electrodoméstico y el programa debe:
    • Verificar si el código existe.
    • Si existe, eliminarlo de la lista.
    • Guardar nuevamente el archivo sin ese registro.
    • Informar si la eliminación fue exitosa.
    • Si no existe, mostrar mensaje correspondiente."
"""
def eliminarRegistro(listaRegistros,codigo):
    encontrado=False

    for i in range(len(listaRegistros)):
        if listaRegistros[i][0]==codigo:
            listaRegistros.pop(i)
            encontrado=True
            print("Registro eliminado exitosamente.")
            break

        if not encontrado:
            print("No existe un regitro con ese código.")
            return
        
        with open("electrodomesticos.txt","w",encoding="UTF-8") as archivo:
            for producto in listaRegistros:
                linea = ";".join(producto) # Convertimos la lista en una linea de texto
                archivo.write(linea + "\n")

    return

"""
 7) Generar un informe por cada marca existente en el archivo. Se debe crear un archivo con nombre:

    informe_[marca].txt

    Cada archivo debe contener:

    Marca: ________
    Total de productos vendidos: ___
    Total entregados: ___
    Total pendientes: ___
    Total cancelados: ___
    Producto más vendido: ___
    Recaudación total de la marca: ___
"""
def informeMarcas(listaRegistros):
    # Obtener marcas sin repetir
    marcas = set()
    for producto in listaRegistros:
        marcas.add(producto[3])

    # Recorrer cada marca
    for marca in marcas:
        total_vendidos=0
        entregados=0
        pendientes=0
        cancelados=0
        recaudacion=0

        productos_marca={}

        # Recorrer todos los productos
        for producto in listaRegistros:
            if producto[3]==marca:
                total_vendidos+=1
                recaudacion+=int(producto[6])

                if producto[5]=="entregado":
                    entregados+=1
                elif producto[5]=="pendiente":
                    pendientes+=1
                elif producto[5]=="cancelado":
                    cancelados+=1

                nombre_producto=producto[2]

                # Contar cuántas veces se vendió cada producto dentro de una marca
                if nombre_producto in productos_marca:
                    productos_marca[nombre_producto]+=1
                else:
                    productos_marca[nombre_producto]=1

        # Obtener producto más vendido
        if productos_marca:
            mas_vendido = max(productos_marca, key=productos_marca.get)
        else:
            mas_vendido="Ninguno"

        # Crear archivo para la marca
        nombre_archivo=f"informe_{marca}.txt"

        with open(nombre_archivo, "w", encoding="UTF-8") as archivo:
            archivo.write(f"Marca: {marca}\n")
            archivo.write(f"Total de productos vendidos: {total_vendidos}\n")
            archivo.write(f"Total entregados: {entregados}\n")
            archivo.write(f"Total pendientes: {pendientes}\n")
            archivo.write(f"Total cancelados: {cancelados}\n")
            archivo.write(f"Producto más vendido: {mas_vendido}\n")
            archivo.write(f"Recaudación total de la marca: {recaudacion}\n")

    print("Informes generados correctamente.")
    return

" 8) Calcular la recaudación total general de la empresa considerando únicamente los productos con estado entregado. Mostrar: Total general recaudado"
def recaudacionTotal(listaRegistros):
    montoTotal=0

    for producto in listaRegistros:
        if producto[5]=="entregado":
            montoTotal+=int(producto[6])

    return montoTotal

"""
 9) Implementar una función que permita modificar el estado de un producto según su código.

   El usuario deberá ingresar:
   • Código del producto
   • Nuevo estado ("entregado", "pendiente" o "cancelado")

   El programa debe:
   • Verificar que el código exista.
   • Validar que el nuevo estado sea correcto.
   • Actualizar el registro en la lista.
   • Guardar nuevamente el archivo con la modificación.
   • Informar si la operación fue exitosa o no.
"""
def modificarEstado(listaRegistros,codigo_del_producto,nuevo_estado):
    encontrado = False

    # Buscamos el producto
    for producto in listaRegistros:
        if producto[0] == codigo_del_producto:
            producto[5] = nuevo_estado
            encontrado = True
            break

    if not encontrado:
        print("Código no encontrado.")
        return

    # Reescribir archivo completo
    with open("electrodomesticos.txt","w",encoding="UTF-8") as archivo:
        for producto in listaRegistros:
            linea=";".join(producto)
            archivo.write(linea+"\n")

    print("Estado modificado correctamente.")
    return


avanzar=True
while avanzar:
    print("--- Menú de Opciones ---")
    print("1. Devolver una lista con todos los Registros.")
    print("2. Listar los electrodomesticos vendidos en un año y mes ingresado por usted. Los clientes llamados administrador no se listan.")
    print("3. Mostrar cuantos productos vendidos hay según la marca ingresada por usted.")
    print("4. Mostrar todos los electrodomésticos que no hayan sido entregados.")
    print("5. Listar los 3 clientes con mayor cantidad de compras realizadas.")
    print("6. Eliminar un registro según su código.")
    print("7. Generar un informe por cada marca existente en el archivo.")
    print("8. Mostrar la recaudación total general de la empresa.")
    print("9. Modificar el estado de un producto según su código.")
    print("10. Salir.")
    accion=int(input("Ingrese la acción a realizar: "))
    while accion<=0 or accion>10:
        accion=int(input("Acción inválida. Ingrese nuevamente la acción a realizar: "))
    
    if accion==1:
        listaRegistros=leerYlistar()
    elif accion==2:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            vendidosEnAnioYMes(listaRegistros)
    elif accion==3:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            marca=str(input("Ingrese la marca para ver cuantos productos se vendieron: "))
            vendidos=vendidosSegunMarca(listaRegistros,marca)
            print(f"Se vendieron {vendidos} productos de la marca {marca}.")
    elif accion==4:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            productosNoEntregados(listaRegistros)
    elif accion==5:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            listarClientes(listaRegistros)
    elif accion==6:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            codigo=str(input("Ingrese el Código del Registro a eliminar: ")).upper()
            eliminarRegistro(listaRegistros,codigo)
    elif accion==7:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            informeMarcas(listaRegistros)
    elif accion==8:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            recaudacion=recaudacionTotal(listaRegistros)
            print(f"El monto total recaudado es de ${recaudacion}")
    elif accion==9:
        if len(listaRegistros)==0:
            print("No es posible acceder a esta opción todavía.")
        else:
            codigo_del_producto=str(input("Ingrese el Código del producto a modificar: ")).upper()
            nuevo_estado=str(input("Ingrese el estado que le quiere colocar al producto: ")).lower()
            while nuevo_estado!="entregado" or nuevo_estado!="pendiente" or nuevo_estado!="cancelado":
                nuevo_estado=str(input("Ingrese nuevamente el estado que le quiere colocar al producto: ")).lower()

            modificarEstado(listaRegistros,codigo_del_producto,nuevo_estado)
    elif accion==10:
        avanzar=False
