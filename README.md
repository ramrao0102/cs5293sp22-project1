Documentation for Project 1/CS 5293

This is Ramkishore Rao’s Project 1

A series of emails were provided from the Company Enron.  They are text files.  The corpus is called Enroncorpus.
The objective of the project is to redact certain sensitive information based on select set of rules that have been identified as criteria for the project.  The dataset was downloaded by running the following commands from the command line.
wget https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz 
tar xvzf enron_mail_20150507.tar.gz

Several files were placed under project1\enroncorpus.  Note a write1 folder was created under enroncorpus to place the redacted files in that folder following execution of the program.
Packages that were utilized to run the project are as follows:
•	sys
•	glob
•	re
•	pytest
•	spacy
•	nltk
•	from spacy.matcher we import Matcher and PhraseMatcher
•	from nltk.corpus we import wordnet
•	spacy’s medium language library was uploaded because I had difficulty uploading the large language library
The program is run from the command line with the following input:
pipenv run python project1\redactor.py --input '*.txt' \ 
                    --names --dates --phones --genders --address\ 
                    --concept 'prison' \ 
                    --output 'files/' \ 
                    --stats stderr
I made one change from specs as I placed the redactor.py file in a subfolder Project 1.
Note that the program can handle the argument stdout inplace of stderr if the user places that on the command line
