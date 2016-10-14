#!/bin/sh

python task1.py ./data/mutation_data/*.maf.txt

python task2.py ./data/refGene/refGene.txt

python task3.py ./results/mutation_count.txt ./results/gene_length.txt

python task4.py ./results/mutation_list.txt ./results/mutation_count.txt
