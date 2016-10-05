#-*- coding:utf-8 -*-

import sys
args = sys.argv

text = open(args[1],'r')
textlist = []   

for line in text:
	items = line[:-1].split('\t')
	textlist.append(items)

textlist.pop(0)  #input *.maf.txt and into list. textlist[0] is index 

mutlist = []
for lists in textlist:
	mutlist.append([lists[15],lists[0],lists[8]]) #pickup(Patient number,gene type,mutation type)

wfile = open('./results/mutation.txt','a+')
for l in mutlist:
	for i in l:
		wfile.write(str(i) + '\t')
	wfile.write('\n') #write data as tsv

wfile.flush()
wfile.close()



