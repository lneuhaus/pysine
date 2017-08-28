import numpy as np
from pyaudio import PyAudio

BITRATE = 96000.


def sine(frequency=440.0, duration=1.0):
    points = int(BITRATE * duration)
    times = np.linspace(0, duration, points, endpoint=False)
    data = np.sin(times*frequency*2*np.pi)
    data /= np.max(np.abs(data))
    data = (data+1.)/2.
    data *= 255
    wavedata=''
    for d in data:
         wavedata += chr(int(d))  # TODO: lookup the right c-function here, extremely inefficient!
    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1),
                    channels = 1,
                    rate = int(BITRATE),
                    output = True)
    stream.write(wavedata)
    stream.stop_stream()
    stream.close()
    p.terminate()
