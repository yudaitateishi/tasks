gene = open('./data/genelen/refGene.txt','r')
genelist = []

for line in gene:
	items = line[:-1].split('\t')
	genelist.append(items)

genelens = {}
#make dictionary{key=gene type:value=[length1,length2,length3,...]}
for lists in genelist:
	exonstart = lists[9].split(',')
	exonstart.pop(-1)
	exonend = lists[10].split(',')
	exonend.pop(-1)
	if lists[12] in genelens:
		genelens[lists[12]].append(sum(map(int,exonend)) - sum(map(int,exonstart)))
	else:
		newgene = []
		newgene.append(sum(map(int,exonend)) - sum(map(int,exonstart)))
		genelens[lists[12]] = newgene

length = open('./results/length.txt','w')

for k,v in genelens.items():
	geneave = sum(map(int,v)) / float(len(v)) #some genes have some length data,so take the average
	length.write(k + '\t' + str(geneave) + '\n')

