from fastapi import APIRouter,Depends
from models import M_materia
from schemas import S_materia
from config.conexion import SessionLocal,engine
from sqlalchemy.orm import Session

M_materia.Base.metadata.create_all(bind=engine)
materia = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@materia.get("/materias/",response_model=None)
def show_materias(db:Session=Depends(get_db)):
    materias = db.query(M_materia.materias).all()
    return materias

@materia.post("/materias/",response_model=None)
def create_materia(entrada:S_materia.Materia,db:Session=Depends(get_db)):
    materia = M_materia.materias(materia = entrada.materia,cuatrimestre = entrada.cuatrimestre)
    db.add(materia)
    db.commit()
    db.refresh(materia)
    return materia

@materia.put("/materias/{id}",response_model=None)
async def update_materia(id:int,entrada:S_materia.MateriaUpdate,db:Session=Depends(get_db)):
    materia = db.query(M_materia.materias).filter_by(id=id).first()
    if materia:
        # Actualiza los valores del alumno
        materia.materia = entrada.materia
        materia.cuatrimestre = entrada.cuatrimestre
        db.commit()
        db.refresh(materia)
        return materia
    else:
        return {"mensaje": "Alumno no encontrado"}

@materia.delete("/materias/{id}",response_model=None)
async def delete_materia(id:int,db:Session=Depends(get_db)):
    materia = db.query(M_materia.materias).filter_by(id=id).first()
    db.delete(materia)
    db.commit()
    respuesta = S_materia.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta