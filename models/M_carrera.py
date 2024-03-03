from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from config.conexion import Base

class carreras(Base):
    __tablename__='tbl_carreras'
    Id_carrera = Column(Integer,primary_key=True,index=True)
    relacion_alumno = relationship("alumnos", back_populates="relacion_carrera")
    carrera = Column(String(20))
    descripcion = Column(String(200))

