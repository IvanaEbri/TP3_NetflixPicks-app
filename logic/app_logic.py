from peewee import *
from logic.app_model import *
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
        self.question_text = ["Seleccione los genero que prefiere", "Seleccione el tipo de público de su preferencia", "Seleccione de que paises productores prefiere"]

        """Comunication será el diccionario que se edita con la infor desde el front para comuinicarse con el back y poder realizar los filtros pertinentes"""
        self.comunication = {
            self.selected:"",
            self.question[0]: [],
            self.question[1]: [],
            self.question[2]: [],
        }

    def conect_db (self):
        """Intento de conexion a la base de datos"""
        try:
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
            botones = self.certificacion_sin_dups(question,query)
            self.button1 = botones[0]
            self.button2 = botones[1]
            self.button3 = botones[2]
            self.button4 = botones[3]
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
                generos.append(MainGenre.get(MainGenre.genero == elem).get_id())
            for elem in res_edades:
                edades.append(AgeCertification.get(AgeCertification.certificacion == elem).get_id())
            for elem in res_producciones:
                producciones.append(MainProduction.get(MainProduction.produccion == elem).get_id())

            if self.comunication[self.selected] ==self.selection[0]:
                resultados=list(table.select().where(
                    (table.film_genre<< generos) & (table.film_age_certification << edades) & (table.film_production << producciones)
                ).order_by(fn.Random()).limit(4))
            else:
                resultados= list(table.select().where(
                    (table.show_genre<< generos) & (table.show_age_certification << edades) & (table.show_production << producciones)
                ).order_by(fn.Random()).limit(4))

            if resultados == []:
                resultados = "No hay resultados para mostrarte :("
            else: 
                if len(resultados)<4:
                    resultados.append("No hemos hallado más resultados :/")
            return  resultados 
        except ValueError as e:
            print("No se han seleccionado los parametros indicados.",e)
        except NameError as e:
            print("Los paramtros seleccionados no son correctos.",e)
        '''except Exception as e:
            print("Error sin definir aún. Eevee is working here", e)'''

    def certificacion_sin_dups(self,question, query):
        if (question == "edad"):
            lista = []
            for elem in query:
                lista.append(elem.__str__())
            lista = set(lista)
            while len(lista)!= 4:
                subquery= list(AgeCertification.select().order_by(fn.Random()).limit(1))
                try:
                    for elem in subquery:
                        lista.add(elem.__str__())
                except Exception as e:
                    print(e)
            query=list(lista)
        return query