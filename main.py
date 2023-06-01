# Code written by Emilie, Fran, Jules, Julia, Nienke and Sven
from DataFilter import Data_filter

data = Data_filter(['6AAE', '7786'])
data.data_input.start(data.sensors)
while True:
    attenuation, cadence = data.run()
    print("-----------------------------------------------------------------------------------------------------------------")
    print(attenuation)
    print(cadence)