#import time
from CreaTeBME import SensorManager
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy

class Data_Input:

    def __init__(self):
        self.increment = [0]
        self.TIME_WINDOW = 8
        self.FREQUENCY = 100  # Adjust for sensor

    def start(self, sensors):
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


        #self.fig, self.ax = plt.subplots(2, len(self.sensors),squeeze=False)
        #self.fig.suptitle('Accelerometers and gyroscopes')



        # Start the sensor manager
        self.manager.start()

        #self.ani = animation.FuncAnimation(self.fig, self.animate, interval=20)

        #plt.show()

        # Stop the sensor manager
        # self.manager.stop()
    def animate(self,i):
        #print(self.increment)
        self.fetch_measurements()
        for col in range(len(self.sensors)):
            for row in range(2):
                self.ax[row, col].clear()
        for s in range(len(self.sensors)):
            for measurement in self.dict_keys:
                time = numpy.linspace(self.increment[0]/self.FREQUENCY, (len(self.stored_values[self.sensors[s]][measurement])+self.increment[0])/self.FREQUENCY, num=len(self.stored_values[self.sensors[s]][measurement]))
                if measurement in self.dict_keys[0:3]: # If it's acc
                    self.ax[0, s].plot(time, self.stored_values[self.sensors[s]][measurement], label = measurement)
                    self.ax[0, s].legend(loc = 'upper left')
                else:
                    self.ax[1, s].plot(time, self.stored_values[self.sensors[s]][measurement], label = measurement)
                    self.ax[1, s].legend(loc='upper left')

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