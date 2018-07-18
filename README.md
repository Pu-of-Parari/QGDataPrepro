# QGDataPrepro
## Overview
Data preprocess for neural question generation model
This is the data split described in the paper "Learning to Ask: Neural Question Generation for Reading Comprehension." by Du et. al, ACL (2017) using "回答可能性付き読解データセット" in the paper "読解による解答可能性を付与した質問応答データセットの構築"by M. Suzuki et. al, 言語処理学会 第24回年次大会.

The structure of this folder is:

    data
    ├── processed
    │   ├── src-{train, dev, test}.txt
    │   ├── tgt-{train, dev, test}.txt
    │   └── para-{train, dev, test}.txt
    │  
    ├── raw
    │   ├── train.json
    │   ├── dev.json
    │   └── test.json
    │
    ├── doclist-train.txt
    ├── doclist-dev.txt
    └── doclist-test.txt

The `raw` folder includes the raw data files from the Suzuki's dataset, split into train.json, dev.json, test.json set. The data is divided beforehand into 13,000(train), 1300(dev), 1,291(test) respectively.

## Requirements
MeCab-python3

## 
You only need to execute this command.

for windows

`./preprocess.sh`

for linux

`./main.sh`

The output files are `./processed` and the `doclist-*.txt`.


`wordcount.py` can count the number of words and sentences.
Use it as follows:

`python wordcount.py <textfile.txt>`
