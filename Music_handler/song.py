# Class song that holds all information about songs (from the table of songs)
# import required libraries
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import pydub.scipy_effects
import time
import threading
import audio_effects as ae

class Song:

    def __init__(self, name, artist, music_id, genre, BPM):
        self.name = name
        self.filename = "Music_handler/MusicFiles/"+name+".wav"
        self.artist = artist
        self.music_id = music_id
        self.genre = genre
        self.BPM = int(BPM)

        self.stop_flag = False
        self.playback = 0

        self.done_playing = True
        self.start_time = 0

        self.song_segment = AudioSegment.from_file(self.filename, format="wav")
        self.duration = self.song_segment.duration_seconds

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

    def play(self, looping = False, speed_change_ratio = 1):
        self.playback = _play_with_simpleaudio(self.song_segment)
        self.thread = threading.Thread(target=self.play_file, kwargs=({'looping': looping}))
        self.thread.start()

    def is_done_playing(self):
        if time.time() > self.start_time+self.duration:
            self.stop()
        return self.done_playing

    def play_file(self, looping = False):
        self.start_time = time.time()
        self.stop_flag = False
        while not self.stop_flag:
            #ae.speed_down(self.song_segment, speed_change_ratio)
            if time.time() > (self.start_time + self.duration) and looping:
                self.playback = _play_with_simpleaudio(self.song_segment)
                self.start_time = time.time()
            elif not looping:
                self.stop_flag = True

    def stop(self): # Call this to stop a song from playing
        self.stop_flag = True
        self.done_playing = True
        self.playback.stop()

    def load_at_speed(self, speed_change_ratio = 1):
        self.song_segment = AudioSegment.from_file(self.filename, format="wav")
        self.duration = self.song_segment.duration_seconds



#TESTING STUFF:
'''
song2 = Song("The Pretender","Stef","5","pop",20)
song2.play(looping=True)
time.sleep(5)

song2.stop()
#song2.stop()
print("not sven")
'''