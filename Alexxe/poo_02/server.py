from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from Usuario import Usuario
from usuario_admin import UsuarioAdmin
from usuario_moderador import UsuarioModerador

class Server(BaseHTTPRequestHandler):
  
  def do_GET(self):
    if self.path == "/":
      with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

  def do_POST(self):
    length = int(self.headers["Content-length"])

    data = parse_qs(self.rfile.read(length).decode())

    nombre = data["nombre"][0]
    email = data["email"][0]

    if email.endswith("@admin.com"):
      usuario = UsuarioAdmin(nombre, email)
    elif email.endswith("@mod.com"):
      usuario = UsuarioModerador(nombre, email)
    else:
      usuario = Usuario(nombre, email)

    self.send_response(200)
    self.send_header("Content-type", "text/html; charset=utf-8")
    self.end_headers()

    if usuario.es_valido():
      self.wfile.write(usuario.mensaje_rol().encode("utf-8"))
    else:
      self.wfile.write("datos incorrectos".encode("utf-8"))


HTTPServer(("localhost", 8000), Server).serve_forever()