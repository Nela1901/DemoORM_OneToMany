from src.modelo.declarative_base import Session, Base, engine
from src.modelo.modelo import Estudiante, Asignatura

# Elimina y crea todas las tablas desde cero
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Configurar una nueva sesión
session = Session()

# Crear estudiantes
estudiante1 = Estudiante(nombre="Carlos Espinoza")
session.add(estudiante1)
session.commit()

estudiante2 = Estudiante(nombre="Lucía Ramírez")
session.add(estudiante2)
session.commit()

# Crear asignaturas asociadas a los estudiantes

asignatura1 = Asignatura(nombre="Matemáticas", estudiante_id=estudiante1.id)
session.add(asignatura1)

asignatura2 = Asignatura(nombre="Inteligencia Artificial", estudiante_id=estudiante2.id)
session.add(asignatura2)

asignatura3 = Asignatura(nombre="Desarrollo Web", estudiante_id=estudiante2.id)
session.add(asignatura3)

session.commit()
