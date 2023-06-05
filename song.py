# Class song that holds all information about songs (from the table of songs)

class Song():

    def __init__(self, name, artist, music_id, genre, BPM):
        self.name = name
        self.artist = artist
        self.music_id = music_id
        self.genre = genre
        self.BPM = int(BPM)

    def __str__(self): # This is the method that is called if an instance of the class is included in a print() statement
        printout_string = f'Song name: "{self.name}", Artist: "{self.artist}", Genre: "{self.genre}", BPM: ˇ{self.BPM}'
        return printout_string

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_music_id(self):
        return self.music_id

    def get_genre(self):
        return self.genre

    def get_BPM(self):
        return self.BPM

