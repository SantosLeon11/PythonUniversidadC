from fastapi import FastAPI
from routes.alumno import alumno
from routes.carrera import carrera
from routes.materia import materia

main = FastAPI()

main.include_router(alumno)
main.include_router(carrera)
main.include_router(materia)

