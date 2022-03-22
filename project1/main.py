
import sys
import pandas
import numpy
import glob
import re
import nltk
import spacy
import project1
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher



filename = sys.argv[2]
names = sys.argv[3]
dates = sys.argv[4]
phones = sys.argv[5]
genders = sys.argv[6]
address = sys.argv[7]
concept = sys.argv[8]
stat = sys.argv[11]

print(names)
print(type(names))

path = "/home/ramrao0102/project1/enroncorpus/"+filename

nlp = spacy.load('en_core_web_md')

wrpath = sys.argv[11]

files_grabbed = (glob.glob(path))

print(files_grabbed)


for i in files_grabbed:
    with open(i) as f:
        writefile = i.replace('home/ramrao0102/project1/enroncorpus', '')
        data = f.read()
    
    data2 = data

    if names == "--names":
        data2, count1 =  project1.redactname(data2)
    

    if genders == "--genders":
        data2, count2 = project1.redactgender(data2)


    if phones == "--phones":
        data2, count3 = project1.redactphone(data2)


    if dates == "--dates":
        data2, count4 = project1.redactdate(data2)

    
    if address == "--address":
        data2, count5  = project1.redactaddress(data2)


    if concept == "--concept":
        data2, count6  = project1.redactconcept(data2)

    print(data2)

    print("Length of Redacted Name String:", count1)

    print("Length of Redacted Genders String:", count2)

    print("Length of Redacted Phones String:", count3)

    print("Length of Redacted Dates String:", count4)

    print("Length of Redacted Address String:", count5)

    print("Length of Redacted Concept String:", count6)

    writename = writefile + "redacted"

    writepath = wrpath + "/"+ writename 

    myText = open(writepath,'w')
    
    myText.write(data2)
    
    
    

