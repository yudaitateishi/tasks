#!usr/bin/env python

import sys

#check args
if len(sys.argv) < 2:
	print('Usage: #python task1.py .maf.txt')
	quit()
list_empty = open("./results/mutation_list.txt","w")
list_empty.close()

#count mutation
mutation_count = {}
silent = ["Silent","Intron","3'UTR","5'UTR","5'Flank","De_novo_Start_Ins","De_novo_Start_Del","RNA","IGR"]
for maf_file in sys.argv:
	if maf_file != "task1.py":
		mutation_list = []
		with open(maf_file,'r') as maf_data:
			for line in maf_data:
				mutation_list.append(line[:-1].rstrip("\n").split("\t"))
		#check 1st line header or not
		while True:
			for value in mutation_list[0]:
				if value == mutation_list[1][mutation_list[0].index(value)]:
					break
				elif value == mutation_list[0][-1]:
					mutation_list.pop(0)
					break
				else:
					continue
			break
		#count mutation(without gene = Unknown and mutation type = silent) 
		for mutation in mutation_list:
			with open("./results/mutation_list.txt","a+") as list_output:
				list_output.write(mutation[0] + "\t" + mutation[8] + "\n")
			if mutation[0] == "Unknown" or mutation[8] in silent:
				continue
			else:
				if mutation[0] in mutation_count:
					mutation_count[mutation[0]] += 1
				else:
					mutation_count[mutation[0]] = 1	

#sort and write result file
with open('./results/mutation_count.txt','w') as result:
	for k,v in sorted(mutation_count.items(),key=lambda x:int(x[1]),reverse=True):
		result.write(k + '\t' + str(v) + '\n')
	print("result file in ./results/mutation_count.txt")

