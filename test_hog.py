#!/usr/bin/env python3
# Generating test files with test data extracted from Word files (containing test or functional descriptions)
# In honour of the Hog, which is a beautiful, underappreciated animal, as well as the phrase "go (the) whole hog"
# Copyright (c) 2021, Iwan van der Kleijn (iwanvanderkleijn@gmail.com)
# This is Free Software (BSD). See the file LICENSE.txt

import hog, os, pytest, importlib
from yaml import YAMLError, safe_load

docx_file = os.path.join(os.path.dirname(__file__), "resources/spec.docx")
invalid_docx_file = os.path.join(os.path.dirname(__file__), "resources/invalid.docx")
given_file = os.path.join(os.path.dirname(__file__), "resources/given.txt")
expected_file = os.path.join(os.path.dirname(__file__), "resources/expected.txt")
template_file = os.path.join(os.path.dirname(__file__), "resources/template.py")
output_file = os.path.join(os.path.dirname(__file__), "out/pi.py")

def test_data_from_word():
    given_txt = open(given_file).read().strip()
    expected_txt = open(expected_file).read().strip()
    given, expected, metadata = hog.read_docx(docx_file)

    assert given_txt == given
    assert expected_txt == expected
    assert metadata.strip() == "---\n processors: [Processnames]"

def test_yaml_from_word():
    given, expected, metadata= hog.read_docx(docx_file)
    given2, expected2, metadata2  = hog.read_yaml(expected, given, metadata)
    assert given2["ray"] == expected2["ray"]
    assert metadata2["processors"] == ["Processnames"]

def test_processor():
    data = safe_load(open(expected_file).read().strip())

    data2 = hog.process(data, "Processnames")
    assert "frenchHens" in data2
    assert "xmasFifthDay" in data2
    assert "goldenRings" in data2["xmasFifthDay"]
    assert data2["xmasFifthDay"]["partridges"]["location"] == "a pear tree"
    assert data2["callingBirds"][3] == "fred"

def test_generate():
    data = {"pi": 3.14159265359}
    hog.generate(data, template_file, output_file)
    out = importlib.__import__("out")
    from out.pi import Pi
    pi = Pi()
    assert data["pi"] == pi.value

def test_invalid_yaml():
    invalid = "playing_playlist: {{ action }} playlist {{ playlist_name }}"
    given2, expected2, metadata  = hog.read_yaml(invalid, invalid, None)
    assert isinstance(given2, YAMLError)
    assert expected2 is None

def test_invalid_docx():
    with pytest.raises(ValueError):
        given, expected, metadata= hog.read_docx(invalid_docx_file)
