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

def listarPorFecha(prestamos, anio, mes): #2003, 10
  for prestamo in prestamos:
    
    #2003-10 y administrador
    if prestamo[0].startswith(anio + "-" + mes) and prestamo[3] == "administrador":
      print(prestamo[1], "-", prestamo[3])
#-----------------------------------------------------+

def contarSolicitudesAutor(prestamos, autor_buscado):
  contador = 0
  
  for prestamo in prestamos:
    if prestamo[2] == autor_buscado:
      contador+=1

  print(f"CANTIDAD DE SOLICUTUDES DE AUTOR {autor_buscado}: ", contador);

#-----------------------------------------------------+

def listarNoDevueltos(prestamos):
  for prestamo in prestamos:
    if prestamo[4] != "devuelto":
      print("Usuario: ", prestamo[3], "| ESTADO: ", prestamo[4])

#-----------------------------------------------------+
def topTresUsuarios(prestamos):
  usuarios_contadores = []

  for prestamo in prestamos:
    usuario = prestamo[3]
    encontrado = False


    #VERIFICAR SI EL USUARIO YA SE ENCUENTRA EN LA LISTA DE USUARIOS TOP 3
    for i in range(len(usuarios_contadores)):
      usuarios_contadores[i][1] += 1
      encontrado = True
      break

    #SI NO EXISTE lo agregamos con contador 1
    if not encontrado:
      usuarios_contadores.append([usuario, 1])

    #ORDENAR POR BURBUJA
    for i in range(len(usuarios_contadores)):
      for j in range(i +  1, len(usuarios_contadores)):
        #si el siguiente tiene mas prestamos, intercambiamos posicion
        if usuarios_contadores[j][1] > usuarios_contadores[i][1]:
          usuarios_contadores[i], usuarios_contadores[j] = usuarios_contadores[j], usuarios_contadores[i]

    #MOSTRAR 3 primeros
    limite = min(3, len(usuarios_contadores))
    for i in range(limite):
      print(usuarios_contadores[i][0], "---", usuarios_contadores[i][1], "prestamos")

#-----------------------------------------------------+
def generarInformePorAutor(prestamos):
  lista_autores = []

  for prestamo in prestamos:
    if prestamo[2] not in lista_autores:
      lista_autores.append(prestamos[2])

  #PARA CADA AUTOR GENERAR INFORME
  for autor in lista_autores:
    #contadores = [total, devueltos, pendientes, retrasados]
    contadores = [0,0,0,0]

    libros_contador = []

    for prestamo in prestamos:
      if prestamo[2] == autor:
        contadores[0]+= 1

        #contar por estado
        if prestamo[4] == "devuelto":
          contadores[1] += 1
        elif prestamos[4] == "pendiente":
          contadores[2] += 1
        elif prestamo[4] == "retrasado":
          contadores[3] += 1

        #contar por libro
        libro = prestamo[1]
        libro_encontrado = None

        for item in libro
