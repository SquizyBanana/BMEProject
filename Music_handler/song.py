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
        self.filename = "MusicFiles/"+name+".wav"
        self.artist = artist
        self.music_id = music_id
        self.genre = genre
        self.BPM = int(BPM)

        self.thread = threading.Thread(target=self.loop_file)
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
        self.start_time = 0
        if looping:
            self.thread.start()
        else:
            #ae.speed_down(self.song_segment, speed_change_ratio)
            self.playback = _play_with_simpleaudio(self.song_segment)

    def done_playing(self):
        if time.time() > self.start_time+self.duration:
            self.stop()
        return self.done_playing

    def loop_file(self, speed_change_ratio = 1): # DO NOT CALL THIS (It is called when looping is set to True in the play method)
        self.stop_flag = False
        #song_segment = AudioSegment.from_file(self.filename, format="wav")
        while not self.stop_flag:
            #ae.speed_down(self.song_segment, speed_change_ratio)
            if time.time() > (self.start_time + self.duration):
                self.playback = _play_with_simpleaudio(self.song_segment)
                self.start_time = time.time()

    def stop(self): # Call this to stop a song from playing
        self.stop_flag = True
        self.done_playing = True
        self.playback.stop()


#TESTING STUFF:
'''
song2 = Song("The Pretender","Stef","5","pop",20)
song2.play()
time.sleep(5)

song2.stop()
#song2.stop()
print("not sven")
'''