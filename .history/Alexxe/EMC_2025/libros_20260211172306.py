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
    if prestamo[0].startswith(f"{anio}-{mes}") and prestamo[3] != "administrador": #"2003-10"
      print(prestamo[1], "-", prestamo[3])
#===========================================================
def contarSolicitudesAutor(lista_prestamos):
  autor = input("Ingrese el nombre del autor: ")
  contador = 0
  for prestamo in lista_prestamos:
    if autor == prestamo[2]:
      contador+=1

  print(f"SOlicitudes del {autor} es de: {contador}")
#===========================================================
def listarNoDevueltos(lista_prestamos):
  for prestamo in lista_prestamos:
    if prestamo[4] != "devuelto":
      print(f"Usuario: {prestamo[3]} | Estado {prestamo[4]}")

#===========================================================
#Listar los 3 usuarios con más libros solicitados
#FUNCION PRINCIPAL
def topTresUsuarios(lista_prestamos):
  #OBTENER USUARIOS UNICOS CON SUS CONTADORES
  usuarios_lista = contarPrestamosPorUsuario(lista_prestamos)

  #ORDENAMOS MAYOR A MENOR
  usuarios_ordenados = ordenarPorCantidad(usuarios_lista)

  #MOSTRAR LOS 3 primeros
  mostrarTop3(usuarios_ordenados)

#===========================================================

def contarPrestamosPorUsuario(lista_prestamos):
  usuarios_lista = [] #[[NOMBRE, CANTIDAD]]

  for prestamo in lista_prestamos:
    usuario = prestamo[3] #usuario = ANA MARIA

    #VERIFICAR SI EL USUARIO EXISTE EN LA LISTA usuario_lista = []
    if usuarioYaExiste(usuarios_lista, usuario):
      incrementarContador(usuarios_lista, usuarios_lista)
    else:
      usuarios_lista.append([usuario, 1]) #[usuario, 1]
    
  return usuarios_lista

#===========================================================

def usuarioYaExiste(usuarios_lista, usuario):
  for item in usuarios_lista:
    if item[0] == usuario:
      return True
  return False
#===========================================================

def incrementarContador(usuarios_lista, usuario):
  for item in usuarios_lista:
    if item[0] == usuario:
      item[1] += 1
      break
#===========================================================
#MAYOR A MENOR
def ordenarPorCantidad(usuarios_lista):
  
#===========================================================

#===========================================================
