from src.modelo.declarative_base import Session, Base, engine
from src.logica.EstudianteManager import ArticuloManager

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Configurar una nueva sesión para cada prueba
session = Session()
manager = ArticuloManager(session)

# crear articulos
articulo1=manager.crear_articulo("El Guille")
articulo2=manager.crear_articulo("El blog investigación")

# crea comentarios
manager.agregar_comentario(articulo1.id, "Es para .net")
manager.agregar_comentario(articulo2.id, "Util para la tesis")
manager.agregar_comentario(articulo2.id, "Tiene los pasos para publicar un artículo")
