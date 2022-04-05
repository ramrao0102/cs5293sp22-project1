
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

    matcher = Matcher(nlp.vocab)
    
    pattern = [{"ENT_TYPE": "PERSON"}]
    matcher.add("personEnt", [pattern])    
    
    matches = matcher(data1)

    listname = []

    for mid, start, end in matches:
        listname.append((start,end))
        count1 += len(str(data1[start:end]))
        
    return listname, count1


def redactgender(data2):

    data11 = nlp(data2)

    gender = ["he", "him", "her", "she", "He", "She", "Him", "Her", "father", "Father", "Mother", "mother", "Sister", "sister", "Brother", "brother", "girl", "Girl", "Boy", "boy"]

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
    
    listphone = []

    count31 = 0

    for mid, start, end in matches:
        
        listphone.append((start,end))
        count31 +=  len(str(data22[start:end]))


    expression = r"(\()?(\d{3})(\))?(\s*)?(.)?(\s*)?(\d{3})(\s*)?(.)?(\s*)?(\d{4})"


    count32 = 0 

    for match in re.finditer(expression, data22.text):
        start, end = match.span()
        span = data22.char_span(start,end)

                
        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listphone.append((start,end))

        if span is not None:
            
            j = 0

            str1 = str(span.text)
                      
            count32 += len(str1)

    expression1 = r"(\()?(\d{3})(\))?(\s*)?(\/)?(\s*)?(\d{3})(\s*)?(\/)?(\s*)?(\d{4})"

    count33 = 0 

    for match in re.finditer(expression1, data22.text):
        start, end = match.span()
        span = data22.char_span(start,end)

        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listphone.append((start,end))

        if span is not None:

            str1 = str(span.text)

            count33 += len(str1)
    
    count3 = count31 + count32 + count33

    return listphone, count3


def redactdate(data2):

    data33 = nlp(data2)


    expression = r"([A-Za-z]{1,9},)(\s*)(\d{1,2})(\s*)([A-Za-z]{1,9})(\s*)(\d{2,4})(\s*)(\d{2}:\d{2}:\d{2})(\s*)(-*)(\d{4})(\s*)((\(*)([PCE][DS]T)(\)*))?"

    count41 = 0 

    listdate = []


    for match in re.finditer(expression, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)

        if span is not None:

            j = 0

            for token in span:

                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listdate.append((start,end))


        if span is not None:
            
            str1 = str(span.text)
    
            count41 += len(str1)

    expression1 = r"(\d{2})(\/)(\d{2})(\/)(\d{4})(\s*)(\d{2})(:)(\d{2})(:)?(\d{2})?(\s*)([AP]M)"

    count42 = 0

    for match in re.finditer(expression1, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)

        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listdate.append((start,end))


        if span is not None:
            
            str1 = str(span.text)

            count42 += len(str1)


    expression2 = r"((\d{2})(\s*)?([A-Za-z]+)(,?)(\s*)?(\d{4})(\s*?)(,?)((\s*)?(\d{2}?)((:?))(\d{2}?))?)"

    

    count43 = 0

    for match in re.finditer(expression2, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)

        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listdate.append((start,end))

        if span is not None:
            str1 = str(span.text)
            
            count43 += len(str1)

    expression3 = r"[A-Za-z]{1,9}(,)(\s*)?[A-Za-z]{1,9}(\s*)(\d{2})(,)?(\s*)?(\d{4})(\s*)(\d*)?(:)?(\d*)(\s*)([AP]M)?"
    
    count441 = 0

    for match in re.finditer(expression3, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)
        
        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listdate.append((start,end))

        if span is not None:
            str1 = str(span.text)
            
            count441 += len(str1)


    expression4 = r"([A-Za-z]+)(,?)(\s*)?(\d{4})"

    count44 = 0

    for match in re.finditer(expression4, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)
       
        if span is not None:

            j =0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listdate.append((start,end))

        if span is not None:
            str1 = str(span.text)
            
            count44 += len(str1)


    expression5 = r"(\d{2})(\/)(\d{2})(\/)(\d{4})"

    count45 = 0

    for match in re.finditer(expression5, data33.text):
        start, end = match.span()
        span = data33.char_span(start,end)
        
        if span is not None:

            j = 0 

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listdate.append((start,end))

        if span is not None:
            str1 = str(span.text)
            
            count45 += len(str1)

    count4 = count41 + count42 + count43 + count441+ count44 + count45

    return listdate, count4

