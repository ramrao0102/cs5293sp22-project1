import project1
import pytest


def test_functions():
    f = open("stats11.txt", "r")
    Lines = f.readlines()

    a =[]

    for line in Lines:
        a.append(int(line.strip()))



    assert a[0] > 0
    assert a[1] > 0

    return 0
