import sys
import os

#ask for path to ccdirectory
ccdirectory = input("Enter the path to the directory to translate:\n")
os.chdir(ccdirectory)
###
#Get file folder and files#
for root,_,files in os.walk(ccdirectory):
    for file in files:
        if file.endswith(".vtt"):
            #specify the text to remove
            bad_words = ['-->', 'WEBVTT']
            #get the name of the new file
            new_file_name = str(os.path.join(root, file))
            #strip the .vtt ending from the file and append .tex
            new_file_name = os.path.splitext(new_file_name)[0]+".txt"
            #open each file in the directory one by one
            with open(os.path.join(root,file)) as oldfile, open(new_file_name, 'w') as newfile:
                #examine each line of the file
                for line in oldfile:
                    #Look and see if there are any "bad_words", remove them if they're there
                    if not any(bad_word in line for bad_word in bad_words):
                        #print each "bad_word" free line to the file.
                        newfile.write(line)
