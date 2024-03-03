from fastapi import APIRouter,Depends
# from typing import List
from models import M_carrera
from schemas import S_carrera
from config.conexion import SessionLocal,engine
from sqlalchemy.orm import Session

M_carrera.Base.metadata.create_all(bind=engine)
carrera = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@carrera.get("/carreras/",response_model=None)
def show_carreras(db:Session=Depends(get_db)):
    alumnos = db.query(M_carrera.carreras).all()
    return alumnos

@carrera.post("/carreras/",response_model=None)
def create_carrera(entrada:S_carrera.Carrera,db:Session=Depends(get_db)):
    alumno = M_carrera.carreras(carrera = entrada.carrera,descripcion = entrada.descripcion)
    db.add(alumno)
    db.commit()
    db.refresh(alumno)
    return alumno

@carrera.put("/carreras/{id}",response_model=None)
async def update_carrera(id:int,entrada:S_carrera.CarreraUpdate,db:Session=Depends(get_db)):
    carrera = db.query(M_carrera.carreras).filter_by(id=id).first()
    if carrera:
        # Actualiza los valores del alumno
        carrera.carrera = entrada.carrera
        carrera.descripcion = entrada.descripcion
        db.commit()
        db.refresh(carrera)
        return carrera
    else:
        return {"mensaje": "Alumno no encontrado"}

@carrera.delete("/carreras/{id}",response_model=None)
async def delete_carrera(id:int,db:Session=Depends(get_db)):
    carrera = db.query(M_carrera.carreras).filter_by(id=id).first()
    db.delete(carrera)
    db.commit()
    respuesta = S_carrera.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta