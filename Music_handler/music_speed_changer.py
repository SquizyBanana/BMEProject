import audio_effects as ae
from pydub import AudioSegment
from pydub.playback import play

# Import an audio file
# Format parameter only
# for readability
root = r'Smooth Criminal.wav'
sound = AudioSegment.from_file(root)

def speed_down(sound,
           speed_changes,
           chunk_size=50,
           crossfade=25,
           merge_crossfade=25,
           crossfade_threshold=10):
    sound = sound
    speed_changes = speed_changes
    chunk_size = chunk_size
    crossfade = crossfade
    merge_crossfade = merge_crossfade
    crossfade_threshold = crossfade_threshold

# sound: a pydub AudioSegment instance

# speed_changes: the ratio of the speed to change, 1 means no speed changes,
# < 1 means slow down, for example, 0.5 means half the speed,
# note that this function only works for speed to slow down, if you want to speed up, please use
# the speedup function of pydub, which you pass speed ratio > 1 to speed up the audio

# chunk_size: the chunk size of the audio to be cut in, in ms

# crossfade: the time of fading effects between 2 adjacent chunks when concatenating
# the duplicates of each chunk, in ms

# merge_crossfade: the time of fading effects between 2 adjacent chunks when concatenating
# the chunks after the duplicating process, in ms

# crossfade_threshold: the minimum value of crossfade, in ms


# examples
current_audio = AudioSegment.from_file('Viva La Vida.wav')
speed_change_ratio = 0.7
current_audio_slow_down = ae.speed_down(current_audio, speed_change_ratio)
play(current_audio_slow_down) # listen to the slow down version of the audio