def redactaddress(data2):

    data44 = nlp(data2)

    matcher44 = Matcher(nlp.vocab)

    pattern = [{"ENT_TYPE": "GPE"}, {"TEXT": ",", "OP": "?"}, {"TEXT": {"REGEX" : "[A-Z]{2}"}}, {"TEXT": {"REGEX": r"(\d{5})"}}]

    matcher44.add("Location", [pattern])

    matches = matcher44(data44)

    listaddress = []

    count51 = 0

    for mid, start, end in matches:
        
        listaddress.append((start,end))

        str1 = str(data44[start:end])
      
        
        count51 += len(str1)

    count52 =0

    expression41 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:St)(.)?"

    for match in re.finditer(expression41, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        
        if span is not None:
            
            j =0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listaddress.append((start,end))


        if span is not None:
            str1 = str(span.text)
            
            count52 += len(str1)

    count53 =0

    expression42 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Rd)(.)?"


    for match in re.finditer(expression42, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        
        if span is not None:

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listaddress.append((start,end))

        if span is not None:
            str1 = str(span.text)
            
            count53 += len(str1)

    count54 =0

    expression43 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Ave)(.)?"


    for match in re.finditer(expression43, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        

        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listaddress.append((start,end))

        if span is not None:
            str1 = str(span.text)
            
            count54 += len(str1)

    count55 = 0


    expression44 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Hwy)(.)?"


    for match in re.finditer(expression44, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        
        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listaddress.append((start,end))

        if span is not None:
            str1 = str(span.text)
            
            count55 += len(str1)

    count56 = 0

    expression45 = r"(\d{0,9})(\s*)?(([A-Za-z]+)?)(\s*)? (([A-Za-z]+)?)(\s*)?(?:Plaza)(.)?"


    for match in re.finditer(expression45, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        
        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listaddress.append((start,end))


        if span is not None:
            str1 = str(span.text)
            
            count56 += len(str1)

    count57 = 0

    expression46 = r"(P)(\s*)?(O)(\s*)?(Box)(\s*)?(\d+) (.)?"

    for match in re.finditer(expression46, data44.text):
        start, end = match.span()
        span = data44.char_span(start,end)
        
        if span is not None:

            j = 0

            for token in span:
                if j ==0:
                    start = token.i
                if j == len(span) -1:
                    end = token.i+1
                j += 1

            listaddress.append((start,end))


        if span is not None:
            str1 = str(span.text)
            
            count57 += len(str1)


    count5 = count51 + count52 + count53 + count54 + count55 + count56 + count57

    return listaddress, count5
    


def redactconcept(data2, conceptstr):

    data55 = nlp(data2)


    count6 = 0

    listconcept = []

    syno = similarword(conceptstr)

    for k in syno:

        for token in data55:
        
            if str(token) == k:
            
                token1 = data55[token.i]
                
                #print(str(token1.sent))

                j = 0

                for token in token1.sent:

                    if j ==0:
                      
                        start = token.i

                    if j == len(token.sent) -1:
                        
                        end = token.i + 1

                    j += 1

                listconcept.append((start,end))

                
                count6 += len(str(token1.sent))

    return listconcept, count6

def similarword(conceptstr):
    synonyms = [ ]

    for syn in wordnet.synsets(conceptstr):
        for lm in syn.lemmas():
            synonyms.append(lm.name())


    return synonyms
