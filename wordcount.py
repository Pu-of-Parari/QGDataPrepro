#!/usr/bin/python
#coding:utf-8
'''与えたテキストファイルの単語数、行数、１行あたりの単語数をカウントする
        使い方
        python wordcount.py ファイル名
'''

import sys

argvs = sys.argv
argc = len(argvs)

if(argc != 2):
    print('Usage: python %s [filename]'% argvs[0])
    quit()

wordlist = []
data = open(argvs[1],"r")
wordcounter = 0
linecounter = 0
sentcounter = 0

for line in data:
    line = line.rstrip()
    words = line.split(' ')
    wordlist += words
    linecounter += 1

data.close()

for word in wordlist:
    wordcounter += 1
    if(word.find("。") > -1):
        sentcounter +=1

print("About %s ..." %argvs[1])
print("tokens : ",wordcounter)
print("lines  : ",linecounter)
print("sents :", sentcounter)
print("avg word per line : ", wordcounter / linecounter)
print("avg sent per paragraph :", sentcounter / linecounter)
