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
	if lists[1] != 'Unknown' and lists[2] != 'Silent':
		if lists[1] in symcount:
			symcount[lists[1]] += 1
		else:
			symcount[lists[1]] = 1

for k,v in sorted(symcount.items(),key=lambda x:x[1],reverse=True):
	sort.write(k + '\t' + str(v) + '\n')	 

