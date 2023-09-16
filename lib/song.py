class Song:
    artist_count =[]
    genre_count = []
    count = 0
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_count()

    @classmethod
    def add_song_count(cls, increment = 1):
        cls.count += increment

    # @classmethod
    # def 

