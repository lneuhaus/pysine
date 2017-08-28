from pysine import sine
from time import time


class TestSine(object):

    def test_sine(self):
        for duration in [0.5, 1.0, 2.0, 10.0]:
            t0 = time()
            sine(duration*1000.0, duration)
            t1 = time()
            diff = abs(t1 - t0 -duration)
            assert diff < 0.5