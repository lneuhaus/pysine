"""
Script to launch pysine from the command line.

Type python -m pysine frequency duration
to generate a sine sound of frequency with duration.
"""
import sys
try:
    from PYSINE import *
except:
    from . import *

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Wrong number of arguments. ")
        print("Usage: python -m pysine frequency duration")
    else:
        frequency = float(sys.argv[1])
        duration = float(sys.argv[2])
        print("Calling sine(frequency=%s, duration=%s)"%(frequency, duration))
        sine(frequency=frequency, duration=duration)
