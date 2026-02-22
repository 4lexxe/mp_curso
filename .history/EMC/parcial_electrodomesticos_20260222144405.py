"""
================================================================================
SOLUCIÓN DEL EXAMEN PARCIAL - ELECTRODOMÉSTICOS (EMC)
================================================================================

EXPLICACIÓN GENERAL:
--------------------
Este programa gestiona ventas de electrodomésticos en una tienda. Utiliza listas
para almacenar la información y funciones modulares para cada tarea específica.

ESTRUCTURA DE DATOS:
-------------------
- Cada venta es una lista: [fecha, producto, marca, cliente, estado]
- lista_ventas: lista de listas con todas las ventas
- clientes_lista: lista de listas [cliente, contador] para contar compras
- productos_lista: lista de listas [producto, contador] para contar productos

TÉCNICAS UTILIZADAS:
-------------------
1. Lectura y escritura de archivos de texto
2. Manejo de excepciones (try-except)
3. Búsqueda secuencial en listas
4. Uso de banderas (funciones booleanas)
5. Ordenamiento burbuja
6. Modularización con funciones auxiliares
7. Eliminación de registros y actualización de archivos
"""

#===========================================================
# CONSIGNA 1: Leer archivo ventas.txt
#===========================================================
def leerVentas():
  try:
    with open("ventas.txt", "r", encoding="UTF-8") as archivo:
      lista_ventas = []
      for linea in archivo:
        campos = linea.strip().split(";")
        if len(campos) == 5:
          venta = []
          for campo in campos:
            venta.append(campo.strip())
          lista_ventas.append(venta)
      return lista_ventas
  except:
    with open("ventas.txt", "w", encoding="UTF-8") as archivo:
      archivo.write("2025-01-15;Heladera;Samsung;Juan Perez;entregado\n")
      archivo.write("2025-01-20;Lavarropas;LG;Maria Lopez;pendiente\n")
      archivo.write("2025-02-10;Microondas;Whirlpool;administrador;entregado\n")
      archivo.write("2025-02-15;Heladera;Samsung;Carlos Gomez;entregado\n")
      archivo.write("2025-03-05;Televisor;Samsung;Ana Martinez;cancelado\n")
    return leerVentas()

#===========================================================
# CONSIGNA 2: Listar productos por fecha (año-mes)
#===========================================================
def listarPorFecha(lista_ventas):
  anio = input("Ingrese el año: ")
  mes = input("Ingrese el mes: ")

  print(f"\n--- Productos vendidos en {anio}-{mes} ---")
  for venta in lista_ventas:
    if venta[0].startswith(f"{anio}-{mes}") and venta[3] != "administrador":
      print(f"{venta[1]} - Cliente: {venta[3]}")

#===========================================================
# CONSIGNA 3: Contar ventas por marca
#===========================================================
def contarVentasPorMarca(lista_ventas):
  marca = input("Ingrese el nombre de la marca: ")
  contador = 0
  for venta in lista_ventas:
    if marca.lower() == venta[2].lower():
      contador += 1

  print(f"\nVentas de la marca {marca}: {contador}")

#===========================================================
# CONSIGNA 4: Listar productos no entregados
#===========================================================
def listarNoEntregados(lista_ventas):
  print("\n--- Productos no entregados ---")
  for venta in lista_ventas:
    if venta[4] != "entregado":
      print(f"Producto: {venta[1]} | Cliente: {venta[3]} | Estado: {venta[4]}")

#===========================================================
# CONSIGNA 5: Borrar venta según código
#===========================================================
def borrarVentaPorCodigo(lista_ventas):
  codigo = input("Ingrese el código del producto (ej: 2025-01-15HEL): ")
  
  # Buscar y eliminar el registro
  encontrado = False
  nueva_lista = []
  
  for venta in lista_ventas:
    # Generar código: fecha + primeras 3 letras del producto
    codigo_venta = venta[0] + venta[1][:3].upper()
    
    if codigo_venta != codigo:
      nueva_lista.append(venta)
    else:
      encontrado = True
      print(f"\nVenta eliminada: {venta[1]} - {venta[3]}")
  
  if not encontrado:
    print("\nCódigo no encontrado.")
    return lista_ventas
  
  # Actualizar el archivo
  with open("ventas.txt", "w", encoding="UTF-8") as archivo:
    for venta in nueva_lista:
      linea = ";".join(venta) + "\n"
      archivo.write(linea)
  
  print("Archivo actualizado correctamente.")
  return nueva_lista

#===========================================================
# CONSIGNA 6: Top 3 clientes con más compras
# FUNCIÓN PRINCIPAL
#===========================================================
def topTresClientes(lista_ventas):
  # Obtener clientes únicos con sus contadores
  clientes_lista = contarComprasPorCliente(lista_ventas)

  # Ordenar de mayor a menor
  clientes_ordenados = ordenarPorCantidad(clientes_lista)

  # Mostrar los 3 primeros
  mostrarTop3Clientes(clientes_ordenados)

#===========================================================
def contarComprasPorCliente(lista_ventas):
  clientes_lista = []  # [[NOMBRE, CANTIDAD]]

  for venta in lista_ventas:
    cliente = venta[3]

    # Verificar si el cliente ya existe
    if clienteYaExiste(clientes_lista, cliente):
      incrementarContadorCliente(clientes_lista, cliente)
    else:
      clientes_lista.append([cliente, 1])
    
  return clientes_lista

