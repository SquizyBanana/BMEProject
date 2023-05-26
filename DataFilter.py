import matplotlib.pyplot as plt
import pandas as pd
import numpy
import scipy.signal as signal
from DataInput import Data_Input

class Data_filter:

    def __init__(self):
        self.data_input = Data_Input()
        # Load data
        self.sensors = ['6AAE', '7786']
    def run(self):
        #df_tibia['norm'] = numpy.sqrt(df_tibia['acc_x']*df_tibia['acc_x'] + df_tibia['acc_y']*df_tibia['acc_y'] + df_tibia['acc_z']*df_tibia['acc_z'])
        # df_head['norm'] = numpy.sqrt(df_head['acc_x']*df_head['acc_x'] + df_head['acc_y']*df_head['acc_y'] + df_head['acc_z']*df_head['acc_z'])

        self.data_input.fetch_measurements()
        values = self.data_input.get_values()
        sternum = [values[self.sensors[0]]['acc_x'],values[self.sensors[0]]['acc_y'],values[self.sensors[0]]['acc_z'],[]]
        tibia = [values[self.sensors[1]]['acc_x'],values[self.sensors[1]]['acc_y'],values[self.sensors[1]]['acc_z'],[]]
        print(sternum)
        print(tibia)
        for i in range(len(sternum[0])):
            print("sternum" + str(i))
            sternum[3][i] = numpy.sqrt(sternum[0][i]*sternum[0][i] + sternum[1][i]*sternum[1][i] + sternum[2][i]*sternum[2][i])
        for i in range(len(tibia[0])):
            print("tibia"+ str(i))
            tibia[3][i] = numpy.sqrt(tibia[0][i] * tibia[0][i] + tibia[1][i] * tibia[1][i] + tibia[2][i] * tibia[2][i])




        #find peaks
        peaks_l = signal.find_peaks(sternum[0],1, distance=300)
        peaks_h = signal.find_peaks(tibia[0],1, distance=150)

        #seperate data for calculation
        peak_h_indecies, peak_h_values = peaks_h
        peak_h_values = peak_h_values["peak_heights"]
        peak_l_indecies, peak_l_values = peaks_l
        peak_l_values = peak_l_values["peak_heights"]
        # print(len(peak_h_indecies))
        peaks_h_corrected = []
        peaks_l_corrected = []

        #filter head peaks
        for h in range(len(peak_h_values)):
            for l in range(len(peak_l_values)):
                if 0 < (peak_h_indecies[h] - peak_l_indecies[l]) < 150:
                    peaks_h_corrected.append(peak_h_values[h])
                    peaks_l_corrected.append(peak_l_values[l])
                    break

        norms_t = peaks_l_corrected
        norms_h = peaks_h_corrected
        #print(float(numpy.mean(numpy.array(norms_h)))/float(numpy.mean(numpy.array(norms_t))))

programm = Data_filter()
programm.data_input.start(programm.sensors)
while True:
    programm.run()