DOCUMENTATION FOR PROJECT 1/CS5293
This is Ramkishore Rao’s Project 1
A series of emails were provided from the Company Enron.  They are text files.  The corpus is called Enroncorpus.
The objective of the project is to redact certain sensitive information based on select set of rules that have been identified as criteria for the project.  The dataset was downloaded by running the following commands from the command line.
wget https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz tar xvzf enron_mail_20150507.tar.gz
Several files were placed under project1\enroncorpus.  Note a write1 folder was created under enroncorpus to place the redacted files in that folder following execution of the program.
Packages that were utilized to run the project are as follows:
* sys
* glob
* re
* pytest
* spacy
* nltk
* from spacy.matcher we import Matcher and PhraseMatcher
* from nltk.corpus we import wordnet
* spacy’s medium language library was uploaded because I had difficulty uploading the large language library by typing the following command on the command line
nlp = spacy.load('en_core_web_md')
The program is run from the command line with the following input:
pipenv run python project1\redactor.py --input '*.txt' \ 
                    --names --dates --phones --genders --address\ 
                    --concept 'prison' \ 
                    --output 'files/' \ 
                    --stats stderr
I made one change from specs as I placed the redactor.py file in a subfolder Project 1.
Note that the program can handle the argument stdout inplace of stderr if the user places that on the command line.
sys.argv is used to find the arguments that are entered on the command line and assign them to the variables.
The idea on the redactor program is to take redact names, dates, phones, genders, and address in various formats in the text file.  The next step is to take the concept word, in this case ‘prison’, find related words and redact the sentences that this word belongs to from the emails.
Index 0 on the command line or sys.argv is the name of the file redactor.py, from there the indexes are increased by a value of 1 for each string that is placed on the command line.  
Following the word input is ‘*.txt’.  This is assigned to sys.argv[1].
To this file name, I am adding the following path that presents the folder in which this file exists, which is:
“/home/ramrao0102/project1/enroncorpus/” + filename
Glob.glob(path) is used to grab all the files and the files are read one at a time in a for loop.
For each file, the data is assigned to data2, which is a string and it is then passed by calling functions from the “project1.py” file.
Several functions have been written in the project1.py to perform the redaction.
The function def redactname(data2) is used to find “PERSON”.  
1) If a person entity type is founded, it is redacted, and the count of the length of the string redacted and the data2 string is returned to main.
2) \u2588 unicode full block character replaces each string character redacted.

The function def redactgender(data2) is used to find gender strings to redact.
1) I am using a list of "he", "him", "her", "she", "He", "She", "Him", "Her" in a list and if a token in a data string matches these strings, then the token is redacted. The count of the length of the string redacted and the data2 string is returned to main.
2) \u2588 unicode full block character replaces each string character redacted.

The function redactphone(data2) is used to find phone numbers of different patterns to redact.
1) Pattern1 :   	
	+1 Optional  
       ( Optional 
       3Digits 
       ) Optional
       3 Digits
-  Optional
- 4 Digits
 
2) Expression :  	
	( - Optional
	3 Digits
	) Optional
	Whitespace Optional
	. Optional
	Whitespace Optional
	3 Digits
	Whitespace Optional
	. Optional
	Whitespace Optional
	4 Digits

3) Expression1:	
	( - Optional
	3 Digits
	) Optional
	Whitespace Optional
	/ Optional
	Whitespace Optional
	3 Digits
	Whitespace Optional
	/ Optional
	Whitespace Optional
	4 Digits

The count of the length of the string redacted and the data2 string is returned to main.
\u2588 unicode full block character replaces each string character redacted.
The function redactdate(data2) is used to find dates of different patterns to redact.
1) Expression:	any character from A-Z or a-z of 1 to 9 characters in length
	Whitespace , zero or more
	Digits -1 to 2 long
	any character from A-Z or a-z of 1 to 9 characters in length
	Whitespace, zero or more
	Digits – 2 to 4 long
	Whitespace, zero or more
	2Digits: 2Digits : 2Digits 
	Whitespace, zero or more
	- zero or more
	4 digits 
	Whitespace, zero or more
	( - Zero or More
	P, C, or E followed by ST
	)  Zero or More


	

