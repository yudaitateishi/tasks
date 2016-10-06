text = open('./results/mutation.txt','r')

textlist = []
for lines in text:
	items = lines[:-1].split('\t')
	textlist.append(items)

text.flush()
text.close()

sort = open('./results/sort.txt','w')
symcount = {}

for lists in textlist:
	if lists[1] == 'Unknown' or lists[2] == 'Silent' or lists[2] == 'Intron' or lists[2] == '3\'UTR' or lists[2] == '5\'UTR':  #exclude Unknown gene and Silent mutations
		pass
	else:
		if lists[1] in symcount:
			symcount[lists[1]] += 1
		else:
			symcount[lists[1]] = 1 #make dictionary{key=gene type,value=number of mutation}

for k,v in sorted(symcount.items(),key=lambda x:x[1],reverse=True):
	sort.write(k + '\t' + str(v) + '\n')	 #sort and write

