# hog
Generating test files with test data extracted from Word files (containing test or functional descriptions).
In honour of the Hog, which is a beautiful, underappreciated animal, as well as the phrase "go (the) whole hog"

## Installation

Obtain a clone of this repository. The script is using Python which needs to be installed as well as the package manager [pip](https://pip.pypa.io/en/stable/). The latter must be used to install [pipenv](https://pipenv.pypa.io/en/latest/). Use pipenv to install the application dependencies.

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

Hog is a simple and quick and (very) dirty script to:

 - extract Yaml data from a Word document (docx)
 - expand the data into a file based on the [Mako templating engine](https://www.makotemplates.org/)
 - optionally process the data through one or multiple processors, written in Python 3

The basic use case is for hog to serve as a command-line tool to help generation of automatic tests which are specified in the Word documents.

### Basic usage

In the file [resources/spec.docx](resources/spec.docx) an example is shown how to specify the data for tests. The Word document contains three tables: one for the specification of a given data-set, one for expected results and one (optionally) for meta-data. The data needs to be in valid [Yaml](https://yaml.org/). The document is read and parsed and expanded into a source file, based on a template using the syntax of the Mako templating system.

The metadata element "processors" can contain a list of 1 or multiple data processors which process & transform the data read from the Word file (input and output data separately). For an example see [Processnames.py](Processnames.py). The processor need to be "loadable" by Python's module load system.

In the template the data is accesible under three variables:

 - *datain*: the given data
 - *dataout*: the expected result
 - *meta*: optional metadata (None if not given)

### Command line

When running *hog.py* from the command line, the following output is given:

```bash
Usage: hog validate <<DOCX>>
       hog generate <<DOC>> <<TEMPLATE>> <<OUTPUT_FILE>>
```

This shows the two possible options offered by hog:

 - *validate*: validates the Yaml for correctness as contained in the Word document loaded from the path as denoted by *<<DOCX>>*
 - *generate*: generates the *<<OUTPUT_FILE>>* based on the data in the Word Document and the template denoted by *<<TEMPLATE>>*

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
Copyright (c) 2021, Iwan van der Kleijn (iwanvanderkleijn@gmail.com)

This is Free Software: [BSD-3-Clause](https://choosealicense.com/licenses/bsd-3-clause-clear/)

See the file LICENSE.txt
