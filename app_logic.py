from peewee import *
from app_model import *
import random

class NetflixPicks ():

    """Comunication será el diccionario que se edita con la infor desde el front para comuinicarse con el back y poder realizar los filtros pertinentes"""
    cominication = {}
    selection = ["peliculas", "series"]
    question = ["genero", "edad", "produccion"]
    button1 = ""
    button2 = ""
    button3 = ""
    button4 = ""

    def conect_db (self):
        try:
            """Intento de conexion a la base de datos"""
            sqlite_db.connect()
            sqlite_db.close()
        except OperationalError as e:
            print("Error al conectar con la BD.", e)
            exit()


    def select_options (self, question):
        """Segun lo que se pregunta se filtratan las opciones de respuesta y se elige entre las opciones 4 para mostrar como opciones"""
        try:
            table = self.get_table(question)
            #selecciono la tabla, ordeno de manera random y tomo los primeros 4 resultados, convierto esto a una lista y asigno a las variables de boton
            query = list(table.select().order_by(fn.Random()).limit(4))
            self.button1 = query[0]
            self.button2 = query[1]
            self.button3 = query[2]
            self.button4 = query[3]
        except ValueError as e:
            print("La clave pasada es erronea. ", e)
        except OperationalError as e:
            print("Error en la conexion con la base. ",e)

    def get_table (self, key):
        """Segun la palabra clave trae la entidad de la tabla"""
        entidad = {
            "peliculas": Film,
            "series": Show,
            "genero": MainGenre,
            "edad": AgeCertification,
            "produccion": MainProduction,
        }
        if key in entidad:
            return entidad[key]
        else:
            raise ValueError
