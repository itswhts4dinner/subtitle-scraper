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
            new_file_name = str(os.path.join(root, file)) + '.txt'
            with open(os.path.join(root,file)) as oldfile, open(new_file_name, 'w') as newfile:
                for line in oldfile:
                    if not any(bad_word in line for bad_word in bad_words):
                        newfile.write(line)
