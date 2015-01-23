class Movie():
    def __init__(self, name, movie_id, genre="", showtimes=[]):
        self.name = name
        self.id = movie_id
        self.showtimes = showtimes
        self.genre = genre