import scipy.signal as signal

def filterSetting(cutOffFrequency):
    
    fs = 60 # Sampling frequency of the sensor
    fc = cutOffFrequency # Cut-off frequency of the filter
    w = (2*fc / fs) # Normalize the frequency
    b, a = signal.butter(2, w, 'low') # Create filter parameters 
    acc_x_filtered = signal.lfilter(b, a, data)