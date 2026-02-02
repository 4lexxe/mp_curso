class Usuario:

  #CONSTRUCTOR
  def __init__(self, nombre, email):
    self._nombre = nombre
    self._email = email

  def es_valido(self):
    return self._nombre != "" and "@" in self._email

  def mensaje_rol(self):
    return self._nombre