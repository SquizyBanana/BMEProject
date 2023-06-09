# A class for creating a queue of songs to be played.

import csv
from song import Song

class SongPicker:

    def __init__(self, BPM_fit_margin = 20, relativeBPM = False, dataset="dataset music.csv"):
        self.csv_file_name = dataset
        self.song_array = []
        self.read_csv()

        self.BPM_fit_margin = BPM_fit_margin
        self.relativeBPM = relativeBPM  # Make true if the margin of when to pick a song is relative

        self.song_queue = []

    def __str__(self): # This is just a method that is called if the class put in a print() function
        printout_string = ""
        for song in self.song_queue:
            printout_string += song.name + " " + str(song.BPM) + "\n"
        return printout_string

    def read_csv(self):  # Sets up the array of instances of class Song, information read from the table
        with open(self.csv_file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.song_array.append(Song(row[0], row[1], row[2], row[3], row[4]))
                    line_count += 1

    def pick_suiting_songs(self, target_BPM = 180):  # Updates the array of songs that could be played at target BPM
        suiting_song_array = []
        for song in self.song_array:
            if not self.relativeBPM:
                if abs(song.get_BPM() - target_BPM) < self.BPM_fit_margin:
                    suiting_song_array.append(song)
            else:
                if abs(song.get_BPM() - target_BPM) < self.BPM_fit_margin * target_BPM:
                    suiting_song_array.append(song)
        return suiting_song_array

    def place_in_order(self, song, targetBPM = 180): # Places new songs into the queue at a correct place
        if len(self.song_queue)>0:
            i = 0
            while (abs(song.get_BPM()-targetBPM) > abs(self.song_queue[i].BPM-targetBPM)):
                i += 1
            self.song_queue.insert(i,song)
        else:
            self.song_queue.append(song)

    def adjust_queue(self, target_BPM): # Removes songs that do not fit the BPM and adds ones that do, in order of fitness
        suiting_song_array = self.pick_suiting_songs(target_BPM)
        i=0
        while i < len(self.song_queue):
            if self.song_queue[i] not in suiting_song_array:
                self.song_queue.pop(i)
            else:
                i+=1
        for song in suiting_song_array:
            if song not in self.song_queue:
                self.place_in_order(song, target_BPM)

    def get_queue(self): # Returns an array that is the queue of songs
        return self.song_queue

    def get_song(self): # Use this one to get the first song of the queue
        return self.song_queue[0]

    def next_song(self): # Moves a song from the beginning of the queue to the end
        self.song_queue.append(self.song_queue[0])
        self.song_queue.pop(0)
