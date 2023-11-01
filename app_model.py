from peewee import *

sqlite_db = SqliteDatabase('./netflixpicks_app.db', pragmas={'journal_mode': 'wal'})

try:
    """Intento de conexion a la base de datos"""
    sqlite_db.connect()
    sqlite_db.close()
except OperationalError as e:
    print("Error al conectar con la BD.", e)
    exit()

class BaseModel(Model):
    """Clase base para las entidades de la base"""
    class Meta:
        database = sqlite_db

class MainGenre(BaseModel):
    """Entidad Genero principal"""
    id_genre = AutoField(primary_key = True)
    genre = TextField(unique = True, null = False)
    
    def __str__(self):
        return self.genre

    class Meta:
        db_table='genres'

class MainProduction (BaseModel):
    """Entidad Produccion principal"""
    id_production = AutoField(primary_key = True)
    production = TextField(unique = True, null = False)
    
    def __str__(self):
        return self.production

    class Meta:
        db_table='productions'

class AgeCertification (BaseModel):
    """Entidad Clasificacion de edad"""
    id_age_certification = AutoField(primary_key = True)
    age_certification = TextField(unique = True, null = False)
    
    def __str__(self):
        return self.age_certification

    class Meta:
        db_table='age_certifications'

class Film (BaseModel):
    """Entidad que recopila las mejores PELICULAS de Netflix"""
    id_film = AutoField(primary_key = True)
    film_title = TextField(null= False)
    film_relase_year = IntegerField(null=True)
    film_score = FloatField(null= False)
    film_num_votes = IntegerField(null=False)
    film_duration = IntegerField(null=False)
    film_genre = ForeignKeyField (MainGenre, backref='genres')
    film_production = ForeignKeyField(MainProduction, backref='productions')
    film_title_id = TextField(null=False)
    film_age_certification = ForeignKeyField(AgeCertification, backref='age_certifications')

    def __str__(self):
        return self.film_title

    class Meta:
        db_table = 'films_netflix'

class Show (BaseModel):
    """Entidad que recopila las mejores PELICULAS de Netflix"""
    id_show = AutoField(primary_key = True)
    show_title = TextField(null= False)
    show_relase_year = IntegerField(null=True)
    show_score = FloatField(null= False)
    show_num_votes = IntegerField(null=False)
    show_seasons = IntegerField (null=False)
    show_duration = IntegerField(null=False)
    show_genre = ForeignKeyField (MainGenre, backref='genres')
    show_production = ForeignKeyField(MainProduction, backref='productions')
    show_title_id = TextField(null=False, unique=True)
    show_age_certification = ForeignKeyField(AgeCertification, backref='age_certifications')

    def __str__(self):
        return self.show_title

    class Meta:
        db_table = 'shows_netflix'

class Credit (BaseModel):
    id_credit = AutoField(primary_key = True)
    credit_title_id = TextField(null=False)
    name = TextField(null=False)
    actor = BooleanField(default=False) #True sera actor y False director

    def is_actor ():
        if self.actor:
            return "Actor/Actriz"
        else:
            return "Director/a"

    def __str__(self):
        return f"{self.name} - {self.is_actor}"

    class Meta:
        db_table = 'credits'