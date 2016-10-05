#!/bin/sh


for FILE in `ls ./data/mutation_data/*.maf.txt`
do
	echo $FILE
	python input_maf_data.py $FILE
done

python mutsort.py

python genelen.py

python correct.py
