# from playsound import playsound
# from pedalboard import AudioFile #lets you excess the audiofile and alter it
#
# #play a music file:
# playsound('Bad Romance.mp3')
import random

# # import required libraries
from pydub import AudioSegment
from pydub.playback import play
import pydub.scipy_effects
import time
import threading

thousand_miles_away = AudioSegment.from_file("hum.wav", format="wav")
hum = AudioSegment.from_file("hum.wav", format="wav")
unaltered_song = AudioSegment.from_file("hum.wav", format="wav")
#song_with_filter = AudioSegment.low_pass_filter(unaltered_song, 400, order=3)  # order 3 is nice

first_10_sec = unaltered_song[:10 * 1000]  # first 10 sec of song
print(first_10_sec.duration_seconds)  # prints duration of certain song
# play(song_with_filter)
# make threads
EpochTime = time.time()
attenuation = True
volume1 = 20
# volume2 = -40

fade_unaltered_song = unaltered_song.fade_in(10000).fade_out(5000)
#song_with_filter += volume1
start_time_song = time.time()
t1 = threading.Thread(target=play, args=(unaltered_song,))
# play(thousand_miles_away[:5000].overlay(fade_unaltered_song))
t1.start()



thread_is_not_alive = True
song_not_finished = True
hum_array = []
attenuation_array = [True, False]
while song_not_finished:
    # get boolean of attenuation VVVV did it now with an array
    attenuation = attenuation_array[random.randint(0, 1)
]
    if attenuation:
        if len(hum_array) == 0:
            hum_array.append(threading.Thread(target=play, args=(hum[1000:6000],)))
            # t2 = threading.Thread(target=play, args=(hum[1000:6000],))
            # t2.start()
            hum_array[0].start()
        else:
            if not hum_array[0].is_alive():
                hum_array.pop(0)

