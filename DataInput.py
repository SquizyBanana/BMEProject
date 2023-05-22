import time
from CreaTeBME import SensorManager
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy


def animate(i):
    print(increment)
    fetch_measurements()
    acc.clear()
    gyro.clear()
    for sensor in sensors:
        for measurement in dict_keys:
            time = numpy.linspace(increment[0]/FREQUENCY, (len(stored_values[sensor][measurement])+increment[0])/FREQUENCY, num=len(stored_values[sensor][measurement]))
            if measurement in dict_keys[0:3]:
                acc.plot(time, stored_values[sensor][measurement], label = measurement)
                acc.legend(loc = 'upper left')
            else:
                gyro.plot(time, stored_values[sensor][measurement], label = measurement)
                gyro.legend(loc='upper left')

def fetch_measurements():
    measurements = manager.get_measurements()
    for sensor, data in measurements.items():
        if not data:
            continue
        else:
            for data_packet in data:
                for i in range(len(data_packet)):
                    stored_values[sensor][dict_keys[i]].append(data_packet[i])
                    if len(stored_values[sensor][dict_keys[i]]) >= TIME_WINDOW*FREQUENCY:
                        stored_values[sensor][dict_keys[i]].pop(0)
                        increment[0] = increment[0] + 1 / (len(data_packet)*len(sensors))

    print(stored_values)

# Create a sensor manager for the given sensor names using the given callback
sensors = ['6DE2']
manager = SensorManager(sensors)

dict_keys = ["acc_x", "acc_y", "acc_z", "gyr_x", "gyr_y", "gyr_z"]
stored_values = {}
for sensor in sensors:
    stored_values[sensor] = {}
    for i in dict_keys:
        stored_values[sensor][i] = []

fig, (acc, gyro) = plt.subplots(2)
fig.suptitle('Accelerometer and gyroscope')


increment = [0]
TIME_WINDOW = 20
FREQUENCY = 100 #adjust for sensor

# Start the sensor manager
manager.start()

ani = animation.FuncAnimation(fig, animate, interval = 20)

plt.show()

# Stop the sensor manager
manager.stop()