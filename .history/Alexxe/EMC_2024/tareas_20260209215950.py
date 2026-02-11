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
  

#--------------------------------------------------------------
