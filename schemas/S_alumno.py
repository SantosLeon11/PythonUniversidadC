from pydantic import BaseModel
from typing import Optional, List

class Alumno(BaseModel):
    id:Optional[int]=None
    Fk_carrera:Optional[int]=None
    nombre:str
    apellido:str
    edad:str
    email:str
    estado:int
    materias: List[int]

    class Config:
        orm_mode = True

class AlumnoUpdate(BaseModel):
    nombre:str
    apellido:str
    edad:str
    email:str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str