#!/usr/bin/env python3
# Generating test files with test data extracted from Word files (containing test or functional descriptions)
# In honour of the Hog, which is a beautiful, underappreciated animal, as well as the phrase "go (the) whole hog"
# Copyright (c) 2021, Iwan van der Kleijn (iwanvanderkleijn@gmail.com)
# This is Free Software (BSD). See the file LICENSE.txt

import hog, os

docx_file = os.path.join(os.path.dirname(__file__), "resources/spec.docx")
given_file = os.path.join(os.path.dirname(__file__), "resources/given.txt")
expected_file = os.path.join(os.path.dirname(__file__), "resources/expected.txt")


def test_data_from_word():
    given_txt = open(given_file).read().strip()
    expected_txt = open(expected_file).read().strip()
    given, expected = hog.read_docx(docx_file)

    assert given_txt == given
    assert expected_txt == expected
