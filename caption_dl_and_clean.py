import os
import sys


channel_being_downloaded = input("What is the name of the channel you're downloading?")
# Parent Directory path
parent_dir = input("What is the path to your other transcripts?")
#New Directory
path = os.path.join(parent_dir, channel_being_downloaded)
#make the directory you're going to save to
os.mkdir(path)
print("Directory '% s' created" % channel_being_downloaded)
#move to the directory you're going to save to
os.chdir(path)

address_of_channel = input("What is the address of the channel?")
#all_of_the_regex_that_cleans_the_file = ''';for f in *.vtt;do sed '1,/^$/d' "$f"|sed 's/<[^>]*>//g'|awk -F. 'NR%8==1{printf"%s ",$1}NR%8==3'>"${f%.vtt}";done'''
#os.system(f"youtube-dl --no-check-certificate --write-auto-sub --skip-download -o'%(upload_date)s.%(title)s.%(id)s.%(ext)s' '{address_of_channel}'{all_of_the_regex_that_cleans_the_file}")
os.system(f"youtube-dl --no-check-certificate --write-auto-sub --skip-download -o'%(upload_date)s.%(title)s.%(id)s.%(ext)s' '{address_of_channel}'")


for root,_,files in os.walk(path):
    for file in files:
        if file.endswith(".vtt"):
            #specify the text to remove
            bad_words = ['-->', 'WEBVTT', '<c>', '</c>']
            #get the name of the new file
            new_file_name = str(os.path.join(root, file))
            #strip the .vtt ending from the file and append .tex
            new_file_name = os.path.splitext(new_file_name)[0]+".txt"
            #open each file in the directory one by one
            with open(os.path.join(root,file)) as oldfile, open(new_file_name, 'w') as newfile:
                #examine each line of the file
                lines_seen = set()
                for line in oldfile:
                    #check to see if it's an empty line
                    if not line.isspace():
                        #Look and see if there are any "bad_words", remove them if they're there
                        if not any(bad_word in line for bad_word in bad_words):
                            if line not in lines_seen: # not a duplicate
                                #print each "bad_word" free, non duplicate line to the file.
                                newfile.write(line)
                                lines_seen.add(line)
