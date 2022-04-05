
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

if __name__ == "__main__":
    nlp = spacy.load('en_core_web_md')

    arg_ls = sys.argv

    for j in range(len(arg_ls)):
        if arg_ls[j] == "--input":
            filename = arg_ls[j+1]

        if arg_ls[j] == "--names":
            names = arg_ls[j]

        if arg_ls[j] == "--dates":
            dates = arg_ls[j]

        if arg_ls[j] == "--phones":
            phones = arg_ls[j]

        if arg_ls[j] == "--genders":
            genders = arg_ls[j]

        if arg_ls[j] == "--address":
            address = arg_ls[j]

        if arg_ls[j] == "--concept":
            concept = arg_ls[j]
            conceptstr = arg_ls[j+1]

        if arg_ls[j] == "--output":
            wrpath = arg_ls[j+1]

        if arg_ls[j] == "--stats":
            stats1 = arg_ls[j]
            stats1 = stats1[2:]
            outputstr = arg_ls[j+1]


    path = "enroncorpus/"+filename

    files_grabbed = (glob.glob(path))

    print(files_grabbed)

    stats = []

    for i in files_grabbed:
    
        with open(i) as f:
            writefile = i.replace('enroncorpus', '')
            data = f.read()
    
        data2 = data

        if names == "--names":
    
            listname, count1 =  project1.redactname(data2)

        stats.append(count1)
        
        if phones == "--phones":

            listphone, count2 = project1.redactphone(data2)

        stats.append(count2)

        if dates == "--dates":

            listdate, count3 = project1.redactdate(data2)

        stats.append(count3)
    
        if address == "--address":

            listaddress, count4  = project1.redactaddress(data2)

        stats.append(count4)

        listredact = listname + listphone + listdate + listaddress

        for i in range(len(listredact)):
            
            dataredact = nlp(data)
            
            if len(str(dataredact[listredact[i][0]:listredact[i][1]])) > 1:
                data2 = data2.replace(str(dataredact[listredact[i][0]:listredact[i][1]]), "\u2588" *len(str(dataredact[listredact[i][0]:listredact[i][1]])))

        if genders == "--genders":
            data2, count5 = project1.redactgender(data2)

        stats.append(count5)

        if concept == "--concept":
            data2, count6  = project1.redactconcept(data2, conceptstr)

        stats.append(count6)

        if outputstr == "stdout":

            sys.stdout.write( data2 )


        if outputstr == "stderr":
            sys.stderr.write(data2)
    

        writename = writefile + ".redacted"

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

    statsfilename = stats1 +'.txt'

    with open(statsfilename, 'w') as my_list_file:
        my_list_file.writelines("%s\n" % stats for stats in statsreturned)


    for i in range(len(newstats)):

        if outputstr == "stdout":

            sys.stdout.write("Summary Statistics of Redacted Strings: " + '\n')

            sys.stdout.write("Length of Redacted Name String: " + "file " + str(i+1) + ',' + str(newstats[i][0]) +'\n')

            sys.stdout.write("Length of Redacted Phones String: " + "file " +  str(i+1) + ',' + str(newstats[i][1]) +'\n')

            sys.stdout.write("Length of Redacted Dates String: " + "file " + str(i+1) + ',' + str(newstats[i][2])+'\n')

            sys.stdout.write("Length of Redacted Address String: " + "file " + str(i+1) + ',' + str(newstats[i][3])+'\n')

            sys.stdout.write("Length of Redacted Genders String: " + "file " +  str(i+1) + ',' + str (newstats[i][4])+'\n')

            sys.stdout.write("Length of Redacted Concept String: " + "file " + str(i+1) + ',' + str(newstats[i][5])+'\n')

        if outputstr == "stderr":

            sys.stderr.write("Summary Statistics of Redacted Strings: " + '\n')

            sys.stderr.write("Length of Redacted Name String: " + "file " + str(i+1) + ',' + str(newstats[i][0])+'\n')

            sys.stderr.write("Length of Redacted Phones String: " + "file " +  str(i+1) + ',' + str(newstats[i][1])+'\n')

            sys.stderr.write("Length of Redacted Dates String: " + "file " + str(i+1) + ',' + str(newstats[i][2])+'\n')

            sys.stderr.write("Length of Redacted Address String: " + "file " + str(i+1) + ',' + str(newstats[i][3])+'\n')

            sys.stderr.write("Length of Redacted Genders String: " + "file " +  str(i+1) + ',' + str (newstats[i][4])+'\n')

            sys.stderr.write("Length of Redacted Concept String: " + "file " + str(i+1) + ',' + str(newstats[i][5])+'\n')

