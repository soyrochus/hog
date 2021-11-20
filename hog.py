#!/usr/bin/env python3
# Generating test files with test data extracted from Word files (containing test or functional descriptions)
# In honour of the Hog, which is a beautiful, underappreciated animal, as well as the phrase "go (the) whole hog"
# Copyright (c) 2021, Iwan van der Kleijn (iwanvanderkleijn@gmail.com)
# This is Free Software (BSD). See the file LICENSE.txt

from docx import Document
import yaml, importlib
from mako.template import Template

def read_docx(path):
    doc = Document(path)

    given = None
    expected = None
    metadata = None

    for t in doc.tables:
        label = t.rows[0].cells[0].text.strip()
        value = t.rows[1].cells[0].text.strip()
        if label == "Given input":
            given = value
        elif label == "Expected output":
            expected = value
        elif label == "Metadata":
            metadata = value

    if given is None or expected is None:
        raise ValueError("Test data not provided")
    return (given, expected, metadata)

def read_yaml(given, expected, metadata=None):
    given_res = None
    expected_res = None
    try:
        given_res = yaml.safe_load(given)
        expected_res = yaml.safe_load(expected)
        metadata_res = yaml.safe_load(metadata) if not metadata is None else None
        return (given_res, expected_res, metadata_res)
    except yaml.YAMLError as ex:
        if given_res is None:
            return (ex, None, None)
        elif metadata_data is None:
            return (given_res, ex, None)
        else:
            return (given_res, expected_res, ex)

def process(data, processor):
    mod = importlib.__import__(processor)
    _data =  mod.process(data)
    print(_data)
    return _data

def generate(data, template, output):
    template = Template(filename=template)
    with open(output, 'w') as f:
        f.write(template.render(**data))

def main():
    pass

if __name__ == "__main__":
    main()
