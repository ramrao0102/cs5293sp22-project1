
import sys

import numpy as np
import glob
import re
import nltk
import spacy
import project1
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from nltk.corpus import wordnet
nltk.download("wordnet")


nlp = spacy.load('en_core_web_md')

filename = sys.argv[2]
names = sys.argv[3]
dates = sys.argv[4]
phones = sys.argv[5]
genders = sys.argv[6]
address = sys.argv[7]
concept = sys.argv[8]
stat = sys.argv[12]
conceptstr = sys.argv[9]
outputstr = sys.argv[13]


path = "/home/ramrao0102/project1/enroncorpus/"+filename


wrpath = sys.argv[11]

files_grabbed = (glob.glob(path))

print(files_grabbed)

stats = []

for i in files_grabbed:
    
    with open(i) as f:
        writefile = i.replace('home/ramrao0102/project1/enroncorpus', '')
        data = f.read()
    
    data2 = data

    if names == "--names":
    
        data2, count1 =  project1.redactname(data2)

    stats.append(count1)

    if genders == "--genders":
        data2, count2 = project1.redactgender(data2)
        
    stats.append(count2)

    if phones == "--phones":
        data2, count3 = project1.redactphone(data2)

    stats.append(count3)

    if dates == "--dates":
        data2, count4 = project1.redactdate(data2)

    stats.append(count4)
    
    if address == "--address":
        data2, count5  = project1.redactaddress(data2)

    stats.append(count5)

    if concept == "--concept":
        data2, count6  = project1.redactconcept(data2, conceptstr)

    stats.append(count6)


    if outputstr == "stdout":

        sys.stdout.write( data2 )


    if outputstr == "stderr":
        sys.stderr.write(data2)
    

    writename = writefile + "redacted"

    writepath = wrpath + "/"+ writename 

    myText = open(writepath,'w')
    
    myText.write(data2)
    
    
inner_size = 6
newstats = [ stats[i:i+inner_size] for i in range(0, len(stats), inner_size) ]


def statistics():

    len1 =0
    len2 =0
    len3 =0
    len4 =0
    len5 =0
    len6 =0
    
    for i in range(len(newstats)):
        len1 += newstats[i][0]

        len2 += newstats[i][1]

        len3 += newstats[i][2]

        len4 += newstats[i][3]

        len5 += newstats[i][4]

        len6 += newstats[i][5]



    return len1, len2, len3, len4, len5, len6


len1, len2, len3, len4, len5, len6 = statistics()

statsreturned = []
statsreturned.append(len1)
statsreturned.append(len2)
statsreturned.append(len3)
statsreturned.append(len4)
statsreturned.append(len5)
statsreturned.append(len6)

with open('stats.txt', 'w') as my_list_file:
    my_list_file.writelines("%s\n" % stats for stats in statsreturned)


for i in range(len(newstats)):

    if outputstr == "stdout":

        sys.stdout.write("Summary Statistics of Redacted Strings: " + '\n')

        sys.stdout.write("Length of Redacted Name String: " + "file " + str(i+1) + ',' + str(newstats[i][0]) +'\n')

        sys.stdout.write("Length of Redacted Genders String: " + "file " +  str(i+1) + ',' + str(newstats[i][1]) +'\n')

        sys.stdout.write("Length of Redacted Phones String: " + "file " + str(i+1) + ',' + str(newstats[i][2])+'\n')

        sys.stdout.write("Length of Redacted Dates String: " + "file " + str(i+1) + ',' + str(newstats[i][3])+'\n')

        sys.stdout.write("Length of Redacted Address String: " + "file " +  str(i+1) + ',' + str (newstats[i][4])+'\n')

        sys.stdout.write("Length of Redacted Concept String: " + "file " + str(i+1) + ',' + str(newstats[i][5])+'\n')

    if outputstr == "stderr":

        sys.stderr.write("Summary Statistics of Redacted Strings: " + '\n')

        sys.stderr.write("Length of Redacted Name String: " + "file " + str(i+1) + ',' + str(newstats[i][0])+'\n')

        sys.stderr.write("Length of Redacted Genders String: " + "file " +  str(i+1) + ',' + str(newstats[i][1])+'\n')

        sys.stderr.write("Length of Redacted Phones String: " + "file " + str(i+1) + ',' + str(newstats[i][2])+'\n')

        sys.stderr.write("Length of Redacted Dates String: " + "file " + str(i+1) + ',' + str(newstats[i][3])+'\n')

        sys.stderr.write("Length of Redacted Address String: " + "file " +  str(i+1) + ',' + str (newstats[i][4])+'\n')

        sys.stderr.write("Length of Redacted Concept String: " + "file " + str(i+1) + ',' + str(newstats[i][5])+'\n')

