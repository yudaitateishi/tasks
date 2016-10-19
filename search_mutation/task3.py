#!/usr/bin/env python

import sys
import glob

#check argv
if len(sys.argv) < 4:
	print("Usage: #python task3.py mutation_count_file length_file output_file")
	quit()

#open mutation count
mutation = {}
with open(sys.argv[1],"r") as mutation_file:
	for mutation_line in mutation_file:
		mutation_items = mutation_line[:-1].split("\t")
		mutation[mutation_items[0]] = mutation_items[1]
#open gene length
length = {}
with open(sys.argv[2],"r") as length_file:
	for length_line in length_file:
		length_items = length_line[:-1].split("\t")
		length[length_items[0]] = length_items[1]

count_length_avg = {}

failure = open("./results/failure.txt","w")

for gene,value in mutation.items():
	if gene in length:
		if float(length[gene]) == 0:
			count_length_avg[gene] = "0"
		else:
			average = str(round((float(value) * 1000000) / float(length[gene]),4))
			count_length_avg[gene] = average
	elif gene not in length:
		failure.write(gene + "\t")
	else:
		print("ERROR")
		quit()
failure.close()
with open(sys.argv[3],"w") as result:
	for k,v in sorted(count_length_avg.items(),key=lambda x:float(x[1]),reverse=True):
		result.write(k + "\t" + v + "/1Mbp" + "\n")
	print("output count/length")
	print("no length gene in ./results/failure.txt")
