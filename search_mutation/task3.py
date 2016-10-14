#!/usr/bin/env python

import sys
import glob

if len(sys.argv) < 3:
	print("Usage: #python task3.py mutation length")
	quit()

mutation = {}
with open(sys.argv[1],"r") as mutation_file:
	for line in mutation_file:
		items = line[:-1].split("\t")
		mutation[items[0]] = items[1]

length = {}
with open(sys.argv[2],"r") as length_file:
	for line in length_file:
		items = line[:-1].split("\t")
		length[items[0]] = items[1]

count_length_avg = {}
result = open("./results/count_length_avg.txt","w")
failure = open("./results/failure.txt","w")

for gene,value in mutation.items():
	if gene in length:
		if float(length[gene]) == 0:
			count_length_avg[gene] = "0"
		else:
			average = str(round((float(value) * 1000000) / float(length[gene]) / len(glob.glob("./data/mutation_data/*.maf.txt")),4))
			count_length_avg[gene] = average
	else:
		failure.write(gene + "\t")
for k,v in sorted(count_length_avg.items(),key=lambda x:float(x[1]),reverse=True):
	result.write(k + "\t" + v + "/1Mbp/patient" + "\n")
result.close()
failure.close()
