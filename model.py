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


class MovieModel:
    def __init__(self, filepath) -> None:
        self.database: list[Movie] = []
        try:
            f = open(filepath, encoding="utf-8")
            rows = reader(f)
            for row in rows:
                self.database.append(Movie(*row))
        except FileNotFoundError as e:
            print(e)
            self.database: list[Movie] = []

    def get_movies_by(self, filter) -> list[Movie]:
        return self.database

    def get_movies(self) -> list[Movie]:
        return self.database