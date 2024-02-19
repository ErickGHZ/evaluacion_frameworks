import web
"""Importamos la clase ModeloProductos del modelo modelo_productos.py"""
from mvc.models.modelo_bienvenida import ModeloBienvenida

render = web.template.render('mvc/views/', base='layout')

m_index = ModeloBienvenida() # Se crea objeto de la clase Modelo Index

class Bienvenida:
    def GET(self):
        try:
            return render.bienvenida()
        except Exception as e:
            print(f"Error 101 - productos {e.args}")
            return "Ups algo salió mal"

    def POST(self):
        try:
            # Lógica para manejar la solicitud POST
            return render.bienvenida()
        except Exception as e:
            print(f"Error 102 - productos {e.args}")
            return "Ups algo salió mal"

