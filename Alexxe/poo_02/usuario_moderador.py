from Usuario import Usuario

class UsuarioModerador(Usuario):

  def mensaje_rol(self):
    return "Este es un usuario moderador"