# all the music processing needs to be done before this can be made

from .songPicker import SongPicker
from .song import Song

class Music_Handler:
    def __init__(self):
        self.song_picker = SongPicker(10000, relativeBPM=False, dataset="Music_handler/database music 2.csv") # !!!!!!! remove , relativeBPM=False, dataset="Music_handler/Testdataset.csv" and change the accepted range when done!
        self.noise = Song('hum','hum',100,'hum',0)
        # self.hum = Song("hum"...) # This will be the track that is added on top

    def play_song(self, target_BPM):
        self.song_picker.adjust_queue(target_BPM=target_BPM)
        song = self.song_picker.get_song()
        if not song.is_playing:
            song.play()
        if song.is_done_playing():
            self.song_picker.next_song()
        # song = self.speedajustment(song)
        # self.song_player.play(song)

    def loop(self,target_BPM, noise_level):
        self.song_picker.adjust_queue(target_BPM)

        if noise_level and not self.noise.is_playing:
            self.noise.play(looping=True)
        elif not noise_level and self.noise.is_playing:
            self.noise.stop()




# Testing stuff

'''mh = Music_Handler()
mh.play_song()
a = 0
while True:
    a = a'''

