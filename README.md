# This is Ramkishore Rao's readme file for Project 1

## Introduction

'A series of emails were provided from the Company Enron.  They are text files.  The corpus is called Enroncorpus.
The objective of the project is to redact certain sensitive information based on select set of rules that have been 
identified as criteria for the project.  The dataset was downloaded by running the following commands from the command line.
wget https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz tar xvzf enron_mail_20150507.tar.gz
Several files were placed under project1\enroncorpus.  Note a write1 folder was created under enroncorpus to 
place the redacted files in that folder following execution of the program.
Packages that were utilized to run the project are as follows:'

1. sys
2. glob
3. re
4. pytest
5. spacy
6. nltk
7. from spacy.matcher we import Matcher and PhraseMatcher
8. from nltk.corpus we import wordnet

Also, spacy’s medium language library was uploaded because I had difficulty uploading the large language library by typing the following command on the command line.<br>
9. nlp = spacy.load('en_core_web_md')


## Program Execution from Command Line, Read Files for Redaction

The program is run from the command line with the following input:<br>
pipenv run python redactor.py --input '*.txt' \ <br>
                                       --names --dates --phones --genders --address\ <br> 
                                       --concept 'prison' \ <br>
                                       --output 'enroncorpus/write1/' \ <br>
                                       --stats stderr

Note that the program can handle the argument stdout inplace of stderr if the user places that on the command line. <br>
Both stdout and stderr are printing to console while the string after the --output is being used as folder/file for <br>
placement of the redacted text file.<br>
sys.argv is used to find the arguments that are entered on the command line and assign them to the variables. <br>

At ths start of the project several text files were placed in /enroncorpus folder. <br>
These are the files that need to be redacted by the program. <br>
Note also that a directory /enroncorpus/write1 was created to place the redacted text files after they were created.

sys.argv is used to find the arguments that are entered on the command line and assign them to the variables.
The idea on the redactor program is to take redact names, dates, phones, genders, and address in various formats <br>
in the text file.

For the sys.argv to work correctly the order of the input string on the command line at runtime should follow <br>
what is presented above.  After --input, we need to have the *.txt for the glob to read input files.  <br>                      After --concept, conceptstring should be entered.  After --output, the folder location with relative path <br>
should be entered.  After --stats, either stdout or stderr should be entered.

The redactor.py then takes the filename passed as input and directs it to a relative path from root to enroncorpus to read <br>
via the glob.glob command. 

## Program Execution for Redaction

The files are read one at a time and then the redactor.py calls functions within project1.py to implement redaction

For each file, the data is assigned to data2, which is a string and it is then passed by calling functions from <br>
the “project1.py” file. <br>
Several functions have been written in the project1.py to perform the redaction.<br>

The function def redactname(data2) is used to find “PERSON”

1) If a person entity type is founded, it is redacted, and the count of the length of the string redacted and the data2 string is returned to main. <br>
2) \u2588 unicode full block character replaces each string character redacted. <br>

The function redactphone(data2) is used to find phone numbers of different patterns to redact. <br>
There are 3 patterns/expressions that are being checked for redaction of phone numbers <br>

Pattern 1:  +1 (Optional) (315)- 243 3255 Note that parentheses before and after first 3 digits and - are optional <br>
Expression: (315). 243 . 3255 Note that parentheses before and after first three digits are optional.  Note also whitespaces between digits and the .'s are optional.<br>
Expression 1:  (315) /243 / 3255  Note that parentheses before and after first three digits are optional.  Note also whitespaces between digits and the / are optional.

The function redactdate(data2) is used to find dates of different patterns to redact.<br>
There were several patterns/expressions checked and they are presented below.<br>

Expression <br>
Sun, 30 Dec 2001 22:49:42 -0800 (PST), This will allow any day of the week to be included first, followed by the date, month, <br> 
time in the format provided and either P, C, or E as the letters to denote which zone we are in followed by ST. <br>
Also allowed is D instead of S in the expression <br>
Expression1 <br>
02/03/22 12:15 AM or 02/03/22 12:15 PM <br>
02/03/22 12:15:30 AM or 02/03/22 12:15:30 PM <br>
Expression2 <br>
13 Dec 2000, 15:55 or 13 December 2000, 15:55 <br>
Expression3 <br>
Tuesday, November 27, 2001 or Tue, Nov 27, 2011 <br>
This expression will acccomodate 10:30:25 AM or PM as options after the year
Expression4 <br>
January, 2022 or Jan, 2022 or January 2022 or Jan 2022 <br>
Expression4 <br>
02/20/2011 <br>

