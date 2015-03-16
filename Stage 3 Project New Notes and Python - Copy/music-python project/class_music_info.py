import webbrowser

class Music_Collection():
    def __init__(self, artist, genre, album):
        self.artist=artist
        self.genre=genre
        self.album=album

    class Favorite_Songs(Music_Collection):
    def __init__(self, artist, genre, album, song_title, song_sample):
        Music_Collection.__init__(self, artist, genre, album)
        self.song_title=song_title
        self.song_sample=song_sample

    def show_info(self):
        print("The song title is "+self.song_title)
        print("The artist is "+self.artist) 
        print("Genre is "+self.genre)
        print("From the album "+self.album)        
        

    def play_song(self):
        webbrowser.open(self.song_sample)

        
        
