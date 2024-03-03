from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from config.conexion import Base

class materias(Base):
    __tablename__='tbl_materias'
    Id_materia = Column(Integer,primary_key=True,index=True)
    materia = Column(String(20))
    cuatrimestre = Column(String(200))

