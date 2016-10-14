#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
	print("Usage: #python task4.py mutation_list mutation_count ")
	quit()
#open mutation list
mutation_list = []
with open(sys.argv[1],"r") as mutation:
	for line in mutation:
		mutation_list.append(line[:-1].split("\t"))
#open mutation count
mutation_count = {}
with open(sys.argv[2],'r') as count:
	for line in count:
		items = line[:-1].split("\t")
		mutation_count[items[0]] = int(items[1])

#count truncating mutation
truncating_type = ['Frame_Shift_Ins','Frame_Shift_Del','Nonsense_Mutation','Splice_Site']
truncating_count = {}
for mutation_type in mutation_list:
	if mutation_type[0] in truncating_count:
		if mutation_type[1] in truncating_type:
			truncating_count[mutation_type[0]] += 1.0
	else:
		if mutation_type[1] in truncating_type:
			truncating_count[mutation_type[0]] = 1.0

#take average
truncating_avg = {}
for gene,count in mutation_count.items():
	if gene in truncating_count:
		truncating_avg[gene] = round(truncating_count[gene] / count,4)
	else:
		truncating_avg[gene] = 0

with open('./results/truncating_avg.txt','w') as result: 
	for k,v in sorted(truncating_avg.items(),key=lambda x:float((x[1]+1)*mutation_count[x[0]]),reverse=True):
		result.write(k + '\t'+ str(mutation_count[k]) + '\t' + str(v) + '\n')
	print("result file is ./results/truncating_avg.txt")



