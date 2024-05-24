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

    def check_match(self, filter: dict[str]) -> bool:
        '''
        Check whether given movie matches all search criteria
        '''
        if not self.check_title(filter["title"]):
            return False
        if not self.check_year(filter["year"]):
            return False
        if not self.check_length(filter["length"]):
            return False

        return True

    def check_title(self, match_title: str) -> bool:
        return True if (not match_title) or (match_title.lower() in self.title.lower()) else False

    def check_year(self, match_year: datetime.date) -> bool:
        return True if (not match_year) or (self.year <= match_year) else False

    def check_length(self, match_length: tuple) -> bool:
        if not match_length:
            return True

        comparison: str = match_length[0]
        search_length: int = match_length[1]
        match comparison:
            case '<':
                if self.length < search_length:
                    return True
            case '<=':
                if self.length <= search_length:
                    return True
            case '>':
                if self.length > search_length:
                    return True
            case '>=':
                if self.length >= search_length:
                    return True
            case '=':
                if self.length == search_length:
                    return True

        return False

    @staticmethod
    def from_csv(row: list[str]):
        row[1] = row[1].split(';')
        row[3] = datetime.date(int(row[3]), 1, 1)
        row[4] = int(row[4])
        row[6] = row[6].split(';')
        return Movie(*row)
    
    @staticmethod
    def from_str(movie_str: str):
        return Movie.from_csv(movie_str.split(','))

    def __str__(self) -> str:
        return f"{self.title}, {self.year.year}"


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
                self.database.append(Movie.from_csv(row))

    def get_all_movies(self) -> list[Movie]:
        return self.database

    def get_movies_by(self, filter: dict[str, str]) -> list[Movie]:
        res: list[Movie] = []
        if len(filter) == 0:
            return res

        filter = MovieRepo.create_filter(filter)
        # print(filter)

        for movie in self.database:
            if movie.check_match(filter):
                res.append(movie)

        return res
    
    def save_movie(self, movie: Movie) -> Movie:
        self.database.append(movie)
        with open(self.src, 'a', encoding="utf-8") as f:
            csv_writer = writer(f)
            f.write("\n")
            
            movie_dict = movie.__dict__
            movie_dict['genre'] = ';'.join(movie_dict['genre'])
            movie_dict['actors'] = ';'.join(movie_dict['actors'])
            csv_writer.writerow(movie_dict.values())
            
        return Movie

    @staticmethod
    def create_filter(filter: dict[str, str]) -> dict[str]:
        filter['genre'] = [genre.strip()
                           for genre in filter['genre'].split(',')] if filter['genre'] else ''

        filter['year'] = datetime.date(
            int(filter['year']), 1, 1) if filter['year'] else ''

        if filter['length']:
            filter['length'] = filter['length'].split()
            filter['length'][1] = int(filter['length'][1])
            filter['length'] = tuple(filter['length'])

        filter['actors'] = [actor.strip() for actor in filter['actors'].split(
            ',')] if filter['actors'] else ''
        return filter


# repo = MovieRepo("D:\Python\Акимов\py_2024_05_22\movies.csv")
# filter = {'title': '', 'genre': '', 'producer': '',
#           'year': '', 'length': '> 180', 'studio': '', 'actors': ''}
# print(*repo.get_movies_by(filter))
# print(repo.save_movie(repo.database[1]))