from repo import Movie, MovieRepo


class MovieModel:
    def __init__(self, movieRepo: MovieRepo = MovieRepo("D:\Python\Акимов\py_2024_05_22\movies.csv")):
        '''
        Initialize a model with injected movie repository.
        
        Keyword arguments:
        movieRepo -- movie repository to use
        '''
        self.movieRepo = movieRepo

    def get_movies_by(self, filter: dict[str, str]) -> list[Movie]:
        return self.movieRepo.get_movies_by(filter)

    def get_movies(self) -> list[Movie]:
        return self.movieRepo.get_all_movies()
    
    def save_movie(self, movie: Movie) -> Movie:
        return self.movieRepo.save_movie(movie)
    