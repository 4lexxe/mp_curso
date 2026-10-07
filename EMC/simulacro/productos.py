def generar_productos():

    lineas = [
        "P001;Mouse Logitech;perifericos;18000;12\n",
        "P002;Teclado Redragon;perifericos;32000;8\n",
        "P003;SSD Kingston;hardware;45000;5\n",
        "P004;Memoria RAM 16GB;hardware;38000;10\n",
        "P005;Pendrive 64GB;almacenamiento;12000;15\n"
    ]

    with open("productos.txt", "w", encoding="utf-8") as fichero:

        for linea in lineas:
            fichero.write(linea)



def crear_lista_productos(fichero):

    lista_productos = []

    for linea in fichero:

        elementos = linea.strip().split(";")

        lista_productos.append(elementos)

    return lista_productos


def leer_archivo_productos():

    try:

        with open("productos.txt", "r", encoding="utf-8") as fichero:

            return crear_lista_productos(fichero)

    except FileNotFoundError:

        generar_productos()

        return leer_archivo_productos()
#2------------------------------
def lista_productos_categoria(productos, categoria):
  lista = []

  for producto in productos:
    if producto[2] == categoria and int(producto[4]) > 0:
      lista.append([producto[0], producto[1], producto[3], producto[4]])
      #                 codigo       nomnbre      precio       stock
  return lista

#3---------------------------------
def mostrar_tres_menores(lista):
  ordenados = sorted(lista, key=lambda producto:int(producto[2]))
#  3_menores = []
  #for i in range(3):
   # 3_menores.append(ordenados[i])

  #return 3_menores
  return ordenados[0:3]


#4------------------------------------
def borrar_producto_por_codigo(productos, codigo):

    with open("productos.txt", "w", encoding="utf-8") as fichero:

        for producto in productos:

            if producto[0] != codigo:

                fichero.write(";".join(producto) + "\n")

#5---------------------------------

def crear_informe_categoria(productos):
  categorias = []
  for producto in productos:
    categoria = producto[2]
    if categoria not in categorias:
      categorias.append(categoria)
  
  for categoria in categorias:
    productos_categoria = []

    for producto in productos:
      if producto[2] == categoria:
        productos_categoria.append(producto)

    #contadores
    con_stock = 0
    sin_stock = 0
    stock_total = 0
    total_productos = len(productos_categoria)
    print(productos_categoria)
    menor = productos_categoria[0]
    mayor = productos_categoria[0]


    for producto in productos_categoria:
      stock = int(producto[4])
      precio = int(producto[3])

      if stock > 0:
        con_stock +=1
      else:
        sin_stock +=1

      stock_total+= stock

      if precio < int(menor[3]):
        menor = producto
      
      if precio > int(mayor[3]):
        mayor = producto

    #crear informe
    nombre = "informe_" + categoria +  ".txt"

    with open(nombre, "w", encoding="utf-8") as fichero:

      fichero.write("Categoria: " + categoria + "\n")
      fichero.write("Total de productos registrados: " + str(total_productos) + "\n")
      fichero.write("Productos con stock: " + str(con_stock) + "\n")
      fichero.write("Productos sin stock: " + str(sin_stock) + "\n")
      fichero.write("Stock total: " + str(stock_total) + "\n")
      fichero.write("Producto con menor precio: " + menor[1] + "\n")
      fichero.write("Producto con mayor precio:"+ mayor[1] + "\n")

# Consigna 1

productos = leer_archivo_productos()


# Consigna 2

categoria = input("Ingrese categoria: ")

filtrados = lista_productos_categoria(productos, categoria)

print("Productos filtrados:", filtrados)


# Consigna 3

print("Tres productos con menor precio:")

print(mostrar_tres_menores(filtrados))


# Consigna 4



# Actualizar lista despues del borrado

productos = leer_archivo_productos()


# Consigna 5

crear_informe_categoria(productos)

print("Informes generados correctamente.")