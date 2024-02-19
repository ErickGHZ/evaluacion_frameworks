import web

class ModeloIndex:
    def __init__(self):
        pass

    def iniciarSesion(self, usuario, contrasena):
        # Aquí maneja la lógica de inicio de sesión
        if usuario == "admin" and contrasena == "1234":
            # Crea una cookie con el nombre de usuario
            web.set_cookie("username", "Erick")
            return True
        else:
            return False
