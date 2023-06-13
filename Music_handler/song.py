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

    def change_speed(self, speed_change_ratio = 1):
        self.speed_change_thread = threading.Thread(target=self.load_speed, args=(speed_change_ratio,))
        self.speed_change_thread.start()
        self.speed_change_thread.join()


    def set_song_segment(self, new_song_segment, new_duration):
        self.song_segment = new_song_segment
        self.duration = new_duration

    def load_speed(self, speed_change_ratio):
        print('Loading started')
        new_song_segment = ae.speed_down(self.song_segment, speed_change_ratio)
        print('Loading ended')
        new_duration = self.song_segment.duration_seconds
        self.set_song_segment(new_song_segment, new_duration)

#TESTING STUFF:
'''
song = Song("Womanizer", "Stef", "5", "rock", 20)
song2 = Song("Viva La Vida","Stef","5","pop",20)
song.play()
song2.change_speed(speed_change_ratio=0.5)
song.stop()
song2.play()
time.sleep(1000)
song2.stop()
#song2.stop()
print("not sven")
'''