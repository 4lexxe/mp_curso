# fecha_hora;placa;tipo_vehiculo;estacion;pago_confirmado
def generar_ficheros():
  lineas = ["2026-11-05 08:30;AB123CD;auto;Peaje_Norte;si\n",
            "2026-11-05 08:45;OFICIAL_01;auto;Peaje_Norte;si\n",
            "2026-11-05 09:12;XY987ZT;camion;Peaje_Norte;no\n",
            "2026-11-05 09:30;JK456LM;moto;Peaje_Sur;si\n",
            "2026-11-05 10:00;AA111BB;camion;Peaje_Norte;si\n"
            "2026-11-05 10:00;OFICIAL_AABB;camion;Peaje_Norte;si\n"]
  
  with open("transitos.txt", "w") as fichero:
    for linea in lineas:
      fichero.write(linea)

#-------------------------------------------------------------
def crear_lista_fichero(fichero):
  registros= []
  for linea in fichero:
    elementos = linea.strip().split(";") #elementos = []
    registros.append(elementos)
  
  print(registros)
  return registros
#-------------------------------------------------------------
def leer_transitos():
  try:
    with open("transitos.txt", "r") as fichero:
      return crear_lista_fichero(fichero)
  except(FileNotFoundError, Exception):
    generar_ficheros()
    return leer_transitos()
#--------------------------------------------------------------

registros = leer_transitos()

#------------------------------------------------------------
estacion = input("Ingrese la estacion a buscar: ")


def filtrar_transito_comercial(registros, estacion):
  camiones = []
  for registro in registros:
    if registro[2] == "camion" and not registro[1].startswith("OFICIAL_"):
      camiones.append([registro[1], registro[2]])
  print(camiones)
  return camiones


filtrar_transito_comercial(registros, estacion)
#------------------------------------------------------------


def enlistar_evasiones_pagos(registros):
  evasiones = []
  for registro in registros:
    if registro[4] == "no":
      evasiones.append([registro[1], registro[0], registro[3]])
  print(evasiones)
  return evasiones

#------------------------------------------------------------

enlistar_evasiones_pagos(registros)

#------------------------------------------------------------

def generar_informes_por_estacion(registros):
  estaciones_unicas = obtener_estaciones_unicas(registros)
  for estacion in estaciones_unicas:
    total_vehiculos = 0
    pagos_confirmados = 0
    evadidos = 0
    registros_estacion=[]

    for registro in registros:
      if registro[3] == estacion:
        total_vehiculos+=1
        registros_estacion.append(registro)
        if registro[4] == "si":
          pagos_confirmados+=1
        elif registro[4] == "no":
          evadidos+= 1

    tipo_frencuente = obtener_tipo_frecuente(registros_estacion)

    nombre_archivo="informe_"+ estacion + ".txt"
    with open(nombre_archivo, "w") as archivo:
      archivo.write("Estacion:"+ str(estacion) +"\n")
      archivo.write("Total de vehículos registrados: "+ str(total_vehiculos) +"\n")
      archivo.write("Total de pagos confirmados: "+ str(pagos_confirmados)+ "\n")
      archivo.write("Total de evadidos (sin pago): "+ str(evadidos)+"\n")
      archivo.write("Tipo de vehículo más frecuente: "+  str(tipo_frencuente) + "\n")

#------------------------------------------------------------
def obtener_estaciones_unicas(registros):
  estaciones_unicas = []
  for registro in registros:
    estacion = registro[3]
    if estacion not in estaciones_unicas:
      estaciones_unicas.append(estacion)
  return estaciones_unicas

#------------------------------------------------------------
def obtener_tipo_frecuente(registros_estacion):
  max_conteo = 0
  tipo_mas_frecuente = ""

  for registro in registros_estacion:
    conteo_actual= registros_estacion.count(registro)

    if conteo_actual > max_conteo:
      max_conteo = conteo_actual
      tipo_mas_frecuente = registro[2]
    
  print(tipo_mas_frecuente)
  return tipo_mas_frecuente
#------------------------------------------------------------

generar_informes_por_estacion(registros)

#------------------------------------------------------------