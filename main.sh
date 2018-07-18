#!/bin/bash
echo train reshaping...
python ./src/train-prepro.py

echo dev reshaping...
python ./src/dev-prepro.py

echo %test reshaping...
python ./src/test-prepro.py

echo completed! output dataset are ./processed/
