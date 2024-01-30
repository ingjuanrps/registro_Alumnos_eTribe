<p align="center">
  <img src="" alt="Portada">
</p>

<h1 align="center">  Registro de Alumnos / eTribe </h1>

## 📋 Indice
1. [Descripcion del Proyecto.](#descripcion)
2. [Creacion de DataFrames.](#dataframe)
3. [Creacion de la base de datos y sus tablas.](#basedatos)
4. [Creación de los microservicios (funciones).](#microservicios)
5. [Creación de FastAPI](#fastapi)
6. [Stack Tecnológico.](#stack)
7. [Contacto.](#contacto)



## 1. Descripcion del Proyecto. <a name="descripcion"></a>

El siguiente proyecto consiste en crear una base de datos en MySQL para registrar alumnos (id, nombre, apellido, correo), materias (id, nombre de materis), profesores (id, nombre, apellido, correo), por medio de la programación con el lenguaje Python. 

## 2. Creacion de DataFrames. <a name="dataframe"></a>

Se crearon unos DataFrame llamados alumnos, materias, profesores los cuales contiene los datos con los que cargaremos las tablas de la base de datos registros_alumnos creada a travez de Python. 
[Link](https://github.com/ingjuanrps/registro_Alumnos_eTribe/blob/master/2dataFrame.ipynb)


## 3. Creacion de la base de datos y sus tablas. <a name="basedatos"></a>

Para la creación de la base de datos y sus tablas se uso:

+ **import pandas**: Biblioteca de Python que se utiliza para el análisis y manipulación de datos.
+ **import mysql.connector**: Módulo de Python que proporciona una interfaz para conecctarse y trabajar con bases de datos MySQL.
+ **from sqlalchemy import create_engine**: Establece la conexión con la base de datos mediante SQLAlchemy, y con CREATE_ENGINE toma como argumento la URL de la conexión de la base de datosy devuelve un objeto.
+ **%store -r**: Función para recuperar variables que han sido almacenadas previamente con %store.
+ **Querys SQL**: Instrucciones para interactuar con la base de datos.
+ **Instancias de variables de los DataFrame**: Instancias recuperadas del alamacenamineto de %store y contienen los DataFrame para llenado de datos en las tablas de la base de datos.
+ [Link](https://github.com/ingjuanrps/registro_Alumnos_eTribe/blob/master/3mysql.ipynb)

## 4. Creación de los microservicios (funciones). <a name="microservicios"></a>

Se crearon las funciones solicitadas y se revisa su funcionamiento para despues usarlas en FastAPI. [Link](https://github.com/ingjuanrps/registro_Alumnos_eTribe/blob/master/microSer.ipynb)

## 5. Creación de FastAPI. <a name="fastapi"></a>

Se crea archivo main.py para la conección con FastAPI con los microservicios creados anteriormente. [Link](https://github.com/ingjuanrps/registro_Alumnos_eTribe/blob/master/main.py)

## 6. Stack Tecnológico. <a name="stack"></a>

Python
MySQL
FastAPI

## 7. Contacto. <a name="contacto"></a>

[Contacto](https://github.com/ingjuanrps)


