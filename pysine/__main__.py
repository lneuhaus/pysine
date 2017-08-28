"""
Script to launch pysine from the command line.

Type python -m pysine frequency duration
to generate a sine sound of frequency with duration.
"""

import sys
try:
    from pysine import *
except:
    from . import *

if __name__ == '__main__':
    if len(sys.argv) > 3:
        print("Wrong number of arguments. ")
        print("Usage: python -m pysine frequency duration")
    else:
        kwargs = dict()
        if len(sys.argv) > 2:
            kwargs['duration'] = float(sys.argv[2])
        if len(sys.argv) > 1:
            kwargs['frequency'] = float(sys.argv[1])
        print("Calling sine(%s)" % kwargs)
        sine(**kwargs)

