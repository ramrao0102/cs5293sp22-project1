import project1

import redactor

import pytest

import os


def test_istheredata():
    
    with open("writepath") as f:

        writelocation = f.readline().rstrip()

    writelocation = str(writelocation)

    obj = os.scandir(writelocation)
    i = 0
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            i = i+1
    print(i)
    assert i >0
