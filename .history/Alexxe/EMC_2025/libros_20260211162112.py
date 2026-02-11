#====================================
def leerPrestamos():
  try:
    with open("prestamos.txt", "r", encoding="UTF-8") as archivo:
      lista_prestamos = []
      for linea in archivo:
        campos = linea.strip()
  except:

#====================================