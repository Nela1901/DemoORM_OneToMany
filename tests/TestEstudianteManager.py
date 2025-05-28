import unittest
from src.modelo.declarative_base import Session, Base, engine
from src.logica.EstudianteManager import EstudianteManager

class TestEstudianteManager(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        self.session = Session()
        self.manager = EstudianteManager(self.session)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_crear_estudiante(self):
        estudiante = self.manager.crear_estudiante("Juan Pérez")
        self.assertIsNotNone(estudiante.id)
        self.assertEqual(estudiante.nombre, "Juan Pérez")

    def test_leer_estudiante(self):
        estudiante = self.manager.crear_estudiante("Ana López")
        estudiante_leido = self.manager.leer_estudiante(estudiante.id)
        self.assertEqual(estudiante_leido.nombre, "Ana López")

    def test_actualizar_estudiante(self):
        estudiante = self.manager.crear_estudiante("Nombre Original")
        actualizado = self.manager.actualizar_estudiante(estudiante.id, "Nombre Actualizado")
        self.assertEqual(actualizado.nombre, "Nombre Actualizado")

    def test_eliminar_estudiante(self):
        estudiante = self.manager.crear_estudiante("Estudiante a Eliminar")
        eliminado = self.manager.eliminar_estudiante(estudiante.id)
        self.assertIsNone(self.manager.leer_estudiante(eliminado.id))

    def test_agregar_asignatura(self):
        estudiante = self.manager.crear_estudiante("Estudiante con Asignatura")
        asignatura = self.manager.agregar_asignatura(estudiante.id, "Matemáticas")
        self.assertEqual(asignatura.nombre, "Matemáticas")
        self.assertEqual(asignatura.estudiante_id, estudiante.id)

    def test_leer_asignaturas(self):
        estudiante = self.manager.crear_estudiante("Estudiante con varias Asignaturas")
        self.manager.agregar_asignatura(estudiante.id, "Física")
        self.manager.agregar_asignatura(estudiante.id, "Química")
        asignaturas = self.manager.leer_asignaturas(estudiante.id)
        self.assertEqual(len(asignaturas), 2)
        self.assertEqual(asignaturas[0].nombre, "Física")
        self.assertEqual(asignaturas[1].nombre, "Química")

if __name__ == "__main__":
    unittest.main()
