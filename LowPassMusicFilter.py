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

thousand_miles_away = AudioSegment.from_file("10,000 Miles Away.wav", format="wav")
hum = AudioSegment.from_file("hum.wav", format="wav")
unaltered_song = AudioSegment.from_file("Hollaback Girl.wav", format="wav")
song_with_filter = AudioSegment.low_pass_filter(unaltered_song, 400, order=3)  # order 3 is nice

first_10_sec = unaltered_song[:10 * 1000]  # first 10 sec of song
print(first_10_sec.duration_seconds)  # prints duration of certain song
# play(song_with_filter)
# make threads
EpochTime = time.time()
attenuation = True
volume1 = 20
# volume2 = -40

fade_unaltered_song = unaltered_song.fade_in(10000).fade_out(5000)
song_with_filter += volume1
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
    attenuation = attenuation_array[random.randint(0, 2)
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

#
# end_time = start_time_song + 5
# while True:
#     current_time = time.time()
#     print("curr time: ", current_time)
#     # print("end time:  ", end_time)
#     if current_time >= end_time:
#         t2 = threading.Thread(target=play, args=(hum[1000:6000],))
#         t2.start()
#         break
#
# end_time = start_time_song + 10
#
# while True:
#     current_time = time.time()
#     print("curr time: ", current_time)
#     # print("end time:  ", end_time)
#     if current_time >= end_time:
#         t2 = threading.Thread(target=play, args=(hum[1000:6000].overlay(unaltered_song),))
#         t2.start()
#         break


# def play_song_per_segment(segments, volume_index):
#     for segment in segments:
#         volume = volume1 if volume_index == 1 else volume2
#         play(segment - volume)
#
#
# def song_splitter():
#     segments = []
#     for i in range(0, len(first_10_sec), 1 * 1000):
#         segments.append(first_10_sec[i:i+1*1000])
#     # segements_unaltered_song = first_10_sec[::1 * 1000]
#     # print(segements_unaltered_song)
#     # play(segements_unaltered_song[0])
#     # segements_song_with_filtered = unaltered_song[::1 * 1000]
#     t1 = threading.Thread(target=play_song_per_segment, args=(segments,), kwargs={'volume_index': 1})
#     # t2 = threading.Thread(target=play_song_per_segment, args=(segements_song_with_filtered,),
#     #                       kwargs={'volume_index': 2})
#     t1.start()
#     # t2.start()
#
#
# song_splitter()


# while t2.is_alive():
#     print(time.time()-EpochTime)
#     if time.time() - EpochTime > 15:  #if 5 seconds have passed
#         print("time has passed")
#         if attenuation:
#             volume = 40
#             t2 = threading.Thread(target=play, args=(unaltered_song - volume,))
#             print("volume is altered")


# t1.join()  # only after the two threads t1 & t2 are finished the rest of the code is run
# t2.join()
print("song has been played")

# start_time_song = time.time()
# print(start_time_song)
# USE THREADING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# use for loop for duration song in sec
# check every .. sec if the low pass filter should be applied
# if true and not already applied
# overlay the low pass filter with the normal song and make
# the volume normal song lower and the volume of the filter part the original volume
# if false and alreay applied
# make the low pass filter volume lower and take it out after a few sec and
# make the normal song volume again the original volume
