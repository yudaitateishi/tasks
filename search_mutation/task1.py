#!usr/bin/env python

import sys

#check args
if len(sys.argv) < 4:
	print('Usage: #python task1.py input_file(.maf.txt) output_list output_count')
	quit()

#count mutation
mutation_count = {}
output_list = []
silent = ["Silent","Intron","3'UTR","5'UTR","5'Flank","De_novo_Start_Ins","De_novo_Start_Del","RNA","IGR"]
for maf_file in sys.argv:
	if maf_file != "task1.py":
		mutation_list = []
		with open(maf_file,'r') as maf_data:
			for line in maf_data:
				mutation_list.append(line[:-1].rstrip("\n").split("\t"))
		#check 1st line is header or not
		while True:
			for first_line in mutation_list[0]:
				position = mutation_list[0].index(first_line)
				if first_line == mutation_list[1][position] or first_line == mutation_list[2][position]:
					break
				elif first_line == mutation_list[0][-1]:
					mutation_list.pop(0)
					break
				else:
					continue
			break
		#count mutation(without Unknown gene and silent mutation type) 
		for mutation in mutation_list:
			output_list.append(mutation[0] + "\t" + mutation[8])#mutation[0] = gene name
			if mutation[0] == "Unknown" or mutation[8] in silent:#mutation[8] = mutation type
				continue
			else:
				if mutation[0] in mutation_count:
					mutation_count[mutation[0]] += 1
				else:
					mutation_count[mutation[0]] = 1	

#sort and write result file
with open(sys.argv[2],"w") as result_list:
	result_list.write("\n".join(output_list))
	print("output mutation list")

with open(sys.argv[3],'w') as result_count:
	for k,v in sorted(mutation_count.items(),key=lambda x:int(x[1]),reverse=True):
		result_count.write(k + '\t' + str(v) + '\n')
	print("output mutation count")

