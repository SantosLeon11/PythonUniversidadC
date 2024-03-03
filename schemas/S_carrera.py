from pydantic import BaseModel
from typing import Optional

class Carrera(BaseModel):
    id:Optional[int]=None
    carrera:str
    descripcion:str

    class Config:
        orm_mode = True

class CarreraUpdate(BaseModel):
    carrera:str
    descripcion:str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str