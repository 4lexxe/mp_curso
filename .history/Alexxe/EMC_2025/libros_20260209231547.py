def leer_prestamos():
  prestamos = []

  try:
    #intentar abrir y leer el fichero

    #La apertura 'a+' en Python abre un fichero para añadir (append) contenido al final y para leer (read) su contenido, sin borrar lo existente.
    with open("prestamos.txt", "a+", encoding="UTF-8") as archivo:

      #RECORRER EL FICHERO
      for linea in archivo:
        registro = linea.strip.split(";")
        #VERIFIICAR QUE TENGA 5 campos
        if len(registro) == 5:
          prestamos.append(registro)

  except:
    #si hay error (archivo no existe), creamos con datos de ejemplos

    with open("prestamos.txt", "w", encoding="UTF-8") as archivo:
      
      archivo.write("2025-09-01;Rayuela;Julio Cortázar;Ana Gutierrez;devuelto\n")

      archivo.write("2025-09-02;Cien años de soledad;Gabriel García\n")


    prestamos = leer_prestamos()

  return prestamos
#-----------------------------------------------------+

def listarPorFecha(prestamos, anio, mes):
  for prestamo in prestamos:
    
    if prestamo[]