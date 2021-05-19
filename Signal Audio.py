import scipy.io.wavfile as ad
import numpy as np

rate = 44100
frequency = 10000
t = np.arange(0, 5, 1/rate)
data = 32767*np.sin(2*np.pi*frequency*t)

ad.write("e:/MyCodes/sine wave.wav", rate, data.astype(np.int16))
