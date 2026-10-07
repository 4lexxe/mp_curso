def generar_fichero():
  lista = [
    "2025-09-01;Rayuela;Julio Cortázar;Ana Gutierrez;devuelto\n",
    "2025-09-02;Cien soledad;Gabriel Marquez;administrador;pendiente\n",
    "2025-09-03;Rayuela;Julio Cortázar;Marco Lopez;retrasado\n",
    "2025-09-03;El Extranjero;Albert Camus;Carlos Gómez;retrasado\n"
  ]

  with open("prestamos.txt", "w", encoding="UTF-8") as fichero:
    fichero.writelines(lista)
#-----------------------------------------
def crear_lista(fichero):
  registros = []
  for linea in fichero:
    elementos = linea.strip().split(";") #
    #["2025-09-01", "Rayuela", "Julio Cortázar", "Ana", "devuelto"],
    registros.append(elementos)
  
  return registros
#----------------------------------------
def leer_prestamos():
  try:
    with open("prestamos.txt", "r", encoding="UTF-8") as fichero:
      return crear_lista(fichero)
  except FileNotFoundError:
    generar_fichero()
    return leer_prestamos()
#-------------------------------------------
def filtrar_libros(registros, anio, mes):
  libros = []
  for registro in registros:
    #["2025-09-01", "Rayuela", "Julio Cortázar", "Ana", "devuelto"],
    fecha = registro[0].split("-") #[2025, 09, 01]

    if fecha[0] == anio and fecha[1] == mes and registro[2] != "administrador":
      libros.append([fecha, registro[1]])

    #libros = [[2026-09], rayuela]]
  return libros
#-------------------------------------------

def contar_solicitudes(registros, libros, autor):
  contador = 0
  for registro in registros:
    if registro[2] == autor and libros[1]:
      contador+=1
  
  return contador
#-------------------------------------------

def listar_libros_no_devueltos(registros):
  libros_no_devueltos = []

  for registro in registros:
    if registro[4] != "devuelto":
      libros_no_devueltos.append([registro[1], registro[3], registro[4]])
      #[["pinocho", "Perez", "pendiente"]]
  return libros_no_devueltos
#-------------------------------------------

def listar_3_usuarios_mas_solicitudes(registros):
  usuarios = []

  for registro in registros:
    usuarios.append(registro[3])
    #["peep", "juan", pepe, pepe, "maria", pepe]
  cantidades = []

  for usuario in usuarios:
    cantidades.append([usuario, usuarios.count(usuario)])
    # [[pepe, 4] , [maria, 3], [juan, 5]]

  #sorted y lambda
  ordenados = sorted(cantidades, key=lambda posicion:posicion[1], reverse=True)
  #mayor a menor
  return  ordenados[0:3]

#-------------------------------------------

def generar_informes_por_autor(registros):
   autores= []
   for registro in registros:
       autor= registro[2]
       if autor not in autores:
           autores.append(autor)
   
   for autor in autores:
       total_libros_solicitados=0
       total_libros_devueltos=0
       total_libros_pendientes=0
       total_libros_retrasados=0 
       
       for registro in registros: 
           if registro[2]== autor:
               total_libros_solicitados+=1
               if registro[4]== "devuelto":
                  total_libros_devueltos+=1
               elif registro[4]== "pendiente": 
                  total_libros_pendientes+=1
               elif registro[4]== "retrasado":
                  total_libros_retrasados+=1   
                     
       nombre_archivo= "informe_" + autor + ".txt"

       with open (nombre_archivo, "w") as archivo:
           archivo.write("Autor: " + str(autor) +"\n")
           archivo.write("Total de libros solicitados: " + str(total_libros_solicitados) +"\n")
           archivo.write("Total de libros devueltos: " + str(total_libros_devueltos) +"\n")
           archivo.write("Total de libros pendientes: " + str(total_libros_pendientes) +"\n")
           archivo.write("Total de libros retrasados " + str(total_libros_retrasados) +"\n")


registros = leer_prestamos()

anio = input("Año: ")
mes = input("Mes: ")

print(filtrar_libros(registros, anio, mes))
print(contar_solicitudes(registros, "Rayuela", "Julio Cortázar"))
print(listar_libros_no_devueltos(registros))
print(listar_3_usuarios_mas_solicitudes(registros))

generar_informes_por_autor(registros)



