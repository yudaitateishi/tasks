#!/bin/sh

python task1.py ./data/mutation_data/*.maf.txt ./results/mutation_list.txt ./results/mutation_count.txt

python task2.py ./data/refGene/refGene.txt ./results/gene_length.txt

python task3.py ./results/mutation_count.txt ./results/gene_length.txt count_length_avg.txt

python task4.py ./results/mutation_list.txt ./results/mutation_count.txt ./results/truncating_count_avg.txt
