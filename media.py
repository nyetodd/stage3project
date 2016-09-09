import webbrowser

class Video():
	""" Parent class for all types of video
	
	Attributes:
		title (str): Movie title.
        duration (int): Movie length (in minutes).
	"""
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

class Movie(Video):
	""" This class provides a way to store movie related information.

	Attributes:
        title (str): Movie title.
        duration (int): Movie length (in minutes).
        storyline (str): Story overview for movie.
        primary_cast (str): Primary cast of movie.
        screenwriter (str): Movie writer.
        director (str): Movie director.
        poster_image_url(str): URL for image of movie poster.
        trailer_youtube_url (str): URL for image of movie trailer
        release date (str): date film released
        VALID_RATINGS (list): This value cannot be set, but is accessible
        to all instances of type movie. 
	"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, title, duration, storyline, primary_cast, screenwriter,
	 director, poster_image_url, trailer_youtube_url, release_date):
		Video.__init__(self, title, duration)
		self.storyline = storyline
		self.primary_cast = primary_cast
		self.screenwriter = screenwriter
		self.director = director
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.release_date = release_date

	def show_trailer(self):
		''' takes in a movie object and launches the trailer for in in 
		new webbrowser window'''
		webbrowser.open(self.trailer_youtube_url)
