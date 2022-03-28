import project1

import pytest

import os


def test_istheredata():
    path = "enroncorpus/write1"
    obj = os.scandir(path)
    i = 0
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            i = i+1
    print(i)
    assert i >0