The function redactaddress(data2) is used to find addresses of different patterns to redact. <br>
There were several patterns/expressions checked and they are presented below.

Pattern <br>
It will find an entity such as city or state that can be read by entity finder of spacy in the string and letters that <br>
denote address and five digits for zip code.  <br>
Several Expressions to find the following: <br>
4725 Divisidero St or Street <br>
4725 Divisidero Rd or Road<br>
4725 Divisidero Ave or Avenue<br>
4725 CarlosBee Hwy or Highway <br>
4725 CarlosBee Plaza or Pz<br>
An Expression to find the following: <br>
P O Box 25245.  Spaces are optional and there are 1 or more digits after Box

The function  redactconcept(data2, conceptstr) is used to find a conceptstr from the command line and then redact sentences <br>
that contain that conceptstr. <br>
wordnet is used to find synonmys for the conceptstr and so the conceptstr and its synonyms are searched for in the text file <br>
and the sentences tha contain them are redacted. <br>

The function def redactgender(data2) is used to find gender strings to redact.<br>

1) I am using a list of "he", "him", "her", "she", "He", "She", "Him", "Her", "father", "Father", "Mother", <br>
"mother", "Sister", "sister", "Brother", "brother", "girl", "Girl", "Boy", "boy" in a list and if a token in a <br>
data string matches these strings, then the token is redacted. The count of the length of the string redacted and <br>
the data2 string is returned to main. <br>
2) \u2588 unicode full block character replaces each string character redacted.<br>

Note that five of the functions in the project1.py return a list that contains the span of the tokens to be redacted from the datafile and <br>
the redaction occurs in the redactor.py file. Each value in the list is a tuple that contains the start index and the end index of the tokens to <br>
be redacted. These five functions are for redaction of names, phone numbers, dates, addresses, and concept string. <br>
The redaction for the sixth function, gender specific words is occuring in the project1.py function directly. <br>

Once executed the data is returned to the redactor.py file and it is written to a file with redacted added <br>
(e.g., 211_2.txtredacted) and stored in /enroncorpus/write1 relative path from root.

## Bug

Noticed one bug in the list that contains the strings to be redacted.  On one of the files, it was redacting a single <br>
character string  in the date string.  In order to find a workaround, I am only redacting those strings that are of a <br>
length of more than 1 character. This is specific to the spans being retained in the list that is being used to redact.<br>
It applies to names, phone #s, dates, addresses, and concept string.  This does not apply to the gender specific string.<br>
As that redaction is being handled separately and after the redaction for other types are completed. <br>

## Statistics for Redacted Strings

The length of the strings that are redacted by the functions above are estimated each time a redaction occurs <br>
and returned to reactor.py and these estimates are then either writen to a stats.txt file and stored in the root folder. <br>
The option also exists to be output to console should the user enter stdout or stderr after --stats string on command line. <br>
The stats.txt file contains the lengths of the strings redacted by redaction type.

The stats.txt file contains six lines: <br>
1) Line 1 contains total length of redacted string from all text files processed for names. <br>
2) Line 2 contains total length of redacted string from all text files processed for phone numbers. <br>
3) Line 3 contains total length of redacted string from all text files processed for dates. <br>
4) Line 4 contains total length of redacted string from all text files processed for addresses. <br>
5) Line 5 contains total length of redacted string from all text files processed for conceptstring. <br>
6) Line 6 contains total length of redacted string from all text files processed for gender specific words.

## Testing of Package

There are 5 tests included in the package:<br>
    1) The first testfile (test_istheredata.py) has a function that checks for count of files following redaction in /enroncorpus/write1.<br>
        This function then has an assert statement that checks if there is more than 0 files, which tells us if a file is <br>
        passed in or read, then it is redacted as there are redacted files in the folder.


2) The second testfile (test_functions.py) has a function that checks the contents of stats.txt in root and asserts<br>
   if the values are greater than 0 for each type of redaction.  The stats.txt file contains length of <br>
   strings redacted by redaction type.  So, it implicitly checks that the functions for redaction are being <br>
   executed by the code in the package.

3) The third testfile (test_namefunction.py) reads the glob of text files passed in and tests the redactname function in <br>
project1.py, completes the redaction, and checks if the length of total redacted strings matches the length in the stats.txt file.

4) The fourth testfile (test_phonefunction.py) reads the glob of text files passed in and tests the redactphone function in
project1.py, completes the redaction, and checks if the length of total redacted strings matches the length in the stats.txt file.

5) The fifth testfile (test_datefunction.py) reads the glob of text files passed in and tests the redactdate  function 
in project1.py, completes the redaction, and checks if the length of total redacted strings matches the length in the stats.txt file.


```python

```
