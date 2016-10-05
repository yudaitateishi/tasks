sort = open('./results/sort.txt','r')
sortdict = {}
for line in sort:
	item = line[:-1].split('\t')
	sortdict[item[0]] = item[1]
sort.close()
#pick data from sort.txt as dictionary{key=gene type:value=number of mutation}

length = open('./results/length.txt','r')
lengdict = {}
for line in length:
	item = line[:-1].split('\t')
	lengdict[item[0]] = item[1]
length.close()
#pick data from length.txt as dictionary{key=gene type:value=length of gene} 

mcorrect = open('./results/correct.txt','w')
fail = open('./results/fail.txt','w')
for k,v in sortdict.items():
	if k in lengdict:
		correct = str(float(v) / float(lengdict[k]))
		mcorrect.write(k + '\t' + correct + '\n')
	else:
		fail.write(k + '\n')
mcorrect.close()
fail.close()

