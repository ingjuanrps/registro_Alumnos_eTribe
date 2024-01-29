import pandas as pd
from fastapi import FastAPI
from fastapi import APIRouter
import mysql.connector


app= FastAPI()

@app.get('/')
def index():
    return 'Proyecto eTribe Base de datos Alumnos'

# Conexión a la base de datos
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='nicojr',
        database='registros_alumnos'
    )

@app.get('/user1/{alumno_id}')
# Obtener alumnos por ID
def get_alumno_by_id(alumno_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM alumnos WHERE id_alumnos = %s"
    cursor.execute(query, (alumno_id,))
    alumno = cursor.fetchone()
    conn.close()
    return alumno

@app.get('/user2/{alumno_id}{correo}')
# Insertar información de un alumno
def update_alumno(alumno_id, correo):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO alumnos (id_alumnos, correo) VALUES (%s, %s) ON DUPLICATE KEY UPDATE correo = %s"
    cursor.execute(query, (alumno_id, correo, correo))
    conn.commit()
    conn.close()
    
    
@app.get('/user3/{alumno_id}')
# Eliminar a un alumno
def delete_alumno(alumno_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM alumnos WHERE id_alumnos = %s"
    cursor.execute(query, (alumno_id,))
    conn.commit()
    conn.close()
    
@app.get('/user4/{materia_id}')
# Obtener materia por ID
def get_materia_by_id(materia_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM materias WHERE id_materia = %s"
    cursor.execute(query, (materia_id,))
    materia = cursor.fetchone()
    conn.close()
    return materia

@app.get('/user5/{materia_id}')
# Dar de baja una materia
def delete_materia(materia_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM materias WHERE id_materia = %s"
    cursor.execute(query, (materia_id,))
    conn.commit()
    conn.close()
    
@app.get('/user6/{alumno_id}{materia}')
# Dar de alta o actualizar una materia
def update_materia(materia_id, materia):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO materias (id_materia, nombre_materia) VALUES (%s, %s) ON DUPLICATE KEY UPDATE nombre_materia = %s"
    cursor.execute(query, (materia_id, materia, materia))
    conn.commit()
    conn.close()
    
@app.get('/user7/{alumno_id}')
# Obtener todas las materias relacionadas con un alumno
def get_materias_alumno(alumno_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT materias.nombre FROM materias JOIN inscripciones ON materias.id = inscripciones.materia_id WHERE inscripciones.alumno_id = %s"
    cursor.execute(query, (alumno_id,))
    materias = cursor.fetchall()
    conn.close()
    return materias