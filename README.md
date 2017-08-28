# pysine

[![travis status](https://travis-ci.org/lneuhaus/pysine.svg?branch=master "Travisstatus")](https://travis-ci.org/lneuhaus/pysine)
[![code coverage](https://codecov.io/github/lneuhaus/pysine/coverage.svg?branch=master "Code coverage")](https://codecov.io/gh/lneuhaus/pysine)
[![PySine versions on PyPI](https://img.shields.io/pypi/pyversions/pysine.svg)](https://pypi.python.org/pypi/pysine/)
[![PySine version on PyPI](https://img.shields.io/pypi/v/pysine.svg "PySine on PyPI")](https://pypi.python.org/pypi/pysine/)
[![Download pyrpl](https://img.shields.io/sourceforge/dm/pysine.svg)](https://sourceforge.net/projects/pysine/files/latest/download)
[![Documentation Status](https://readthedocs.org/projects/pysine/badge/?version=latest)](http://pysine.readthedocs.io/en/latest/?badge=latest)
[![join chat on gitter](https://badges.gitter.im/JoinChat.svg "Join chat on gitter")](https://gitter.im/lneuhaus/pysine)
[![License](https://img.shields.io/pypi/l/pysine.svg)](https://github.com/lneuhaus/pysine/blob/master/LICENSE)

PySine allows to play single tones on the PyAudio sound output in real time



## Installation
Either
```
pip install pysine
```

or

```
cd DESIRED_SOUCE_CODE_DIRECTORY
git clone hyyps://www.github.com/lneuhaus/pysine
python setup.py develop
```

## Quick start
```
python -m pysine frequency duration
```
A sine sound with the desired properties should be heard.

## Issues
Please report all problems or wishes as new issues on [this page](https://github.com/lneuhaus/pysine/issues), so we can fix it and improve the future user experience.

## Unit test
Use nosetests for unit tests:
```
cd package_code_directory
nosetests
```
All tests should take about 3 minutes and finish without failures or errors. If there are errors, please report the console output as an issue (see the section "Issues" below for detailed explanations).

## License
Please read our license file [LICENSE](https://github.com/lneuhaus/pysine/blob/master/LICENSE) for more information.
