import sys
from pysine import sine

if __name__ == '__main__':
    if len(sys.argv) > 3:
        print("Wrong number of pysine frequency duration")
    else:
        kwargs = dict()
        if len(sys.argv) > 2:
            kwargs['duration'] = float(sys.argv[2])
        if len(sys.argv) > 1:
            kwargs['frequency'] = float(sys.argv[1])
        print("Calling sine(%s)" % kwargs)
        sine(**kwargs)
