#--------------------------------------------------------------
#leer el fichero y pasarlo a una lista
def leer_tareas():
  tareas = []

  #abrir el fichero en modo lectura
  archivo = open("tareas.txt", "r", encoding="UTF-8")

  #RECORRER cada linea del archivo
  for linea in archivo:
    tarea = linea.strip().split(";") #["1", "10-05-2024, 10:30", "descrip", "registd"]
    
    #verificar los campos para evitar lista fuera de rango
    if len(tarea) == 4:
      #limpiar espacios de cada campo
      tarea_limpia = []
      for campo in tarea:
        tarea_limpia.append(campo.strip())
      tareas.append(tarea_limpia)

  archivo.close()
  return tareas

#--------------------------------------------------------------
#crear el id
def obtener_ultimo_id():
  #obtener el ultimo id numero
  tareas = leer_tareas()

  #si no hay tareas, comenzamos con 0
  if len(tareas) == 0:
    return 0
  
  #buscar el id mas alto
  for tarea in tareas:
    ultimo = 0
    #comparar el id actual con el ultimo encotrado
    if int(tarea[0]) > ultimo:
      ultimo = int(tarea[0])
  
  return ultimo
#--------------------------------------------------------------
def agregar_tarea():
  fecha = input("Ingrese la fecha (dd-mm-yyyy): ").strip()
  
  #validar formato fecha
  while not validar_fecha(fecha):
    print("Formato de fecha no valido")
    fecha = input("Ingrese la fecha valido (dd-mm-yyyy): ").strip()


  #solicitar y validar la hora
  hora = input("ingrese la hora hh:mm").strip()
  while not validar_hora(hora):
    print("Formato de hora no valido")
    hora = input("ingrese la hora valido hh:mm").strip()


  #solicitar la descripcion y validar
  descripcion = input("Ingrese la descripcion: ")
  while not validar_descripcion(descripcion):
    print("la descripcion no puede estar vacia.")
    descripcion = input("Ingrese la descripcion no vacía: ")
    
  #GENERAR ID
  nuevo_id = obtener_ultimo_id() + 1
  guardar_tarea(nuevo_id, fecha, hora, descripcion)
#--------------------------------------------------------------
def validar_fecha(fecha): #09-10-2003
  if len(fecha) != 10 or fecha[2] != "-" or fecha[5] != "-":
    return False;

  dia = int(fecha[0:2])
  mes = int(fecha[3:5])
  anio = int(fecha[6:10])

  if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 1900:
    return False
  
  return True
#--------------------------------------------------------------
def validar_hora(hora):
  if len(hora) != 5 or hora[2] != ":":
    return False;

  horas = int(hora[0:2])
  minutos = int(hora[3:5])

  if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
    return False
  
  return True
#--------------------------------------------------------------
def validar_descripcion(descripcion):
  if len(descripcion) == 0:
    return False
  
  return True
#--------------------------------------------------------------
#guardar TAREAS
def guardar_tarea(id, fecha, hora, descripcion):
  #abrir en modo append(a) para agregar al final
  archivo = open("tareas.txt", "a", encoding="UTF-8")
  archivo.write(str(id) + "; " + fecha + ", " + hora + "; " + descripcion + "; Registrada\n")
  archivo.close()
#--------------------------------------------------------------

def buscar_tarea():
  id_buscado = input("Ingrese el id de la tarea: ")
  tareas = leer_tareas()

  for tarea in tareas:
    if tarea[0] == id_buscado:
      print("ID: ", tarea[0])
      print("FECHA Y HORA: ", tarea[1])
      print("DESCRIPCION: ", tarea[2])
      print("ESTADO: ", tarea[3])
      return
  
  print("TAREA NO ENCONTRADA")

agregar_tarea()
buscar_tarea()


