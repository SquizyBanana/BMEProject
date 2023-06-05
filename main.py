# Code written by Emilie, Fran, Jules, Julia, Nienke and Sven
from DataFilter import Data_filter
from Music_handler import Music_Handler

handler = Music_Handler()
data = Data_filter(['6AAE', '7786'])
goal_BPM = 180
data.data_input.start(data.sensors)
song_end = True
while True:
    attenuation, cadence = data.run()
    print("-----------------------------------------------------------------------------------------------------------------")
    print(attenuation)
    print(cadence)
    if song_end:
        handler.play_song()
    target_BPM = cadence + (goal_BPM - cadence / 10) # subject to change
    handler.loop(target_BPM,attenuation)