def leer_prestamos():
  prestamos = []

#La apertura 'a+' en Python abre un fichero para añadir (append) contenido al final y para leer (read) su contenido, sin borrar lo existente.
  with open("prestamos.txt", "a+", encoding="UTF-8") as archivo:
    archivo.seek(0)
    
    #RECORRER EL FICHERO

    for linea in archivo:
      registro = linea.strip.split(";")
      #VERIFIICAR QUE TENGA 5 campos
      if len(registro) == 5:
        prestamos.append(registro)
        
  return prestamos
#-----------------------------------------------------+



