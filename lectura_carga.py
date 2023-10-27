from peewee import *
import pandas as pd

#sqlite_db = SqliteDatabase('./TP3_NetflixPicks-app/netflixpicks_app.db', pragmas={'journal_mode': 'wal'})

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

    def make_new_dataset (self):
        """Lectura de los dataset y armado de los nuevos data set a limpiar"""
        try:
            df_movies, df_shows, df_titles, df_credits = self.read_csv_proyect()
            movies_ds = df_movies.merge(df_titles, left_on='TITLE', right_on= 'title', how='inner')
            showss_ds = df_shows.merge(df_titles, left_on='TITLE', right_on= 'title', how='inner')
            return movies_ds, df_shows, df_credits
        except Exception as e:
            print("Error al joinnear el dataset.", e)
            exit()

    def read_csv_proyect (self):
        """Lectura del dataset mediante modulo 'pandas'"""
        try:
            df_movies = pd.read_csv(best_movies, sep = ',', quotechar='"', on_bad_lines='skip', header=0)
            df_shows = pd.read_csv(best_shows, sep = ',', quotechar='"', on_bad_lines='skip', header=0)
            df_titles = pd.read_csv(raw_titles, sep = ',', quotechar='"', on_bad_lines='skip', header=0)
            df_credits = pd.read_csv(raw_credits, sep = ',', quotechar='"', on_bad_lines='skip')
            return df_movies, df_shows, df_titles, df_credits
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            exit()



if __name__=='__main__':
    gestor = CreateDB()
    gestor.make_new_dataset()
    print ("funco!")