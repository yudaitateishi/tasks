#!/usr/bin/env python

import sys

#check args
if len(sys.argv) < 3:
	print("Usage: #python task2.py GenePred_file output_file")
	quit()

#make refGene data list
gene_list = []
with open(sys.argv[1],'r') as gene_file:
	for line in gene_file:
		gene_list.append(line[:-1].rstrip("\n").split("\t"))

gene_length = {}
for line in gene_list:
	starts = line[9].split(",")
	starts.pop(-1)
	cdstart = line[6]
	read_starts = []
	ends = line[10].split(",")
	ends.pop(-1)
	cdend = line[7]
	read_ends = []
	for value in starts:
		position = starts.index(value)
		if starts[position] < cdstart:#first check where is exon start position
			if ends[position] < cdstart:
				pass
			elif cdstart <= ends[position] < cdend:#check where is exon end position
				read_starts.append(cdstart)
				read_ends.append(ends[position])
			elif cdend <= ends[position]:
				read_starts.append(cdstart)
				read_ends.append(cdend)
			else:
				sys.stderr.write('Error')
				quit()
		elif cdstart <= starts[position]:
			if starts[position] <= ends[position] <= cdend:
				read_starts.append(starts[position])
				read_ends.append(ends[position])
			elif starts[position] <= cdend <= ends[position]:
				read_starts.append(starts[position])
				read_ends.append(cdend)
			elif cdend < starts[position]:
				pass
			else:
				sys.stderr.write('Error')
				quit()
		else:
			sys.stderr.write('Error')
			quit()

	length = sum(map(int,read_ends)) - sum(map(int,read_starts)) + len(read_starts)
	if line[12] in gene_length:
		if length > gene_length[line[12]]:
			gene_length[line[12]] = length
		else:
			pass
	else:
		gene_length[line[12]] = length	

with open(sys.argv[2],"w") as result:
	for k,v in sorted(gene_length.items(),key=lambda x:int(x[1]),reverse=True):
		result.write(k + "\t" + str(v) + "\n")
	print("output gene length")
				
