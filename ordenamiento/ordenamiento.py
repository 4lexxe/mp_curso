# 1. Crear el archivo de productos con datos de prueba
def generar_fichero_productos():
    lineas = [
        "COD101;Leche Entera 1L;Lacteos;1.50;50\n",
        "COD102;Aceite de Oliva 500ml;Abarrotes;8.90;12\n",
        "COD103;Pan Molde;Panaderia;2.20;30\n",
        "COD104;Cafe soluble 200g;Abarrotes;6.45;8\n",
        "COD105;Queso Gouda 250g;Lacteos;4.10;25\n",
    ]
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)


  # 2. Leer el fichero y formatear los datos (convertir precio a float)
def leer_productos():
    productos = []
    try:
        with open("productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(";")
                # Convertimos el precio (indice 3) a flotante y el stock (indice 4) a entero
                codigo = partes[0]
                nombre = partes[1]
                categoria = partes[2]
                precio = float(partes[3])
                stock = int(partes[4])

                productos.append([codigo, nombre, categoria, precio, stock])
    except FileNotFoundError:
        generar_fichero_productos()
        return leer_productos()

    return productos


# ------------------------------------------------------------
# FUNCIONES DE ORDENAMIENTO
# ------------------------------------------------------------
#PRODUCTOS = [ [ ] ]
def ordenar_por_mayor_menor(productos):
  return sorted(productos, key=lambda producto: producto[4], reverse=True)

def ordenar_por_menor_mayor(productos):
  return sorted(productos, key=lambda producto: producto[4], reverse=False)


productos = leer_productos()

print(ordenar_por_mayor_menor(productos))
print("\n"+"---------------------------------")
print(ordenar_por_menor_mayor(productos))
print("\n"+"---------------------------------")


