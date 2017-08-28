from time import time
from pysine import sine


class TestSine(object):

    def test_sine(self):
        for duration in [0.5, 1.0, 2.0, 4.0]:
            yield self.assert_excess_duration, duration

    def assert_excess_duration(self, duration):
        t0 = time()
        sine(duration*1000.0, duration)
        t1 = time()
        diff = t1 - t0 -duration
        assert diff >= -0.1, diff
        assert diff <= 0.1, diff