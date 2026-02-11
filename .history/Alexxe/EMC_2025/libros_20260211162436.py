#====================================
def leerPrestamos():
  try:
    with open("prestamos.txt", "r", encoding="UTF-8") as archivo:
      lista_prestamos = []
      for linea in archivo:
        campos = linea.strip().split(";")
        if len(campo) == 5:
          prestamo = []
          for campo in campos:
            prestamo.append(campo.strip())
          lista_prestamos.append(prestamo)
  except:
    with open("prestamos.txt", "w")

#====================================