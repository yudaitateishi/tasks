def tcvconvert(arg1,arg2):
	for line in arg1:
		items = line[:-1].split('\t')
		arg2.append(items)

def sortwrite(arg3,arg4):
	for k,v in sorted(arg3.items(),key=lambda x:float(x[1]),reverse=True):
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

silent = ['Silent','Intron','3\'UTR','5\'UTR','5\'Flank','De_novo_Start_*','RNA','IGR']
for lists in mutlist:
	if lists[1] == 'Unknown' or lists[2] in silent:
		pass
	else:
		if lists[1] in symcount:
			symcount[lists[1]] += 1
		else:
			symcount[lists[1]] = 1
sortwrite(symcount,sort)
sort.flush()
sort.close()


gene = open('./data/genelen/refGene.txt','r')
genelist = []
tcvconvert(gene,genelist)
gene.close()

genelength = {}
for lists in genelist:
	starts = lists[9].split(',')
	starts.pop(-1)
	chs = lists[6]
	exons = []
	ends = lists[10].split(',')
	ends.pop(-1)
	che = lists[7]
	exone = []
	for v in starts:
		num = starts.index(v)
		if che > ends[num] > starts[num] > chs:
			exons.append(starts[num])
			exone.append(ends[num])
		elif che > ends[num] > chs > starts[num]:
			exons.append(chs)
			exone.append(ends[num])
		elif ends[num] > che > starts[num] > chs:
			exons.append(starts[num])
			exone.append(che)
	leng = sum(map(int,exone)) - sum(map(int,exons))
	if lists[12] in genelength:
		if leng < genelength[lists[12]]:
			pass
	else:
		genelength[lists[12]] = leng
length = open('./results/length.txt','w')
sortwrite(genelength,length)
length.flush()
length.close()


sort2 = open('./results/sort.txt','r')
sortdict = {}
for line in sort2:
	items = line[:-1].split('\t')
	sortdict[items[0]] = items[1]
sort2.close()

genelen = open('./results/length.txt','r')
lengdict = {}
for line in genelen:
	items = line[:-1].split('\t')
	lengdict[items[0]] = items[1]
genelen.close()

correctdict = {}
mcorrect = open('./results/correct.txt','w')
fail = open('./results/fail.txt','w')
for k,v in sortdict.items():
	if k in lengdict:
		if float(lengdict[k]) == 0:
			correctdict[k] = '0'
		else:
			correct = str((float(v) / float(lengdict[k])) * 1000000)
			correctdict[k] = correct
	else:
		fail.write(k + '\t')
sortwrite(correctdict,mcorrect)
mcorrect.flush()
mcorrect.close()
fail.flush()
fail.close()


