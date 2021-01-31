import sys
import os

bad_words = ['-->', 'WEBVTT']
with open('oldfile.vtt') as oldfile, open('newfile.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
