import soundcard as sc
import matplotlib.pyplot as plt
import numpy as np

mics = sc.all_microphones(include_loopback=True)
default_mic = mics[3]
print(default_mic.name)
for mic in mics:
    print(mic.name)

with default_mic.recorder(samplerate=48000) as mic:
    data = mic.record(5 * 48000)

x = np.arange(0, len(data), 1)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, data, 'y')

plt.show()
print(data.shape)