from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from config.conexion import Base

class alumnos(Base):
    __tablename__='tbl_alumnos'
    Id_alumno = Column(Integer,primary_key=True,index=True)
    Fk_carrera = Column(Integer, ForeignKey('tbl_carreras.Id_carrera'))
    relacion_carrera = relationship("carreras", back_populates="relacion_alumno")
    materias = relationship("MateriasAlumno", back_populates="alumno")
    nombre = Column(String(20))
    apellido = Column(String(200))
    edad = Column(String(20))
    email = Column(String(20))
    estado = Column(Integer)

class MateriasAlumno(Base):
    __tablename__='tbl_materias_alumno'
    Id = Column(Integer, primary_key=True)
    Id_alumno = Column(Integer, ForeignKey('tbl_alumnos.Id_alumno'))
    Id_materia = Column(Integer, ForeignKey('tbl_materias.Id_materia'))
    alumno = relationship("alumnos", back_populates="materias")
    materia = relationship("materias")

