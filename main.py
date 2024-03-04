from fastapi import FastAPI
from routes.alumno import alumno
from routes.carrera import carrera
from routes.materia import materia
from routes.calificacion import calificacion

main = FastAPI()

main.include_router(alumno)
main.include_router(carrera)
main.include_router(materia)
main.include_router(calificacion)

