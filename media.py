"""Class representing a movie"""
class Movie():
    """
        __init__ is a constructor for a Movie object.

        It receives a movie_title representing the title of a movie,
        a movie_image that is a url to the movie poster image and
        movie_trailer that is a youtube url for the movie trailer.
    """
    def __init__(self, movie_title, movie_image, movie_trailer):
        self.title = movie_title
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer
