import numpy as np
from pyaudio import PyAudio

BITRATE = 96000.
PYAUDIO = PyAudio()

def open_stream(bitrate=BITRATE):
    stream = PYAUDIO.open(
            format=PYAUDIO.get_format_from_width(1),
            channels=1,
            rate=int(bitrate),
            output=True)
    return stream

def close_stream(stream):
    stream.stop_stream()
    stream.close()

STREAM = open_stream()

# to terminate stream and pyaudio object
# close_stream(stream)
# PYAUDIO.terminate()




def sine(frequency=440.0, duration=1.0):
    points = int(BITRATE * duration)
    times = np.linspace(0, duration, points, endpoint=False)
    data = np.array((np.sin(times*frequency*2*np.pi) + 1.0)*127.5, dtype=np.int8)
    STREAM.write(data.tostring())
    return
    wavedata=''
    for d in data:
         wavedata += chr(int(d))  # TODO: lookup the right c-function here, extremely inefficient!
    STREAM.write(wavedata)


