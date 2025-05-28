from src.modelo.modelo import Estudiante, Asignatura

class EstudianteManager:
    def __init__(self, session):
        self.session = session

    def crear_estudiante(self, nombre):
        estudiante = Estudiante(nombre=nombre)
        self.session.add(estudiante)
        self.session.commit()
        return estudiante

    def leer_estudiante(self, estudiante_id):
        return self.session.query(Estudiante).filter_by(id=estudiante_id).first()

    def actualizar_estudiante(self, estudiante_id, nuevo_nombre):
        estudiante = self.leer_estudiante(estudiante_id)
        if estudiante:
            estudiante.nombre = nuevo_nombre
            self.session.commit()
        return estudiante

    def eliminar_estudiante(self, estudiante_id):
        estudiante = self.leer_estudiante(estudiante_id)
        if estudiante:
            self.session.delete(estudiante)
            self.session.commit()
        return estudiante

    def agregar_asignatura(self, estudiante_id, asignatura_nombre):
        estudiante = self.leer_estudiante(estudiante_id)
        if estudiante:
            asignatura = Asignatura(nombre=asignatura_nombre, estudiante=estudiante)
            self.session.add(asignatura)
            self.session.commit()
            return asignatura
        return None

    def leer_asignaturas(self, estudiante_id):
        estudiante = self.leer_estudiante(estudiante_id)
        return estudiante.asignaturas if estudiante else None
