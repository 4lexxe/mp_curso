numeros = [10, 15, 20, 25, 30, 35]

# Tradicional:
# pares = []
# for n in numeros:
#     if n % 2 == 0:
#         pares.append(n)

pares = [n for n in numeros if n % 2 == 0]
print(pares)


etiquetas = ["PAR" if n % 2 == 0 else "IMPAR" for n in numeros]
print(etiquetas)






registros = [['COD104', 'Cafe soluble 200g', 'Abarrotes', 6.45, 8], ['COD102', 'Aceite de Oliva 500ml', 'Abarrotes', 8.9, 12],['COD102', 'Aceite de Oliva 500ml', 'Abarrotes', 8.9, 12], ['COD105', 'Queso Gouda 250g', 'Lacteos', 4.1, 25], ['COD103', 'Pan Molde', 'Panaderia', 2.2, 30], ['COD101', 'Leche Entera 1L', 'Lacteos', 1.5, 50]]

def obtener_tipo_frecuente(registros_estacion):
  max_conteo = 0
  tipo_mas_frecuente = ""

  for registro in registros_estacion:
    conteo_actual= registros_estacion.count(registro)

    if conteo_actual > max_conteo:
      max_conteo = conteo_actual
      tipo_mas_frecuente = registro[2]
    
  print(tipo_mas_frecuente)
  return tipo_mas_frecuente


def obtener_tipo_frecuente2(registros_estacion):
  tipos = [registro[2] for registro in registros_estacion] #[]
  tipos_max_frecuente = max(set(tipos), key=tipos.count)
  return tipos_max_frecuente

print(obtener_tipo_frecuente2(registros))










vehiculos = ["auto", "camion", "auto", "moto", "camion", "auto"]

vehiculo = set(vehiculos)
print(vehiculo)
lista = list(vehiculo)
print(lista)


