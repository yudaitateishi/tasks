def tcvconvert(arg1,arg2):
	for line in arg1:
		items = line[:-1].split('\t')
		arg2.append(items)

def sortwrite(arg3,arg4):
	for k,v in sorted(arg3.items(),key=lambda x:x[1],reverse=True):
		arg4.write(k + '\t' + str(v) + '\n')


import glob
txt = glob.glob('./data/mutation_data/*.maf.txt')
for files in txt:
	tcga = open(files,'r')
	tcgalist = []
	tcvconvert(tcga,tcgalist)
	tcga.close()
	tcgalist.pop(0)
	mutlist = []
	for lists in tcgalist:
		mutlist.append([lists[15],lists[0],lists[8]])
	wfile = open('./results/mutation.txt','a+')
	for l in mutlist:
		for i in l:
			wfile.write(str(i) + '\t')
		wfile.write('\n')
	wfile.flush()
	wfile.close()


mutation = open('./results/mutation.txt','r')
mutlist = []
tcvconvert(mutation,mutlist)
mutation.close()

sort = open('./results/sort.txt','w')
symcount = {}

silent = ['Silent','Intron','3\'UTR','5\'UTR','5\'Flank']
for lists in mutlist:
	if lists[1] == 'Unknown' or lists[2] in silent:
		pass
	else:
		if lists[1] in symcount:
			symcount[lists[1]] += 1
		else:
			symcount[lists[1]] = 1
sortwrite(symcount,sort)
sort.close()


gene = open('./data/genelen/refGene.txt','r')
genelist = []
tcvconvert(gene,genelist)
gene.close()

genelength = {}
for lists in genelist:
	starts = lists[9].split(',')
	starts.pop(-1)
	ends = lists[10].split(',')
	ends.pop(-1)
	if lists[12] in genelength:
		genelength[lists[12]].append(sum(map(int,ends)) - sum(map(int,starts)))
	else:
		newgene = []
		newgene.append(sum(map(int,ends)) - sum(map(int,starts)))
		genelength[lists[12]] = newgene

length = open('./results/length.txt','w')
for k,v in genelength.items():
	geneave = sum(map(int,v)) / float(len(v))
	length.write(k + '\t' + str(geneave) + '\n')
length.close()


sort = open('./results/sort.txt','r')
sortdict = {}
for line in sort:
	items = line[:-1].split('\t')
	sortdict[items[0]] = items[1]
sort.close()

genelen = open('./results/length.txt','r')
lengdict = {}
for line in genelen:
	items = line[:-1].split('\t')
	lengdict[items[0]] = items[1]
length.close()

correctdict = {}
mcorrect = open('./results/correct.txt','w')
fail = open('./results/fail.txt','w')
for k,v in sortdict.items():
	if k in lengdict:
		correct = str((float(v) / float(lengdict[k])) / 1000000)
		correctdict[k] = correct
	else:
		fail.write(k + '\t')
sortwrite(sortdict,mcorrect)
mcorrect.close()
fail.close()


