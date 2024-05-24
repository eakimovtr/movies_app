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
        '''
        Construct a search dictionary from user input
        '''
        search_filter: dict[str, str] = {}
        allowed_fields = ["title", "genre", "producer", "year", "length", "studio", "actors"]
        
        print("\nEnter search options","\ns to stop")
        for i in range(len(allowed_fields)):
            value = input(f"Enter value for field '{allowed_fields[i]}'. Use , for multiple options: ")
            if value == 's':
                for j in range(i, len(allowed_fields)):
                    search_filter[allowed_fields[j]] = ""
                break
            
            search_filter[allowed_fields[i]] = value
            
        return search_filter
    
    def display_movies(self, movies: list, search=False) -> None:
        header = "\n---SEARCH RESULTS---" if search else "\n---MOVIES---"
        print(header)
        if len(movies) == 0:
            print("No movies found")
        for i, movie in enumerate(movies, start=1):
            print(i, movie)
            
    def display_movie_entry(self) -> str:
        print("Enter movie data. Use semicolon between entries in one category")
        fields = ["title", "genre", "producer", "year", "length", "studio", "actors"]
        res = []
        for field in fields:
            value = input(f"Enter {field}: ")
            res.append(value)
        return ','.join(res)