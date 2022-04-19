
import sys

import numpy as np
import glob
import re
import os
import nltk
import spacy
import project1
import os
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from nltk.corpus import wordnet
nltk.download("wordnet")

def readinput():

    arg_ls = sys.argv

    for j in range(len(arg_ls)):
        
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

        if arg_ls[j] == "--stats":
            outputstr = arg_ls[j+1]
                    
    return names, dates, phones, genders, address, concept, conceptstr, outputstr


def readpath():

    arg_ls = sys.argv

    for j in range(len(arg_ls)):

        if arg_ls[j] == "--input":
            filename = arg_ls[j+1]


    readpath = filename

    return readpath

def writepath():

    arg_ls = sys.argv

    for j in range(len(arg_ls)):

        if arg_ls[j] == "--output":
            wrdir = arg_ls[j+1]

    wrdir = wrdir.replace("'", "")

    wrdir = wrdir.replace("/", "")
    
    return wrdir

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
   
if __name__ == "__main__":
    
    nlp = spacy.load('en_core_web_md')

    names, dates, phones, genders, address, concept, conceptstr, outputstr = readinput()

    filename = readpath()

    wrdir = writepath()

    if not os.path.exists(wrdir):

        os.mkdir(wrdir)

    writepathfile = open('writepath', 'w')
    writepathfile.write(wrdir)     

    readpathfile = open('readpath', 'w')
    readpathfile.write(filename)

    files_grabbed = (glob.glob(filename))

    stats = []

    for i in files_grabbed:

        file_name = i

        with open(i) as f:
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

        if concept == "--concept":
            listconcept, count5  = project1.redactconcept(data2, conceptstr)

        stats.append(count5)

        listredact = listname + listphone + listdate + listaddress + listconcept

        for i in range(len(listredact)):
            
            dataredact = nlp(data)
       
            if len(str(dataredact[listredact[i][0]:listredact[i][1]])) > 1:
                data2 = data2.replace(str(dataredact[listredact[i][0]:listredact[i][1]]), "\u2588" *len(str(dataredact[listredact[i][0]:listredact[i][1]])))

        if genders == "--genders":
            data2, count6 = project1.redactgender(data2)

        stats.append(count6)
    
        writepath = wrdir + "/"  + file_name + ".redacted"

        myText = open(writepath,'w')
    
        myText.write(data2)
    
    
    inner_size = 6
    newstats = [ stats[i:i+inner_size] for i in range(0, len(stats), inner_size) ]

    len1, len2, len3, len4, len5, len6 = statistics()

    statsreturned = []
    statsreturned.append(len1)
    statsreturned.append(len2)
    statsreturned.append(len3)
    statsreturned.append(len4)
    statsreturned.append(len5)
    statsreturned.append(len6)

    statsfilename = 'stats11'

    with open(statsfilename, 'w') as my_list_file:
        my_list_file.writelines("%s\n" % stats for stats in statsreturned)

    str1 = 'stdout'
    str1 = str1.lower()

    str2 = 'stderr'
    str2 = str2.lower()

    if outputstr.lower() != str1:
        if outputstr.lower() != str2:

            myfile = open(outputstr, 'w')

            myfile.write(' "Summary Statistics of Redacted Strings: " \n')

            for i in range(len(newstats)):

                myfile.write('File No: ')
                myfile.write('%s\n' %(i+1))

                myfile.write('Length of Redacted Name String: ')
                myfile.write('%s\n' %newstats[i][0])

                myfile.write('Length of Redacted Phone String: ')
                myfile.write('%s\n' %newstats[i][1])

                myfile.write('Length of Redacted Dates String: ')
                myfile.write('%s\n' %newstats[i][2])

                myfile.write('Length of Redacted Address String: ')
                myfile.write('%s\n' %newstats[i][3])

                myfile.write('Length of Redacted Concept String: ')
                myfile.write('%s\n' %newstats[i][4])

                myfile.write('Length of Genders String: ')
                myfile.write('%s\n' %newstats[i][5])

            myfile.close()

   # These below lines are to write a stat file that can be redirected to stdout and stderr   

    myfile1 = open("stats", 'w')

    myfile1.write(' "Summary Statistics of Redacted Strings: " \n')
            
    for i in range(len(newstats)):
                
        myfile1.write('File No: ')
        myfile1.write('%s\n' %(i+1))
                
        myfile1.write('Length of Redacted Name String: ')
        myfile1.write('%s\n' %newstats[i][0])
                
        myfile1.write('Length of Redacted Phone String: ')
        myfile1.write('%s\n' %newstats[i][1])
                
        myfile1.write('Length of Redacted Dates String: ')
        myfile1.write('%s\n' %newstats[i][2])
                
        myfile1.write('Length of Redacted Address String: ')
        myfile1.write('%s\n' %newstats[i][3])
                
        myfile1.write('Length of Redacted Concept String: ')
        myfile1.write('%s\n' %newstats[i][4])
                
        myfile1.write('Length of Genders String: ')
        myfile1.write('%s\n' %newstats[i][5])
           
    myfile1.close()


    if outputstr == "stdout":

        os.system("cat stats > statsstdout")

    if outputstr == "stderr":

        os.system("cat stats > statsstderr 2>&1")

        

