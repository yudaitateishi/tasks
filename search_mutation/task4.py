#!/usr/bin/env python

import sys
import pandas as pd
import pyper
r = pyper.R(use_pandas = "True")

if len(sys.argv) < 4:
	print("Usage: #python task4.py mutation_list mutation_count output_file")
	quit()
#open mutation list
mutation_list = []
with open(sys.argv[1],"r") as mutation_file:
	for line in mutation_file:
		mutation_list.append(line[:-1].split("\t"))#make list [[gene name,mutation type],...]
#open mutation count
mutation_count = {}
with open(sys.argv[2],'r') as count_file:
	for line in count_file:
		items = line[:-1].split("\t")
		mutation_count[items[0]] = int(items[1])#make dict {key=gene name:value=mutation count,...}

#count truncating mutation
truncating_type = ['Frame_Shift_Ins','Frame_Shift_Del','Nonsense_Mutation','Splice_Site']
truncating_count = {}
for mutation in mutation_list:#make dict {key=gene name:value=truncating count,...}
	if mutation[1] in truncating_count:#mutation[0] = gene name
		if mutation[2] in truncating_type:#mutation[1] = mutation type
			truncating_count[mutation[1]] += 1.0
	else:
		if mutation[2] in truncating_type:
			truncating_count[mutation[1]] = 1.0

#take average
truncating_avg = {}
p_value = {}
for gene,count in mutation_count.items():
	if gene in truncating_count:
		truncating_avg[gene] = round(truncating_count[gene] / count,4)
	else:
		truncating_avg[gene] = 0
		truncating_count[gene] = 0
	r.assign("T",count)
	r.assign("S",truncating_count[gene])
	r("R<-binom.test(S,T,0.5,alternative=\"greater\")")
	p_value[gene] = r.get("R$p.value")


with open(sys.argv[3],'w') as result:
	result.write("gene\tmutation\ttruncating\taverage\tp-value\n") 
	for k,v in sorted(p_value.items(),key=lambda x:x[1]):
		result.write(k + '\t'+ str(mutation_count[k]) + '\t' + str(truncating_count[k]) + "\t" + str(truncating_avg[k])+ "\t" + str(v) + '\n')
	print("output truncating average")



