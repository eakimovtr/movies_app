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
    
    def get_target(self) -> dict[str, str]:
        search_filter: dict[str, str] = {}
        allowed_fields = ["title", "genre", "producer", "year", "length", "studio", "actors"]
        
        print("\nEnter search options\nAllowed fields: ", *allowed_fields, "\ns to stop")
        while len(search_filter.keys()) < 7:
            field = input("Enter search field: ")
            if field == 's':
                break
            if field not in allowed_fields:
                print("Invalid field!")
                continue
            
            value = input("Enter field value: ")
            
            search_filter[field] = value
            
        return search_filter
    
    def display_movies(self, movies: list, search=False) -> None:
        header = "\n---SEARCH RESULTS---" if search else "\n---MOVIES---"
        print(header)
        if len(movies) == 0:
            print("No movies found")
        for i, movie in enumerate(movies, start=1):
            print(i, movie)
        