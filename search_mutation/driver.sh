#!/bin/sh

rm ./results/*.txt
touch ./results/mutation.txt
touch ./results/sort.txt
touch ./results/length.txt
touch ./results/fail.txt
touch ./correct.txt
touch ./truncating_ave.txt

python task1-3.py

python truncating_ave.py
