from fastapi import APIRouter,Depends
# from typing import List
from models import M_calificacion,M_alumno,M_materia
from schemas import S_calificacion
from config.conexion import SessionLocal,engine
from sqlalchemy.orm import Session

M_calificacion.Base.metadata.create_all(bind=engine)
calificacion = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@calificacion.get("/calificaciones/", response_model=list[dict])
def show_calificaciones(db:Session=Depends(get_db)):
    return [{"nombre_alumno": c.R_calificacion_alumno.nombre, 
             "nombre_materia": c.R_calificacion_materia.materia, 
             "calificacion": c.calificacion} 
            for c in db.query(M_calificacion.calificaciones).all()]

@calificacion.post("/calificaciones/",response_model=None)
def create_calificacion(entrada:S_calificacion.Calificacion,db:Session=Depends(get_db)):
    calificacion = M_calificacion.calificaciones(Fk_alumno = entrada.Fk_alumno,Fk_materia = entrada.Fk_materia,calificacion = entrada.calificacion)
    db.add(calificacion)
    db.commit()
    db.refresh(calificacion)
    return calificacion

@calificacion.put("/calificaciones/{id}",response_model=None)
async def update_calificacion(id:int,entrada:S_calificacion.CalificacionUpdate,db:Session=Depends(get_db)):
    calificacion = db.query(M_calificacion.calificaciones).filter_by(id=id).first()
    if calificacion:
        # Actualiza los valores del alumno
        calificacion.calificacion = entrada.calificacion
        db.commit()
        db.refresh(calificacion)
        return calificacion
    else:
        return {"mensaje": "Calificacion no encontrada"}

@calificacion.delete("/calificaciones/{id}",response_model=None)
async def delete_calificacion(id:int,db:Session=Depends(get_db)):
    calificacion = db.query(M_calificacion.calificaciones).filter_by(id=id).first()
    db.delete(calificacion)
    db.commit()
    respuesta = S_calificacion.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta