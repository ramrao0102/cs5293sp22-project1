
import sys
import pandas
import numpy
import glob
import re
import nltk
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_md')

def redactname(data2):
    
    data1 = nlp(data2)

    count1 =0

    for ent in data1.ents:
        if (ent.label_ == "PERSON"):
            data2 = data2.replace(ent.text, "\u2588" *len(ent.text))
    
            count1 += len(ent.text)    

    return data2, count1


def redactgender(data2):

    data11 = nlp(data2)

    gender = ["he", "him", "her", "she", "He", "She", "Him", "Her"]

    count2 = 0
    
    for item in gender:
   
        for token in data11:
        
            str1 = str(token.text)
                
            if item.lower() == str1.lower():
           
                pattern =  "\\" + "b" + item + "\\" + "b"
                data2 = re.sub(pattern, "\u2588" *len(str1), data2)
   
                count2 += len(str1)

    return data2, count2


def redactphone(data2):

    data22 = nlp(data2)

    pattern1 = [{"TEXT": "+1", "OP": "?"},{"TEXT": "(" ,"OP": "?"}, {"SHAPE": "ddd"}, {"TEXT": ")", "OP": "?"}, {"SHAPE": "ddd"}, {"TEXT": "-", "OP": "?"},{"SHAPE": "dddd"}  ]

    matcher = Matcher(nlp.vocab)

    matcher.add("phone no", [pattern1])

    matches = matcher(data22)

    count3 = 0

    for mid, start, end in matches:
        data2 = data2.replace(str(data22[start:end]), "\u2588" *len(str(data22[start:end])))
        
        count3 +=  len(str(data22[start:end]))

    return data2, count3


def redactdate(data2):

    data33 = nlp(data2)


    expression = r"([A-Za-z]{1,3},)(\s*)(\d{1,2})(\s*)([A-Za-z]{3})(\s*)(\d{2,4})(\s*)(\d{2}:\d{2}:\d{2})(\s*)(-*)(\d{4})(\s*)((\(*)([PCE]ST)(\)*))?"

    count41 = 0 

    for match in re.finditer(expression, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)

        if span is not None:
            
            str1 = str(span.text)
            
            data2 = data2.replace(str1, "\u2588" *len(str1))

            count41 += len(str1)

    expression1 = r"(\d{2})(\/)(\d{2})(\/)(\d{2})(\s*)(\d{2}:\d{2}:\d{2})(\s*)([AP]M)?"

    count42 = 0

    for match in re.finditer(expression1, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)

        if span is not None:
            
            str1 = str(span.text)
            
            data2 = data2.replace(str1, "\u2588" *len(str1))

            count42 += len(str1)

    count4 = count41 + count42        

    return data2, count4

def redactaddress(data2):

    data44 = nlp(data2)

    matcher44 = Matcher(nlp.vocab)

    pattern = [{"ENT_TYPE": "GPE"}, {"TEXT": ",", "OP": "?"}, {"TEXT": {"REGEX" : "[A-Z]{2}"}}, {"TEXT": {"REGEX": "(\d{5})"}}]

    matcher44.add("Location", [pattern])

    matches = matcher44(data44)

    count5 = 0

    for mid, start, end in matches:
        
        str1 = str(data44[start:end])
        
        data2 = data2.replace(str1, "\u2588"*len(str1))

        count5 += len(str1)

    return data2, count5

def redactconcept(data2):

    data55 = nlp(data2)


    count6 = 0

    for token in data55:
        
        if str(token) == "cancer" :
            
            token1 = data55[token.i]
            

            data2 = data2.replace(str(token1.sent), "\u2588"*len(str(token1.sent)))

            count6 += len(str(token1.sent))

    return data2, count6

