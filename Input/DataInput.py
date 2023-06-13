#import time
from CreaTeBME import SensorManager
import matplotlib.pyplot as plt
from matplotlib import animation
import threading
import numpy
import pandas as pd
import scipy.signal as signal



class Data_Input:

    def __init__(self,sensors):
        self.increment = [0]
        self.TIME_WINDOW = 8
        self.FREQUENCY = 100  # Adjust for sensor
        self.stored_cadence = []
        self.stored_attenuation = []
        self.data_steps = 0

        # Load data
        self.sensors = sensors
        self.test = 0
        self.cutOffFrequency = 15

        fs = 60  # Sampling frequency of the sensor
        fc = self.cutOffFrequency  # Cut-off frequency of the filter
        w = (2 * fc / fs)  # Normalize the frequency
        self.b, self.a = signal.butter(2, w, 'low')  # Create filter parameters

    def start(self, sensors, anibool=False):
        print("Called")
        # Create a sensor manager for the given sensor names using the given callback
        self.sensors = sensors
        self.manager = SensorManager(self.sensors)

        self.dict_keys = ["acc_x", "acc_y", "acc_z", "gyr_x", "gyr_y", "gyr_z"]
        self.stored_values = {}
        for sensor in self.sensors:
            self.stored_values[sensor] = {}
            for i in self.dict_keys:
                self.stored_values[sensor][i] = []


        self.fig, self.ax = plt.subplots(2, len(self.sensors),squeeze=False)
        self.fig.suptitle('Top: Raw acceleration measurements\nBottom: Cadence & Attenuation')

        # Start the sensor manager
        self.manager.start()

        # Only if animation set to true
        if anibool:
            #thread = threading.Thread(target=animation.FuncAnimation, args=(self.fig, self.animate), kwargs=({'interval': 2, 'cache_frame_data' : False}))
            #thread.start()
            self.ani = animation.FuncAnimation(self.fig, self.animate, interval=20, cache_frame_data=False)
            print("Wow, I'm out")
            plt.show()

        # Stop the sensor manager
        # self.manager.stop()

    def run(self):
        self.fetch_measurements()
        #self.data_input.set_measurements()
        values = self.get_values()
        sternum = [values[self.sensors[0]]['acc_x'], values[self.sensors[0]]['acc_y'],values[self.sensors[0]]['acc_z'],[]]
        tibia = [values[self.sensors[1]]['acc_x'], values[self.sensors[1]]['acc_y'],values[self.sensors[1]]['acc_z'],[]]

        # calculate the norm
        for i in range(len(sternum[0])):
            sternum[3].append(numpy.sqrt(sternum[0][i] * sternum[0][i] + sternum[1][i]*sternum[1][i] + sternum[2][i] * sternum[2][i]))
        for i in range(len(tibia[0])):
            tibia[3].append(numpy.sqrt(tibia[0][i] * tibia[0][i] + tibia[1][i] * tibia[1][i] + tibia[2][i] * tibia[2][i]))

        # filter data
        sternum_norm_filtered = signal.lfilter(self.b, self.a, sternum[3])
        tibia_norm_filtered = signal.lfilter(self.b, self.a, tibia[3])
        # find peaks
        peaks_s = signal.find_peaks(sternum_norm_filtered,height=1.5, distance=20)
        peaks_t = signal.find_peaks(tibia_norm_filtered,height= 1.5, distance=20)

        # seperate data for calculation
        peak_s_indecies, peak_s_values = peaks_s
        peak_s_values = peak_s_values["peak_heights"]
        peak_t_indecies, peak_t_values = peaks_t
        peak_t_values = peak_t_values["peak_heights"]
        # print(len(peak_h_indecies))
        peaks_s_corrected = []
        peaks_t_corrected = []

        # filter sternum peaks
        for s in range(len(peak_s_values)):
            for t in range(len(peak_t_values)):
                if 0 < (peak_s_indecies[s] - peak_t_indecies[t]) < 20:
                    peaks_s_corrected.append(peak_s_values[s])
                    peaks_t_corrected.append(peak_t_values[t])
                    break

        norms_t = peaks_t_corrected
        norms_s = peaks_s_corrected
        self.attenuation = float(numpy.mean(numpy.array(norms_s)))/float(numpy.mean(numpy.array(norms_t)))
        self.cadence = len(peaks_s[0])*60/self.TIME_WINDOW

        self.set_cadence_attenuation(self.cadence, self.attenuation)
        return self.attenuation, self.cadence

    def get_data(self):
        return self.attenuation, self.cadence


    def animate(self,i):
        #self.fetch_measurements()
        #self.get_values()

        for col in range(len(self.sensors)):
            for row in range(2):
                self.ax[row, col].clear()
        for s in range(len(self.sensors)):
            for measurement in self.dict_keys[0:3]:
                self.time = numpy.linspace(self.increment[0]/self.FREQUENCY, (len(self.stored_values[self.sensors[s]][measurement])+self.increment[0])/self.FREQUENCY, num=len(self.stored_values[self.sensors[s]][measurement]))
                self.ax[0, s].plot(self.time, self.stored_values[self.sensors[s]][measurement], label = measurement)
                self.ax[0, s].legend(loc = 'upper left')
        self.run()
        cadAt_time = range(len(self.stored_attenuation)) #self.time[(len(self.time)-len(self.stored_cadence))+1:]
        self.ax[1, 0].plot(cadAt_time, self.stored_cadence, label = 'cadence')
        self.ax[1, 1].plot(cadAt_time, self.stored_attenuation, label='attenuaion')
        self.ax[1, 0].legend(loc='upper left')
        self.ax[1, 1].legend(loc='upper left')

    def fetch_measurements(self):
        #print("called")
        measurements = self.manager.get_measurements()
        for sensor, data in measurements.items():
            if not data:
                continue
            else:
                for data_packet in data:
                    for i in range(len(data_packet)):
                        self.stored_values[sensor][self.dict_keys[i]].append(data_packet[i])
                        if len(self.stored_values[sensor][self.dict_keys[i]]) >= self.TIME_WINDOW*self.FREQUENCY:
                            self.stored_values[sensor][self.dict_keys[i]].pop(0)
                            self.increment[0] = self.increment[0] + 1 / (len(data_packet)*len(self.sensors))
       # print(self.stored_values)

    def get_values(self):
        return self.stored_values

    def set_cadence_attenuation(self, cadence, attenuation):
        self.stored_cadence.append(cadence)
        self.stored_attenuation.append(attenuation)
        for array in (self.stored_cadence, self.stored_attenuation):
            if len(array) >= 80:
                array.pop(0)

    def set_measurements(self, stored_values):
        self.stored_values = stored_values