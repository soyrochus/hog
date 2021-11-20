#!/usr/bin/env python3
# Generating test files with test data extracted from Word files (containing test or functional descriptions)
# In honour of the Hog, which is a beautiful, underappreciated animal, as well as the phrase "go (the) whole hog"
# Copyright (c) 2021, Iwan van der Kleijn (iwanvanderkleijn@gmail.com)
# This is Free Software (BSD). See the file LICENSE.txt

from docx import Document

def read_docx(path):
    doc = Document(path)
    t1, t2 = doc.tables
    return t1.rows[1].cells[0].text.strip(), t2.rows[1].cells[0].text.strip()

def main():
    pass


if __name__ == "__main__":
    main()
