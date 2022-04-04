import pytest
import project1
import numpy
import glob
import re
import nltk
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

def test_datefunction():
    
    path = "enroncorpus/"+ "*.txt"

    files_grabbed = (glob.glob(path))

    count = 0

    for i in files_grabbed:

        with open(i) as f:
            writefile = i.replace('enroncorpus', '')
            data = f.read()

        data2 = data

        data2, count4 = project1.redactdate(data2)

        count += count4

    f = open("stats.txt", "r")
    Lines = f.readlines()

    a =[]

    for line in Lines:
        a.append(int(line.strip()))

    assert count == a[3]

    return 0
