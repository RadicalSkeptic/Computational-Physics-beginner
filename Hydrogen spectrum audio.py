import scipy.io.wavfile as ad
import numpy as np

rate = 44100
scale = 400
t = np.arange(0, 10, 1/rate)

data = np.zeros([rate*10, 6])

for j in np.arange(0, 6, 1):
    for k in range(1, 10):
        for i in np.arange(0, rate*10, 1):
            f = scale*(1/(j+1)**2-1/(j+1+k)**2)
            data[i, j] += np.sin(2*np.pi*f*i/rate)

ad.write("e:/MyCodes/Hwave.wav", rate, data.astype(np.float32))
