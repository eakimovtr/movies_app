from csv import reader, writer


class Movie:
    def __init__(self, title: str, genre: list[str], producer: str,
                 year: str, length: str, studio: str, actors: list[str]):
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

    def get_all_movies(self) -> list[Movie]:
        res: list[Movie] = []
        with open(self.src, encoding="utf-8") as f:
            rows = reader(f)
            for row in rows:
                res.append(Movie(*row))
                
        return res

    def get_movies_by(self, filter) -> list[Movie]:
        return self.get_all_movies()