#===========================================================
def clienteYaExiste(clientes_lista, cliente):
  for item in clientes_lista:
    if item[0] == cliente:
      return True
  return False

#===========================================================
def incrementarContadorCliente(clientes_lista, cliente):
  for item in clientes_lista:
    if item[0] == cliente:
      item[1] += 1
      break

#===========================================================
# Ordenamiento burbuja - MAYOR A MENOR
#===========================================================
def ordenarPorCantidad(clientes_lista):
  for i in range(len(clientes_lista)):
    for j in range(i + 1, len(clientes_lista)):
      if clientes_lista[j][1] > clientes_lista[i][1]:
        clientes_lista[i], clientes_lista[j] = clientes_lista[j], clientes_lista[i]

  return clientes_lista

#===========================================================
def mostrarTop3Clientes(clientes_ordenados):
  print("\n--- Top 3 clientes con más compras ---")
  if len(clientes_ordenados) < 3:
    print("Clientes insuficientes")
    return
    
  for i in range(3):
    print(f"{i+1}. {clientes_ordenados[i][0]} - {clientes_ordenados[i][1]} compras")

#===========================================================
# CONSIGNA 7 (OBLIGATORIO): Generar informe por marca
# FUNCIÓN PRINCIPAL
#===========================================================
def generarInformePorMarca(lista_ventas):
  # Generar un informe por cada marca
  marcas = obtenerMarcasUnicas(lista_ventas)

  for marca in marcas:
    ventas_marca = filtrarVentasPorMarca(lista_ventas, marca)
    
    # Total de productos vendidos
    total = len(ventas_marca)
    
    # Total por estado
    entregados, pendientes, cancelados = contarPorEstado(ventas_marca)
    
    # Producto más vendido
    productos_lista = contarProductosPorMarca(ventas_marca)
    producto_top = obtenerProductoMasVendido(productos_lista)
    
    # Escribir informe
    escribirInforme(marca, total, entregados, pendientes, cancelados, producto_top)

#===========================================================
def obtenerMarcasUnicas(lista_ventas):
  marcas = []
  for venta in lista_ventas:
    if venta[2] not in marcas:
      marcas.append(venta[2])
  
  return marcas

#===========================================================
def filtrarVentasPorMarca(lista_ventas, marca):
  ventas_marca = []
  for venta in lista_ventas:
    if venta[2] == marca:
      ventas_marca.append(venta)
  return ventas_marca

#===========================================================
def contarPorEstado(ventas_marca):
  entregados = 0
  pendientes = 0
  cancelados = 0

  for venta in ventas_marca:
    if venta[4] == "entregado":
      entregados += 1
    elif venta[4] == "pendiente":
      pendientes += 1
    elif venta[4] == "cancelado":
      cancelados += 1

  return entregados, pendientes, cancelados

#===========================================================
def contarProductosPorMarca(ventas_marca):
  productos_lista = []

  for venta in ventas_marca:
    producto = venta[1]

    if productoYaExiste(productos_lista, producto):
      incrementarContadorProducto(productos_lista, producto)
    else:
      productos_lista.append([producto, 1])
    
  return productos_lista

#===========================================================
def productoYaExiste(productos_lista, producto):
  for item in productos_lista:
    if item[0] == producto:
      return True
  return False

#===========================================================
def incrementarContadorProducto(productos_lista, producto):
  for item in productos_lista:
    if item[0] == producto:
      item[1] += 1
      break

#===========================================================
def obtenerProductoMasVendido(productos_lista):
  if len(productos_lista) == 0:
    return "Ninguno"
    
  producto_mayor = productos_lista[0][0]
  cantidad_max = productos_lista[0][1]

  for item in productos_lista:
    if item[1] > cantidad_max:
      cantidad_max = item[1]
      producto_mayor = item[0]

  return producto_mayor

#===========================================================
def escribirInforme(marca, total, entregados, pendientes, cancelados, producto_top):
  nombre_archivo = f"informe_{marca}.txt"
  with open(nombre_archivo, "w", encoding="UTF-8") as archivo:
    archivo.write(f"Marca: {marca}\n")
    archivo.write(f"Total de productos vendidos: {total}\n")
    archivo.write(f"Total de productos entregados: {entregados}\n")
    archivo.write(f"Total de productos pendientes: {pendientes}\n")
    archivo.write(f"Total de productos cancelados: {cancelados}\n")
    archivo.write(f"Producto más vendido: {producto_top}\n")
  
  print(f"Informe generado: {nombre_archivo}")

#==================PROGRAMA PRINCIPAL========================

print("=" * 60)
print("SISTEMA DE GESTIÓN DE VENTAS - ELECTRODOMÉSTICOS")
print("=" * 60)

# Cargar datos
lista = leerVentas()

# Ejecutar consignas
print("\n[CONSIGNA 2]")
listarPorFecha(lista)

print("\n[CONSIGNA 3]")
contarVentasPorMarca(lista)

print("\n[CONSIGNA 4]")
listarNoEntregados(lista)

print("\n[CONSIGNA 5]")
lista = borrarVentaPorCodigo(lista)

print("\n[CONSIGNA 6]")
topTresClientes(lista)

print("\n[CONSIGNA 7 - OBLIGATORIO]")
generarInformePorMarca(lista)

print("\n" + "=" * 60)
print("PROGRAMA FINALIZADO")
print("=" * 60)
