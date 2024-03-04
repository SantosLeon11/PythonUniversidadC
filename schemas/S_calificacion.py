from pydantic import BaseModel
from typing import Optional

class Calificacion(BaseModel):
    id:Optional[int]=None
    Fk_alumno:Optional[int]=None
    Fk_materia:Optional[int]=None
    calificacion:int

    class Config:
        orm_mode = True

class CalificacionUpdate(BaseModel):
    calificacion:int

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str