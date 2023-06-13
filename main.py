# Code written by Emilie, Fran, Jules, Julia, Nienke and Sven
from Input.DataFilter import Data_filter
from Music_handler.Music_handler import Music_Handler

music_handler = Music_Handler()
data = Data_filter(['6AAE', '7786']) #back, tibia
goal_BPM = 180
data.data_input.start(data.sensors)
song_end = True
noise_level = False
attenuation_treshold = 1.3
#music_handler.loop(138,0.7)


while True:
    attenuation, cadence = data.run()
    music_handler.play_song(cadence+(goal_BPM-cadence)*0.5)
    if attenuation > attenuation_treshold:
        noise_level = True
    else:
        noise_level = False
    music_handler.loop(cadence, noise_level)
    print(cadence)

    #target_BPM = cadence + (goal_BPM - cadence / 10) # subject to change
    #handler.loop(target_BPM,attenuation)