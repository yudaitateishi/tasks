#!/usr/bin/env python

import sys
import glob

#check argv
if len(sys.argv) < 3:
	print("Usage: #python task3.py mutation length")
	quit()

#open mutation count
mutation = {}
with open(sys.argv[1],"r") as mutation_file:
	for line in mutation_file:
		items = line[:-1].split("\t")
		mutation[items[0]] = items[1]
#open gene length
length = {}
with open(sys.argv[2],"r") as length_file:
	for line in length_file:
		items = line[:-1].split("\t")
		length[items[0]] = items[1]

count_length_avg = {}

failure = open("./results/failure.txt","w")

for gene,value in mutation.items():
	if gene in length:
		if float(length[gene]) == 0:
			count_length_avg[gene] = "0"
		else:
			average = str(round((float(value) * 1000000) / float(length[gene]),4))
			count_length_avg[gene] = average
	else:
		failure.write(gene + "\t")
failure.close()
with open("./results/count_length_avg.txt","w") as result:
	for k,v in sorted(count_length_avg.items(),key=lambda x:float(x[1]),reverse=True):
		result.write(k + "\t" + v + "/1Mbp" + "\n")
	print("result file is ./results/count_length_avg.txt")

