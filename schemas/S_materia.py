from pydantic import BaseModel
from typing import Optional

class Materia(BaseModel):
    id:Optional[int]=None
    materia:str
    cuatrimestre:str

    class Config:
        orm_mode = True

class MateriaUpdate(BaseModel):
    materia:str
    cuatrimestre:str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str