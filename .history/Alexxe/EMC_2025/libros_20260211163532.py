#===========================================================
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
          return lista_prestamos
  except:
    with open("prestamos.txt", "w", encoding="UTF-8") as archivo:
      archivo.write("2025-09-01;Rayuela;Julio Cortázar;Ana Gutierrez;devuelto\n")
      archivo.write("2025-09-02;Cien años de soledad;Gabriel García Marquez;administrador;pendiente\n")
    return leerPrestamos()
#===========================================================
def listarPorFecha(lista_prestamos): #2025-09-01
  anio = input("Ingrese la fecha") #2003
  mes = input("ingrese el mes") #10

  for prestamo in lista_prestamos:
    if prestamo[0].startswith(f"{anio}-{mes}") and prestamo[]: #"2003-10"

