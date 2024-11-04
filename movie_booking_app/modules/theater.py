class Theater:

    def __init__(self, screen1, screen2, screen3) -> None:
        self.screens = [screen1, screen2 , screen3]

    def list_movies(self):

        movies = []
        for screen in self.screens:
            movies.append(screen.movie.name)

        return movies

    def book_ticket(self):



        return []
