class Persona:
  #2
  def __init__(self, nombre):
    self.nombre = nombre

  def saludar(self):
    print("Hola me llamo", self.nombre)