# -*- coding: utf-8 -*-
import json
import codecs
import sys
import MeCab
import collections
from collections import OrderedDict

def wakati(input_str):
        '''分かち書き用関数
        引数 input_str : 入力テキスト
        返値 m.parse(wakatext) : 分かち済みテキスト'''
        wakatext = input_str
        m = MeCab.Tagger('-Owakati')
        #print(m.parse(wakatext))
        return m.parse(wakatext)

argvs = sys.argv
argc = len(argvs)

file_name = str(argvs[1]).strip('.txt')
waka_file_name = file_name+'-wakati.txt'

if(argc != 2):
    print('Usage: python %s [filename]'% argvs[0])
    quit()

data = open(argvs[1],"r")
with open(waka_file_name, 'w') as wakafile:
    for line in data:
        wakaline = wakati(line)
        #print(wakaline)
        wakafile.write(wakaline)
