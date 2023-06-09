# all the music processing needs to be done before this can be made

from .songPicker import SongPicker
# from .song import Song

class Music_Handler:
    def __init__(self):
        self.song_picker = SongPicker(10000, relativeBPM=False, dataset="Music_handler/Testdataset.csv")

        # self.hum = Song("hum"...) # This will be the track that is added on top

    def play_song(self):
        song = self.song_picker.get_song()
        song.play()
        if song.is_done_playing():
            self.song_picker.next_song()
        # song = self.speedajustment(song)
        # self.song_player.play(song)

    def loop(self,target_BPM, attenuation):
        self.song_picker.adjust_queue(target_BPM)
        #self.noiseadder.addnoise(attenuation)
"""
# Testing stuff
mh = Music_Handler()
mh.play_song()
"""
