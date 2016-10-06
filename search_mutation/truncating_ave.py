mutation = open('./results/mutation.txt','r')
mutlist = []
for line in mutation:
	items = line[:-1].split('\t')
	mutlist.append(items)
mutation.close()

sort = open('./results/sort.txt','r')
sortdict = {}
for line in sort:
	items = line[:-1].split('\t')
	sortdict[items[0]] = int(items[1])
sort.close()

truncating = {}
for lists in mutlist:
	if lists[1] in truncating:
		if lists[2] == 'Frame_Shift_Ins' or lists[2] == 'Frame_Shift_Del' or lists[2] == 'Nonsense_Mutation':
			truncating[lists[1]] += 1.0
	else:
		if lists[2] == 'Frame_Shift_Ins' or lists[2] == 'Frame_Shift_Del' or lists[2] == 'Nonsense_Mutation':
			truncating[lists[1]] = 1.0

truncating_ave = {}
for k,v in sortdict.items():
	if k in truncating:
		truncating_ave[k] = truncating[k] / v
	else:
		truncating_ave[k] = 0

trunc = open('./results/truncating_ave.txt','w')
for k,v in sorted(truncating_ave.items(),key=lambda x:x[1],reverse=True):
	trunc.write(k + '\t' + str(v) + '\n')
trunc.flush()
trunc.close()


