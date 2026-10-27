import csv
from collections import namedtuple
from datetime import date

Pelicula = namedtuple('Pelicula', [
    "fecha_estreno",   # tipo date
    "titulo",          # tipo str
    "director",        # tipo str
    "generos",          # tipo list[str]
    "duracion",        # tipo int
    "presupuesto",     # tipo int
    "recaudacion",     # tipo int
    "reparto"          # tipo list[str]
])

def lee_peliculas(ruta_fichero: str) -> list[Pelicula]:    
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) # Saltamos la cabecera
        peliculas = []
        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno = date.fromisoformat(fecha_estreno) # Convierto fecha_estreno a date
            generos = generos.split(",")
            duracion = int(duracion)
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = reparto.split(",")
            tupla = Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto)
            peliculas.append(tupla)
        return peliculas
    
    

def existe_pelicula(peliculas: list[Pelicula], cadena_en_titulo: str) -> bool:
    """
    Comprueba si existe alguna película cuyo título contenga la cadena dada.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    cadena_en_titulo (str): Cadena a buscar en los títulos de las películas.
    Devuelve:
    bool: True si existe al menos una película cuyo título contiene la cadena, False en caso
    contrario.
    """
    existe = False
    for p in peliculas:
        if cadena_en_titulo in p.titulo:
            existe = True
            break
    return existe

def son_todas_director_genero(peliculas: list[Pelicula], director: str, genero: str) -> bool:
    """
    Comprueba si todas las películas del director dado pertenecen al género indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    director (str): Nombre del director.
    genero (str): Género a comprobar.
    Devuelve:
    bool: True si todas las películas del director pertenecen al género, False en caso contrario.
    """
    todas_genero = True
    for p in peliculas:
        # if p.director == director and genero not in p.generos:
        if p.director == director: # FILTRO
            if genero not in p.generos:
                todas_genero = False
                break

    return todas_genero
        


def construye_lista_titulos_actor(peliculas: list[Pelicula], actor: str) -> list[str]:
    """
    Devuelve una lista de títulos en los que el actor indicado aparece en el reparto.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    actor (str): Nombre del actor.
    Devuelve:
    list[str]: Lista de títulos de películas en las que aparece el actor.
    """    
    titulos = []  # res = []
    for p in peliculas:
        if actor in p.reparto: # FILTRO
            titulos.append(p.titulo)
    return titulos
    

def calcula_presupuesto_total_año(peliculas: list[Pelicula], año: int) -> int:
    """
    Suma y devuelve el presupuesto total de las películas cuyo año de estreno es el indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    año (int): Año de estreno.
    Devuelve:
    int: Presupuesto total de las películas estrenadas en el año indicado.
    """
    total = 0
    for p in peliculas:
        if p.fecha_estreno.year == año:
            total += p.presupuesto
    return total

def encuentra_pelicula_mayor_recaudacion(peliculas: list[Pelicula], genero: str) -> Pelicula | None:
    """
    Devuelve la película con mayor recaudacion entre las que incluyen el genero dado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    genero (str): Género a buscar.
    Devuelve:
    Pelicula | None: Película con mayor recaudación del género indicado, o None si no existe ninguna.
    """
    pelicula_mayor_recaudacion = None
    for p in peliculas:
        if genero in p.generos: # FILTRO
            if pelicula_mayor_recaudacion == None or p.recaudacion > pelicula_mayor_recaudacion.recaudacion:
                pelicula_mayor_recaudacion = p
    return pelicula_mayor_recaudacion







