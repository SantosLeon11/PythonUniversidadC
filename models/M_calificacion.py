from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from config.conexion import Base

class calificaciones(Base):
    __tablename__='tbl_calificaciones'
    Id_alumno = Column(Integer,primary_key=True,index=True)
    Fk_alumno = Column(Integer, ForeignKey('tbl_alumnos.Id_alumno'))
    R_calificacion_alumno = relationship("alumnos", back_populates="R_alumno_calificacion")
    Fk_materia = Column(Integer, ForeignKey('tbl_materias.Id_materia'))
    R_calificacion_materia = relationship("materias", back_populates="R_materia_calificacion")
    calificacion = Column(String(20))
