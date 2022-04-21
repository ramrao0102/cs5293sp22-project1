# Changes Log

## Output Files not Stored in Respective Folder

I have moved the *.txt files to the project1 folder.  Now the readpath does not point to a subfolder.  It just reads from the 
glob.glob, the string that the user passes to read the files is after the --input flag.

Also, I have now added code to handle the creation of a directory where the user wants to store the redacted files.  This is the directory that the user adds from the command line following the --output flag.  Note that one key item here is that the 
output file should either end with the "/" character or not have the "/" character, there should not be a white space at the end of the "/" character for my code to be functional.

Another key assumption here the flags need to have -- infront of it and should have the same spelling as noted in the project directions.  Otherwise for example if the user uses --output as a flag and 'output' as the conceptstring it messes the code up.  So, please make sure that then flags follow the pattern noted in the assignment.  Also, there should be no space between the -- and the flag.  I am sure there is a way to generalize this more, but I have not attempted to do it.  I want to make sure that we get past the command line and actually review the work please.
For some reason, after I committed the changes to markdown, the end of line character \ got stripped but we need to have the end of line character <br>
when we enter into command line to run the program. <br>


pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --concept 'jail' \
                    --output 'testoutput/‘ \
                    --stats stderr


## None of the features are being redacted.

I believe this error occurred because the files are first not being read and so the code was not processing the <br>
information nor were output files being generated.  This has been corrected.  Please see above explanation. <br>

## Missing Stats

I have now added code to make sure that when the user enters a text file after the --stats flag, then based on the <br>
they enter, it will create a stats log of the total length of redactions that are to occur <br>

Also, another "stats" file is being created and is being written to the project root folder.  This file will be "redirected" <br>
to statstderr when the user enters stderr after the --stats flag or statsstdout when the user enters stdout after <br>
the --stats flag.

## File Names Not Assigned Correctly

I believe this error occurred because the files are first not being read and so the code was not processing the
information nor were output files being generated. This has been corrected. Please see above explanation.

## Test Functions Missing

I believe this error occurred because the files are first not being read and so the code was not processing the <br>
information nor were output files being generated. This has been corrected. Please see above explanation. <br>

Also note that I have now added code in the redactor.py program to write the readpath of the glob and the writedirectory <br>
that the user enters for the folder where the redacted files are to be stored.<br>
These paths are then read from the test functions to check the various functions implemented in Project 1. <br>

