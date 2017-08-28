from pyaudio import PyAudio
from . import logger
try:
    import numpy as np
except:
    logger.warning("Could not load numpy. The program code will be much slower without it. ")
    from math import sin, pi


class PySine(object):
    BITRATE = 96000.

    def __init__(self):
        self.pyaudio = PyAudio()
        try:
            self.stream = self.pyaudio.open(
                format=self.pyaudio.get_format_from_width(1),
                channels=1,
                rate=int(self.BITRATE),
                output=True)
        except:
            logger.error("No audio output is available. Mocking audio stream to simulate one...")
            # output stream simulation with magicmock
            try:
                from mock import MagicMock
            except:  # python > 3.3
                from unittest.mock import MagicMock
            from time import sleep
            self.stream = MagicMock()
            def write(array):
                duration = len(array)/float(self.BITRATE)
                sleep(duration)
            self.stream.write = write

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()

    def sine(self, frequency=440.0, duration=1.0):
        points = int(self.BITRATE * duration)
        try:
            times = np.linspace(0, duration, points, endpoint=False)
            data = np.array((np.sin(times*frequency*2*np.pi) + 1.0)*127.5, dtype=np.int8).tostring()
        except:  # do it without numpy
            data = ''
            omega = 2.0*pi*frequency/self.BITRATE
            for i in range(points):
                data += chr(int(127.5*(1.0+sin(float(i)*omega))))
        self.stream.write(data)

PYSINE = PySine()


def sine(frequency=440.0, duration=1.0):
    return PYSINE.sine(frequency=frequency, duration=duration)


