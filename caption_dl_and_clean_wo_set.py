import os
import sys



channel_being_downloaded = input("What is the name of the channel you're downloading?")
# Parent Directory path
parent_dir = input("What is the path to your other transcripts?")
#New Directory
path = os.path.join(parent_dir, channel_being_downloaded)
#make the directory you're going to save to
os.mkdir(path)
print(f"Directory {channel_being_downloaded} created")
#move to the directory you're going to save to
os.chdir(path)

#get address of the channel
address_of_channel = input("What is the address of the channel?")
#download the .vtt files
os.system(f"youtube-dl --no-check-certificate --write-auto-sub --skip-download -o'%(upload_date)s.%(title)s.%(id)s.%(ext)s' '{address_of_channel}'")


#Look at the folder full of .vtt files you just downloaded
#clean all files of formatting and convert to .txt
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
                lines_seen = ""
                #examine each line of the file
                for line in oldfile:
                    #check to see if it's an empty line
                    if not line.isspace():
                        #Look and see if there are any "bad_words", remove them if they're there
                        if not any(bad_word in line for bad_word in bad_words):
                            if line != lines_seen: # not a duplicate
                                #print each "bad_word" free, non duplicate line to the file.
                                newfile.write(line)
                                #add this new line to the list of lines you've examined for duplicates
                                lines_seen = line
#Organize all the files by type and put them in their own folders
#delete all .en files
for root,_,files in os.walk(path):
    #creath directories for the vtt and txt files
    vtt_dir = os.path.join(parent_dir, channel_being_downloaded, "vtt files")
    txt_dir = os.path.join(parent_dir, channel_being_downloaded, "txt files")
    os.mkdir(vtt_dir)
    os.mkdir(txt_dir)
    for file in files:
        #if it ends in vtt move it to the vtt folder
        if file.endswith(".vtt"):
            src = f"{path}/{file}"
            dst = f"{vtt_dir}/{file}"
            os.rename(src, dst)
        #if it ends in txt move it to the txt folder
        if file.endswith(".txt"):
            src = f"{path}/{file}"
            dst = f"{txt_dir}/{file}"
            os.rename(src, dst)
        #if it ends in .en delete it
        if file.endswith(".en"):
            src = f"{path}/{file}"
            os.remove(src)
