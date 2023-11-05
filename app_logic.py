from peewee import *
from app_model import *
import random

class NetflixPicks ():

    def __init__(self):
        #clave de seleccion
        self.selected = "selected"
        #clave de serie o pelicula
        self.selection = ["peliculas", "series"]
        #claves de pregunta
        self.question = ["genero", "edad", "produccion"]
        self.button1 = ""
        self.button2 = ""
        self.button3 = ""
        self.button4 = ""
        #texto de pegunta que corresponde al mismo indice que la pregunta
        self.question_text = ["Seleccione los genero que prefiere", "Seleccione que resticcion de edad prefiere", "Seleccione de que paises productores prefiere"]

        """Comunication será el diccionario que se edita con la infor desde el front para comuinicarse con el back y poder realizar los filtros pertinentes"""
        self.comunication = {
            self.selected:"",
            self.question[0]: [],
            self.question[1]: [],
            self.question[2]: [],
        }

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
        except NameError as e:
            print("La clave pasada es erronea. ", e)
        except OperationalError as e:
            print("Error en la conexion con la base. ",e)

    def get_table (self, key):
        """Segun la palabra clave trae la entidad de la tabla"""
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

    def result(self):
        """Debo leer el diccionario que almacena 'pregunta: [respuesta/s]' y armar la query con la que haré el select sobre la tabla"""
        try:
            table = ""
            res_generos = self.comunication[self.question[0]]
            res_edades = self.comunication[self.question[1]]
            res_producciones = self.comunication[self.question[2]]
            
            if not(self.comunication[self.selected] == ""):
                table= self.get_table(self.comunication[self.selected])
                if (res_generos ==[] and res_edades ==[] and res_producciones == []):
                    raise ValueError
            else: raise ValueError

            generos=[]
            edades=[]
            producciones=[]
            for elem in res_generos:
                generos.append(MainGenre.get(MainGenre.genre == elem).get_id())
            for elem in res_edades:
                edades.append(AgeCertification.get(AgeCertification.age_certification == elem).get_id())
            for elem in res_producciones:
                producciones.append(MainProduction.get(MainProduction.production == elem).get_id())

            if self.comunication[self.selected] ==self.selection[0]:
                resultados=list(table.select().where(
                    (table.film_genre<< generos) & (table.film_age_certification << edades) & (table.film_production << producciones)
                ).order_by(fn.Random()).limit(4))
            else:
                resultados= list(table.select().where(
                    (table.show_genre<< generos) & (table.show_age_certification << edades) & (table.show_production << producciones)
                ).order_by(fn.Random()).limit(4))
            return  resultados 
        except ValueError:
            print("No se han seleccionado los parametros indicados")
        except NameError:
            print("Los paramtros seleccionados no son correctos")
        '''except Exception as e:
            print("Error sin definir aún. Eevee is working here", e)'''