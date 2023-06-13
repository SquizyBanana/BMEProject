import matplotlib.pyplot as plt
import pandas as pd
import numpy
import scipy.signal as signal

from .DataInput import Data_Input
class Data_filter:

    def __init__(self,sensors):
        self.data_input = Data_Input()
        # Load data
        self.sensors = sensors
        self.test = 0
        self.cutOffFrequency = 15

        fs = 60  # Sampling frequency of the sensor
        fc = self.cutOffFrequency  # Cut-off frequency of the filter
        w = (2 * fc / fs)  # Normalize the frequency
        self.b, self.a = signal.butter(2, w, 'low')  # Create filter parameters

    def run(self):
        #df_tibia['norm'] = numpy.sqrt(df_tibia['acc_x']*df_tibia['acc_x'] + df_tibia['acc_y']*df_tibia['acc_y'] + df_tibia['acc_z']*df_tibia['acc_z'])
        # df_head['norm'] = numpy.sqrt(df_head['acc_x']*df_head['acc_x'] + df_head['acc_y']*df_head['acc_y'] + df_head['acc_z']*df_head['acc_z'])
        #self.data_input.animate(1)
        self.data_input.fetch_measurements()
        values = self.data_input.get_values()
        sternum = [values[self.sensors[0]]['acc_x'],values[self.sensors[0]]['acc_y'],values[self.sensors[0]]['acc_z'],[]]
        tibia = [values[self.sensors[1]]['acc_x'],values[self.sensors[1]]['acc_y'],values[self.sensors[1]]['acc_z'],[]]

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
        attenuation = float(numpy.mean(numpy.array(norms_s)))/float(numpy.mean(numpy.array(norms_t)))
        cadence = len(peaks_s[0])*60/self.data_input.TIME_WINDOW
        return attenuation, cadence




