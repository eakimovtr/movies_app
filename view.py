class MovieView:
    def __init__(self) -> None:
        pass
    
    def wait_user_answer(self) -> str:
        print("\nWaiting for user input...")
        print("Available actions:",
              "\n1\tSearch movie",
              "\n2\tShow all movies",
              "\n3\tAdd new movie",
              "\nq\tExit")
        user_query = input("Choose menu option: ")
        return user_query
    
    def get_target(self) -> str:
        return input("Enter search info: ")
    
    def display_movies(self, movies: list, search=False) -> None:
        header = "\n---SEARCH RESULTS---" if search else "\n---MOVIES---"
        print(header)
        if len(movies) == 0:
            print("No movies found")
        for i, movie in enumerate(movies, start=1):
            print(i, movie)
        