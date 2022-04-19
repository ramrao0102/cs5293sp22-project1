import pytest
import project1
import redactor
import numpy
import glob
import re
import nltk
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

def test_phonefunction():
    
    with open("readpath") as f:
        readlocation = f.readline().rstrip()
    
    readlocation = str(readlocation)

    files_grabbed = (glob.glob(readlocation))

    count = 0

    for i in files_grabbed:

        with open(i) as f:
            
            data = f.read()

        data2 = data

        listphone, count4 = project1.redactphone(data2)

        count += count4

    f = open("stats11", "r")
    Lines = f.readlines()

    a =[]

    for line in Lines:
        a.append(int(line.strip()))

    assert count == a[1]

    return 0
