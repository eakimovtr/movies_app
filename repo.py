from csv import reader, writer
import datetime


class Movie:
    def __init__(self, title: str, genre: list[str], producer: str,
                 year: datetime.date, length: int, studio: str, actors: list[str]):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year = year
        self.length = length
        self.studio = studio
        self.actors = actors

    def __str__(self) -> str:
        return f"{self.title}, {self.year}"


class MovieRepo:
    def __init__(self, src: str):
        '''
        Initialize a movie repository.

        Keyword arguments:
        src -- path to the CSV file with movies
        '''
        self.src = src
        self.database: list[Movie] = []
        with open(self.src, encoding="utf-8") as f:
            rows = reader(f)
            for row in rows:
                # REDO IMMEDIATELY
                movie = Movie(*row)
                movie.genre = movie.genre.split(';')
                movie.year = datetime.date(int(movie.year), 1, 1)
                movie.length = int(movie.length)
                movie.actors = movie.actors.split(';')
                self.database.append(movie)

    def get_all_movies(self) -> list[Movie]:
        return self.database

    def get_movies_by(self, filter: dict[str, str]) -> list[Movie]:
        if len(filter) == 0:
            return []
            
        filter = MovieRepo.create_filter(filter)
        
        for movie in self.database:
            print("")
            for item in zip(filter.values(),movie.__dict__.values()):
                print(item)
        
        return []
    
    @staticmethod
    def create_filter(filter: dict[str, str]) -> dict[str]:
        filter['genre'] = [genre.strip() for genre in filter['genre'].split(',')] if filter['genre'] else ''
        filter['actors'] = [actor.strip() for actor in filter['actors'].split(',')] if filter['actors'] else ''
        return filter
    
    
repo = MovieRepo("movies.csv")
filter = {'title': 'godfather', 'genre': 'drama, comedy', 'producer': '', 'year': '', 'length': '', 'studio': '', 'actors': 'actor1, actor2'}
repo.get_movies_by(filter)