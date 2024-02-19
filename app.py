"""Framewerk web.py"""
import web

#  Rutas de los controladores
urls = (
    '/login', 'mvc.controllers.index.Index',
    '/', 'mvc.controllers.bienvenida.Bienvenida'
)

app = web.application(urls, globals())

#  Punto de entrada
if __name__ == "__main__":
    app.run()
    