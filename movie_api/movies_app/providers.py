class GenericProvider(object):
    def __init__(self, movie):
        self.movie = movie
        self.provider = eval(movie.provider + "Provider")

    def upload(self, file, title, plot):
        return self.provider(self.movie).upload(file, title, plot)

    def retrieve(self):
        return self.provider(self.movie).retrieve()
