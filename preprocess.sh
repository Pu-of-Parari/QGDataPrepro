#!/usr/bin/env bash

echo train reshaping...
python ./src/train_prepro.py

echo dev reshaping...
python ./src/dev_prepro.py

echo %test reshaping...
python ./src/test_prepro.py

echo completed! output dataset are ./processed/
