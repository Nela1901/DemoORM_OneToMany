from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class Estudiante(Base):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    asignaturas = relationship("Asignatura", back_populates="estudiante", cascade="all, delete-orphan")

class Asignatura(Base):
    __tablename__ = 'asignaturas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    estudiante = relationship("Estudiante", back_populates="asignaturas")
