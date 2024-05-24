from view import MovieView
from model import MovieModel


class MovieController:
    def __init__(self):
        self.view = MovieView()
        self.model = MovieModel()

    def run(self) -> None:
        user_option = ""
        while user_option != "q":
            user_option = self.view.wait_user_answer()
            match user_option:
                case "1":
                    filter = self.view.get_target()
                    movies = self.model.get_movies_by(filter)
                    self.view.display_movies(movies, search=True)
                case "2":
                    movies = self.model.get_movies()
                    self.view.display_movies(movies)