from Usuario import Usuario

class UsuarioAdmin(Usuario):

  def mensaje_rol(self):
    return "Este es un usuario administrador"