#!/bin/sh
rm ./results/*.txt
touch ./results/correct.txt
touch ./results/fail.txt
touch ./results/length.txt
touch ./results/mutation.txt
touch ./results/sort.txt


for FILE in `ls ./data/mutation_data/*.maf.txt`
do
	echo $FILE
	python input_maf_data.py $FILE
done

python mutsort.py

python genelen.py

python correct.py
