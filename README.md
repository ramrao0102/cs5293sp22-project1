<<<<<<< HEAD
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

The program is run from the command line with the following input:<br>
pipenv run python redactor.py --input '*.txt' \ <br>
                                       --names --dates --phones --genders --address\ <br> 
                                       --concept 'prison' \ <br>
                                       --output 'files/' \ <br>
                                       --stats stderr

Note that the program can handle the argument stdout inplace of stderr if the user places that on the command line.
sys.argv is used to find the arguments that are entered on the command line and assign them to the variables.


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
=======
This is Ramkishore Rao's readme file for Project 1
Introduction
'A series of emails were provided from the Company Enron. They are text files. The corpus is called Enroncorpus. The objective of the project is to redact certain sensitive information based on select set of rules that have been identified as criteria for the project. The dataset was downloaded by running the following commands from the command line. wget https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz tar xvzf enron_mail_20150507.tar.gz Several files were placed under project1\enroncorpus. Note a write1 folder was created under enroncorpus to place the redacted files in that folder following execution of the program. Packages that were utilized to run the project are as follows:'

sys
glob
re
pytest
spacy
nltk
from spacy.matcher we import Matcher and PhraseMatcher
from nltk.corpus we import wordnet
Also, spacy’s medium language library was uploaded because I had difficulty uploading the large language library by typing the following command on the command line.
9. nlp = spacy.load('en_core_web_md')

The program is run from the command line with the following input:
pipenv run python redactor.py --input '*.txt' \
--names --dates --phones --genders --address\
--concept 'prison' \
--output 'files/' \
--stats stderr

Note that the program can handle the argument stdout inplace of stderr if the user places that on the command line. sys.argv is used to find the arguments that are entered on the command line and assign them to the variables.

	

>>>>>>> 9741dc4dc7731cb39bd154d4a38732688ea5b805
