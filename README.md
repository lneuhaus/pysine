# pysine

[![travis status](https://travis-ci.org/lneuhaus/pysine.svg?branch=master "Travisstatus")](https://travis-ci.org/lneuhaus/pysine)
[![code coverage](https://codecov.io/github/lneuhaus/pysine/coverage.svg?branch=master "Code coverage")](https://codecov.io/gh/lneuhaus/pysine)
[![PySine python versions on PyPI](https://img.shields.io/pypi/pyversions/pysine.svg)](https://pypi.python.org/pypi/pysine/)
[![PySine version on PyPI](https://img.shields.io/pypi/v/pysine.svg "PySine on PyPI")](https://pypi.python.org/pypi/pysine/)
[![License](https://img.shields.io/pypi/l/pysine.svg)](https://github.com/lneuhaus/pysine/blob/master/LICENSE)

PySine allows to play single tones on the PyAudio sound output in real time.

This is always useful when no text output is available, for example for
debugging multi-thread programs or calls to object destructors by Python's
garbage collector.


## Installation
Either
```
pip install pysine
```

or

```
cd DESIRED_SOURCE_CODE_DIRECTORY
git clone https://www.github.com/lneuhaus/pysine
cd pysine
python setup.py install
```

## Quick start / usage example:

From the command line:
```
python -m pysine 440.0 3
```
The sound of a 880-Hz sine wave should be heard for a duration of 3 seconds.

Within a python code block:
```
from pysine import sine
sine(frequency=440.0, duration=1.0)  # plays a 1s sine wave at 440 Hz
```

## Issues
Please report all problems or wishes as new issues on [this page](https://github.com/lneuhaus/pysine/issues), so we can fix it and improve the future user experience.

## Unit test
Use nosetests for unit tests:
```
cd PACKAGE_SOURCE_CODE_DIRECTORY
nosetests
```
If there are errors, please report the console output as an issue (see the section “Issues” below for detailed explanations) with as much detail on your test environment (operating system, hardware specifics, ...) as possible.

## License
Please read our license file [LICENSE](https://github.com/lneuhaus/pysine/blob/master/LICENSE) for more information.
