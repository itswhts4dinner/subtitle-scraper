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

#get address of the channel
address_of_channel = input("What is the address of the channel?")
#download the .vtt files
os.system(f"youtube-dl --no-check-certificate --write-auto-sub --skip-download -o'%(upload_date)s.%(title)s.%(id)s.%(ext)s' '{address_of_channel}'")

#Look at the folder full of .vtt files you just downloaded
for root,_,files in os.walk(path):
    for file in files:
        #only work on the .vtt files
        if file.endswith(".vtt"):
            #specify the text to remove
            bad_words = ['-->', 'WEBVTT', '<c>', '</c>']
            #get the name of the new file
            new_file_name = str(os.path.join(root, file))
            #strip the .vtt ending from the file and append .tex
            new_file_name = os.path.splitext(new_file_name)[0]+".txt"
            #open each file in the directory one by one
            with open(os.path.join(root,file)) as oldfile, open(new_file_name, 'w') as newfile:
                #create a list of lines from the file that you're cleaning to see if it's a duplicate line.
                lines_seen = set()
                #examine each line of the file
                for line in oldfile:
                    #check to see if it's an empty line
                    if not line.isspace():
                        #Look and see if there are any "bad_words", remove them if they're there
                        if not any(bad_word in line for bad_word in bad_words):
                            if line not in lines_seen: # not a duplicate
                                #print each "bad_word" free, non duplicate line to the file.
                                newfile.write(line)
                                #add this new line to the list of lines you've examined for duplicates
                                lines_seen.add(line)
