#!/usr/bin/env python3
# Generating test files with test data extracted from Word files (containing test or functional descriptions)
# In honour of the Hog, which is a beautiful, underappreciated animal, as well as the phrase "go (the) whole hog"
# Copyright (c) 2021, Iwan van der Kleijn (iwanvanderkleijn@gmail.com)
# This is Free Software (BSD). See the file LICENSE.txt

from docx import Document
import yaml, importlib
from mako.template import Template
import sys, os

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
        raise ValueError("Test data not present in document")
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
    return mod.process(data)

def error(s):
    print(f"Error: {s}")
    sys.exit()

def quit(s):
    print(s)
    sys.exit()

def unknown(cmd):
    error(f"Unknown command: {cmd}")

def prepare(doc):
    try:
        given, expected, metadata = read_docx(doc)
    except ValueError as ex:
        error(ex)

    given2, expected2, metadata2  = read_yaml(expected, given, metadata)
    if isinstance(given2, yaml.YAMLError):
        error(f"Error in Given input: {given2}")
    elif isinstance(expected2, yaml.YAMLError):
        error(f"Error in expected output: {expected2}")
    elif isinstance(metadata2, yaml.YAMLError):
        error(f"Error in metadata: {metadata2}")
    else:
        if "processors" in metadata2:
            for proc in metadata2["processors"]:
                given2 = process(given2, proc)
                expected2 = process(expected2, proc)

        return {"datain": given2, "dataout": expected2, "meta": metadata2}

def generate(data, template, output):
    template = Template(filename=template)
    r = template.render(**data)
    with open(output, 'w') as f:
        f.write(r)

def usage():
    print("""
Usage: hog validate <<DOCX>>
       hog generate <<DOC>> <<TEMPLATE>> <<OUTPUT_FILE>>
""")

def main():
    try:
        l = len(sys.argv)
        if l == 3:
            env, cmd, doc = sys.argv
            if cmd == "validate":
                data = prepare(os.path.abspath(doc))
                quit(f"Validated!\n{data}")
            else:
                unkown(cmd)
        elif l == 5:
            env, cmd, doc, templ, out = sys.argv
            if cmd == "generate":
                data = prepare(os.path.abspath(doc))
                generate(data, os.path.abspath(templ), os.path.abspath(out))
                quit(f"Output written to {out}")
            else:
                unknown(cmd)
        else:
            usage()
    except Exception as ex:
        error(ex)

if __name__ == "__main__":
    main()
