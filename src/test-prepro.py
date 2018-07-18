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


json_file = codecs.open("./raw/test.json", 'r', encoding='utf-8')


with open('./processed/tgt-test.txt', 'w') as tgt_test, open('./processed/ans-test.txt', 'w') as ans_test,\
 open('./processed/para-test.txt', 'w') as para_test, open('./processed/src-test.txt', 'w') as src_test,\
 open('doclist-test.txt', 'w') as doc_test:
    for line in json_file:
        json_dic = json.loads(line)

        #answer わかち処理
        ans_wakati = wakati(json_dic["answer"]).replace('\n','')
        ans_wakati = ans_wakati.strip()

        #question わかち処理
        question_wakati = wakati(json_dic["question"]).replace('\n','')
        question_wakati = question_wakati.strip()

        for article in json_dic["documents"]:
                if article["score"] >= 2:
                        #paragraph わかち処理
                        para_wakati = wakati(article["text"]).replace('\n','')
                        para_wakati = para_wakati.strip()

                        if para_wakati.find(ans_wakati) == -1:
                                continue
                        #para_wakati.find(ans_wakati) : 答えの開始位置

                        #paragraphsを文単位に分割
                        sent_lists = []
                        sent_lists = para_wakati.split('。')

                        #title わかち処理
                        title_wakati = wakati(article["title"]).replace('\n','')
                        title_wakati = title_wakati.strip()
                        title_under = title_wakati.replace(' ', '_')

                        #file書き出し
                        for sent_list in sent_lists:
                            if sent_list.find(ans_wakati) >= 0:
                                src_test.write(sent_list)
                                src_test.write(" 。\n")

                                para_test.write(para_wakati)
                                para_test.write('\n')

                                ans_test.write(ans_wakati)
                                ans_test.write('\n')

                                tgt_test.write(question_wakati)
                                tgt_test.write('\n')

                                doc_test.write(title_under)
                                doc_test.write('\n')
                            break


json_file.close()
