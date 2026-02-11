#leer el fichero y pasarlo a una lista
def leer_tareas():
  tareas = []

  #abrir el fichero en modo lectura
  archivo = open("tareas.txt", "r", encoding="UTF-8")

  #RECORRER cada linea del archivo
  for linea in archivo:
    tarea = linea.strip().split(";") #[1, 10-05-2024, 10:30", ]


