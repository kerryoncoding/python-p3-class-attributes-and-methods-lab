class Song:
    artists =[]
    genres = []
    count = 0
    genre_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count()

# Whenever a new song is created, increment count by 1
    @classmethod
    def add_song_count(cls, increment = 1):
        cls.count += increment

# adds any new unique genres to a class attribute "genres" list
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

# adds any new unique artists to a class attribute "artists" list
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

# dictionary which keys are names of genre and value is number of songs in that genre => {"Rap": 5, "Rock": 1, "Country": 3}
    @classmethod
    def add_to_genre_count(cls, genre_count):
        # create a key for each "genre" in list
        # if genre matches, increment it
        genre_count = {}

        pass


        