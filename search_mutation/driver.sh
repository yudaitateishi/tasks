#!/bin/sh

rm ./results/*.txt

python task1-3.py

python truncating_ave.py
