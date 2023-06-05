# all the music processing needs to be done before this can be made

from songPicker import SongPicker

class Music_Handler:
    def __init__(self):
        self.song_picker = SongPicker()

    def play_song(self):
        self.song_picker.next_song()
        song = self.song_picker.get_song()
        # song = self.speedajustment(song)
        # self.song_player.play(song)

    def loop(self,target_BPM, attenuation):
        self.song_picker.ajust_queue(target_BPM)
        #self.noiseadder.addnoise(attenuation)



