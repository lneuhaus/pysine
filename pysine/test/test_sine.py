from time import time
from pysine import sine
import os

class TestSine(object):

    def test_duration_offset(self):
        for duration in [0.0, 1.0]:
            t0 = time()
            sine(1000, duration)
            t1 = time()
            diff = t1 - t0 - duration
            print(diff)
            assert diff < 1.0, diff

    def test_sine(self):
        # return
        for duration in [0.25, 0.5, 1.0, 2.0]:
            yield self.assert_excess_duration, duration
            yield self.assert_excess_duration_commandline, duration

    def assert_excess_duration(self, duration):
        t0 = time()
        sine(duration*1000.0, duration)
        t1 = time()
        diff = t1 - t0 - duration
        assert diff >= -0.1, diff
        assert diff <= 0.1, diff

    def assert_excess_duration_commandline(self, duration):
        t0 = time()
        os.system("python -m pysine %f %f" % (duration*1000.0, duration))
        t1 = time()
        diff = t1 - t0 - duration
        assert diff >= -0.1, diff
        assert diff <= 1.0, diff
