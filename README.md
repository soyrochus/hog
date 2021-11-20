# hog
Generating test files with test data extracted from Word files (containing test or functional descriptions)

## Installation

Obtain a clone of this repository
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pipenv](https://pipenv.pypa.io/en/latest/). Use pipenv to install the application dependencies.

```bash
$ pip install pipenv  #install manually dependency
$ pipenv sync         #through pipenv, install the remaining depencies, creating virtualenv

```
## Prerequisites and documentation

 - [Python](https://www.python.org/)
 - [Pipenv](https://pipenv.pypa.io/en/latest/)
 - [PyTest](https://realpython.com/pytest-python-testing/)
 - [python-docx](https://python-docx.readthedocs.io/en/latest/)
 - [Mako](https://www.makotemplates.org/)
 - [Pyyaml](https://pyyaml.org/)

## Usage
### Introduction

...

### Command line

...

### Running Test

Use pytest (installed when running Pipenv sync) to run the included unit tests.

```bash
$ pipenv shell   # activate virtualenv
$ pytest         # run tests
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD-3-Clause](https://choosealicense.com/licenses/bsd-3-clause-clear/)
