import numpy as np
from pyaudio import PyAudio


class PySine(object):
    BITRATE = 96000.

    def __init__(self):
        self.pyaudio = PyAudio()
        self.stream = self.pyaudio.open(
                format=self.pyaudio.get_format_from_width(1),
                channels=1,
                rate=int(self.BITRATE),
                output=True)

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()

    def sine(self, frequency=440.0, duration=1.0):
        points = int(self.BITRATE * duration)
        times = np.linspace(0, duration, points, endpoint=False)
        data = np.array((np.sin(times*frequency*2*np.pi) + 1.0)*127.5, dtype=np.int8)
        self.stream.write(data.tostring())

PYSINE = PySine()


def sine(frequency=440.0, duration=1.0):
    return PYSINE.sine(frequency=frequency, duration=duration)


