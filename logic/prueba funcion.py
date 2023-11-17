from peewee import *
from app_model import *
import random

button1 = ""
button2 = ""
button3 = ""
button4 = ""
def conect_db ():
    try:
        sqlite_db.connect()
        sqlite_db.close()
    except OperationalError as e:
        print("Error al conectar con la BD.", e)
        exit()

def select_options (question):
    try:
        table = get_table(question)
        #selecciono la tabla, ordeno de manera random y tomo los primeros 4 resultados, convierto esto a una lista y asigno a las variables de boton
        query = list(table.select().order_by(fn.Random()).limit(4))
        return query
    except NameError as e:
        print("La clave pasada es erronea. ", e)
    except OperationalError as e:
        print("Error en la conexion con la base. ",e)


def get_table ( key):
    entidad = {
        "peliculas": Film,
        "series": Show,
        "creditos": Credit,
        "genero": MainGenre,
        "edad": AgeCertification,
        "produccion": MainProduction,
    }
    if key in entidad:
        return entidad[key]
    else:
        raise NameError

prueba= select_options("edad")
for elem in prueba:
    print(elem)