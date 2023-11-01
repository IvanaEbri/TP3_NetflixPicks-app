from peewee import *
import pandas as pd
from app_model import *

best_movies = './Best_Movies_Netflix.csv'
best_shows = './Best_Shows_Netflix.csv'
raw_titles = './raw_titles.csv'
raw_credits = './raw_credits.csv'

class CreateDB():

    def connect_db (self):
        """sentencias necesarias para realizar la conexión a la base de datos "netflixpicks_app.db” """
        try:
            """Intento de conexion a la base de datos"""
            sqlite_db.connect()
        except OperationalError as e:
            print("Error al conectar con la BD.", e)
            exit()

    def load_data(self):
        """sentencias necesarias para persistir los datos de las tablas (ya transformados y 
        “limpios”) que contienen los Dataframes en la base de datos relacional SQLite. 
        Para ello se debe utilizar el método de clase Model create() en cada una 
        de las clase del modelo ORM definido"""
        self.mapear_model()

        movies_df, shows_df, credits_df = self.clean_data()
        
        #Carga de datos en la tabla 'genres'
        films_genre = list(movies_df['MAIN_GENRE'].unique())
        shows_genre = list(shows_df['MAIN_GENRE'].unique())
        genres_unique = films_genre

        for genre in shows_genre:
            if not(genre in films_genre):
                genres_unique.append(genre)

        for elem in genres_unique:
            try:
                MainGenre.create(genre = elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Generos.", e)
        print("Se completó la carga de las Generos")
        
        #Carga de datos en la tabla 'productions'
        films_production = list(movies_df['MAIN_PRODUCTION'].unique())
        shows_production = list(shows_df['MAIN_PRODUCTION'].unique())
        productions_unique = films_production

        for production in shows_production:
            if not(production in films_production):
                productions_unique.append(production)

        for elem in productions_unique:
            try:
                MainProduction.create(production = elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Producciones.", e)
        print("Se completó la carga de las Producciones")

        #Carga de datos en la tabla 'Clasificacion de edad'
        films_age = list(movies_df['age_certification'].unique())
        shows_age = list(shows_df['age_certification'].unique())
        ages_unique = films_age

        for age in shows_age:
            if not(age in films_age):
                ages_unique.append(age)

        for elem in ages_unique:
            try:
                AgeCertification.create(age_certification = elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Clasificaciones de edad.", e)
        print("Se completó la carga de las Clasificaciones de edad")
        
        #Carga de datos en la tabla 'Creditos'
        try:
            for index, elem in credits_df.iterrows():
                lactor = self.actor(elem [2])
                Credit.create (credit_title_id = elem[0], name = elem [1], actor = lactor)
            print("Se completó la carga de manera exitosa de los Creditos")
        except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Creditos.", e)
        
        #Carga de datos en la tabla 'Peliculas'
        try:
            for index,elem in movies_df.iterrows():
                genero = MainGenre.get(MainGenre.genre == elem[6])
                produccion = MainProduction.get(MainProduction.production == elem[7])
                edad = AgeCertification.get(AgeCertification.age_certification == elem[10])
                Film.create (film_title = elem[1], film_relase_year = elem [2], film_score =elem [3] ,film_num_votes= elem [4], film_duration=elem [5] , film_genre= genero, film_production=produccion, film_title_id=elem [8] ,film_age_certification = edad)
            print("Se completó la carga de manera exitosa de las Peliculas")
        except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Peliculas.", e)
        
        #Carga de datos en la tabla 'Series'
        try:
            for index,elem in shows_df.iterrows():
                genero = MainGenre.get(MainGenre.genre == elem[7])
                produccion = MainProduction.get(MainProduction.production == elem[8])
                edad = AgeCertification.get(AgeCertification.age_certification == elem[11])
                Show.create (show_title = elem[1], show_relase_year = elem [2], show_score =elem [3] ,show_num_votes= elem [4], show_duration=elem [5] , show_seasons= elem[6],show_genre= genero, show_production=produccion, show_title_id=elem [9] ,show_age_certification = edad)
            print("Se completó la carga de manera exitosa de las Series")
        except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Series.", e)

    def actor(self, elem):
        if (elem =="ACTOR"): 
            return True
        else:
            return False

    def mapear_model (self):
        """sentencias necesarias para realizar la creación de la estructura de la base de datos (tablas y relaciones) utilizando el método de instancia “create_tables(list)” del módulo peewee"""
        
        try:
            sqlite_db.create_tables([MainGenre, MainProduction, AgeCertification, Film, Show, Credit])
            print("Se crearon las tablas")
        except Exception as e:
            print("Error al crear las tablas.", e)
            exit()

    def clean_data(self):
        """Limpieza del dataset"""
        try:
            movies_df, shows_df, df_credits = self.make_new_dataset()
            movies_df=movies_df.drop(['type','runtime','genres', 'production_countries','seasons','imdb_id','imdb_score','imdb_votes'], axis=1)
            shows_df=shows_df.drop(['type','runtime','genres', 'production_countries','seasons','imdb_id','imdb_score','imdb_votes'], axis=1)
            credits_df= df_credits.drop(['index','person_id','character'], axis=1)
            movies_df.dropna(subset = ['id'], axis = 0, inplace = True)
            movies_df.dropna(subset = ['age_certification'], axis = 0, inplace = True)
            shows_df.dropna(subset= ['id'], axis=0, inplace=True)
            shows_df.dropna(subset = ['age_certification'], axis = 0, inplace = True)
            print("Los datos estan limpios")
            return movies_df, shows_df, credits_df
        except Exception as e:
            print("Error al limpiar el dataset.", e)
            exit()

    def make_new_dataset (self):
        """Lectura de los dataset y armado de los nuevos data set a limpiar"""
        try:
            df_movies, df_shows, df_titles, df_credits = self.read_csv_proyect()
            movies_df = df_movies.merge(df_titles, left_on='TITLE', right_on= 'title', how='inner')
            shows_df = df_shows.merge(df_titles, left_on='TITLE', right_on= 'title', how='inner')
            return movies_df, shows_df, df_credits
        except Exception as e:
            print("Error al joinnear el dataset.", e)
            exit()

    def read_csv_proyect (self):
        """Lectura del dataset mediante modulo 'pandas'"""
        try:
            df_movies = pd.read_csv(best_movies, sep = ',', quotechar='"', on_bad_lines='skip', header=0)
            df_shows = pd.read_csv(best_shows, sep = ',', quotechar='"', on_bad_lines='skip', header=0)
            df_titles = pd.read_csv(raw_titles, sep = ',', quotechar='"', on_bad_lines='skip', header=0)
            df_titles=df_titles.drop(['index','release_year'], axis=1)
            df_credits = pd.read_csv(raw_credits, sep = ',', quotechar='"', on_bad_lines='skip')
            return df_movies, df_shows, df_titles, df_credits
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            exit()



if __name__=='__main__':
    gestor = CreateDB()
    gestor.load_data()
    print ("funco!")