from fastapi import APIRouter,Depends, HTTPException
# from typing import List
from models import M_alumno,M_materia
from models.M_alumno import MateriasAlumno
from schemas import S_alumno
from config.conexion import SessionLocal,engine
from sqlalchemy.orm import Session

M_alumno.Base.metadata.create_all(bind=engine)
alumno = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@alumno.get("/alumnos/",response_model=None)
def show_alumnos(db:Session=Depends(get_db)):
    alumnos = db.query(M_alumno.alumnos).all()
    for alumno in alumnos:
        db.refresh(alumno)  # Actualizar el objeto para cargar las relaciones
        alumno.materias = ", ".join([materia.materia.materia for materia in alumno.materias]) if alumno.materias else ""

    return alumnos

@alumno.post("/alumnos/",response_model=None)
def create_alumnos(entrada:S_alumno.Alumno,db:Session=Depends(get_db)):
    alumno = M_alumno.alumnos(Fk_carrera = entrada.Fk_carrera,nombre = entrada.nombre,apellido = entrada.apellido,
                              edad = entrada.edad,email = entrada.email, estado = entrada.estado)
    db.add(alumno)
    db.commit()
    db.refresh(alumno)
    
    # Asociar las materias al alumno
    for materia_id in entrada.materias:
        materia = db.query(M_materia.materias).filter(M_materia.materias.Id_materia == materia_id).first()
        if materia is None:
            raise HTTPException(status_code=404, detail=f"No se encontró la materia con ID {materia_id}")
        
        nueva_relacion_materia_alumno = MateriasAlumno(
            Id_alumno=alumno.Id_alumno,
            Id_materia=materia_id
        )
        db.add(nueva_relacion_materia_alumno)
    db.commit()
    return alumno

@alumno.put("/alumnos/{alumno_id}",response_model=None)
async def update_alumno(id:int,entrada:S_alumno.AlumnoUpdate,db:Session=Depends(get_db)):
    alumno = db.query(M_alumno.alumnos).filter_by(id=id).first()
    if alumno:
        # Actualiza los valores del alumno
        alumno.nombre = entrada.nombre
        alumno.apellido = entrada.apellido
        alumno.edad = entrada.edad
        alumno.email = entrada.email
        db.commit()
        db.refresh(alumno)
        return alumno
    else:
        return {"mensaje": "Alumno no encontrado"}

@alumno.delete("/alumnos/{alumno_id}",response_model=None)
async def delete_alumno(id:int,db:Session=Depends(get_db)):
    alumno = db.query(M_alumno.alumnos).filter_by(id=id).first()
    db.delete(alumno)
    db.commit()
    respuesta = S_alumno.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta