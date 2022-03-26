
import sys

import numpy
import glob
import re
import nltk
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from nltk.corpus import wordnet


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

    count31 = 0

    for mid, start, end in matches:
        data2 = data2.replace(str(data22[start:end]), "\u2588" *len(str(data22[start:end])))
        
        count31 +=  len(str(data22[start:end]))



    expression = r"(\()?(\d{3})(\))?(\s*)?(.)?(\s*)?(\d{3})(\s*)?(.)?(\s*)?(\d{4})"


    count32 = 0 

    for match in re.finditer(expression, data22.text):
        start, end = match.span()
        span = data22.char_span(start,end)

        if span is not None:
            
            str1 = str(span.text)
            
            data2 = data2.replace(str1, "\u2588" *len(str1))

            count32 += len(str1)

    expression1 = r"(\()?(\d{3})(\))?(\s*)?(\/)?(\s*)?(\d{3})(\s*)?(\/)?(\s*)?(\d{4})"

    count33 = 0 

    for match in re.finditer(expression1, data22.text):
        start, end = match.span()
        span = data22.char_span(start,end)

        if span is not None:

            str1 = str(span.text)

            data2 = data2.replace(str1, "\u2588" *len(str1))

            count33 += len(str1)
    
    count3 = count31 + count32 + count33

    return data2, count3


def redactdate(data2):

    data33 = nlp(data2)


    expression = r"([A-Za-z]{1,9},)(\s*)(\d{1,2})(\s*)([A-Za-z]{1,9})(\s*)(\d{2,4})(\s*)(\d{2}:\d{2}:\d{2})(\s*)(-*)(\d{4})(\s*)((\(*)([PCE]ST)(\)*))?"

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


    expression2 = r"((\d{2})?(\s*)?([A-Za-z]+)(,?)(\s*)?(\d{4})(\s*?)(,?)((\s*)?(\d{2}?)((:?))(\d{2}?))?)"

    

    count43 = 0

    for match in re.finditer(expression2, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count43 += len(str1)


    expression3 = r"([A-Za-z]+)(,?)(\s*)?(\d{4})"

    count44 = 0

    for match in re.finditer(expression3, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count44 += len(str1)



    count4 = count41 + count42 + count43 + count44

    return data2, count4

def redactaddress(data2):

    data44 = nlp(data2)

    matcher44 = Matcher(nlp.vocab)

    pattern = [{"ENT_TYPE": "GPE"}, {"TEXT": ",", "OP": "?"}, {"TEXT": {"REGEX" : "[A-Z]{2}"}}, {"TEXT": {"REGEX": "(\d{5})"}}]

    matcher44.add("Location", [pattern])

    matches = matcher44(data44)

    count51 = 0

    for mid, start, end in matches:
        
        str1 = str(data44[start:end])
        
        data2 = data2.replace(str1, "\u2588"*len(str1))

        count51 += len(str1)

    count52 =0

    expression41 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:St)(.)?"

    for match in re.finditer(expression41, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count52 += len(str1)

    count53 =0

    expression42 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Rd)(.)?"


    for match in re.finditer(expression42, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count53 += len(str1)

    count54 =0

    expression43 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Ave)(.)?"


    for match in re.finditer(expression43, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count54 += len(str1)

    count55 = 0


    expression44 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Hwy)(.)?"


    for match in re.finditer(expression44, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count55 += len(str1)

    count56 = 0

    expression45 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Plaza)(.)?"


    for match in re.finditer(expression45, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count56 += len(str1)

    count57 = 0

    expression46 = r"(P)(\s*)?(O)(\s*)?(Box)(\s*)?(\d+) (.)?"

    for match in re.finditer(expression46, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        if span is not None:
            str1 = str(span.text)
            data2 = data2.replace(str1, "\u2588" *len(str1))
            count57 += len(str1)


    count5 = count51 + count52 + count53 + count54 + count55 + count56 + count57

    return data2, count5
    


def redactconcept(data2, conceptstr):

    data55 = nlp(data2)


    count6 = 0

    syno = similarword(conceptstr)

    for k in syno:


        for token in data55:
        
            if str(token) == k:
            
                token1 = data55[token.i]
                
                print(str(token1.sent))

                data2 = data2.replace(str(token1.sent), "\u2588"*len(str(token1.sent)))

                count6 += len(str(token1.sent))

    return data2, count6

def similarword(conceptstr):
    synonyms = ['jail', 'jailhouse', 'gaol', 'clink', 'slammer', 'poky', 'pokey', 'imprison', 'incarcerate', 'lag', 'immure', 'put_behind_bars', 'jail', 'jug', 'gaol', 'put_away', 'remand']

   # for syn in wordnet.synsets(conceptstr):
    #    for lm in syn.lemmas():
     #       synonyms.append(lm.name())


    print(synonyms)

    return synonyms
