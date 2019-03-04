#! /usr/bin/python3
import sys
infile = open(sys.argv[1],"r").read().strip().split('\n')
fin = open("dictall.txt","r").read().strip().split('\n')
outfile = open(sys.argv[2],'w')
keydict = {}
num = len(infile[0])
dict = {word for word in fin if len(word) == num}
az = 'abcdefghijklmnopqrstuvwxyz'
cur = 1
for l in dict:
        keydict[l] = []
        for x in range(num):
            for y in range(26):
                if(az[y]!= l[x]):
                    q = l[0:x] + az[y] + l[(x+1):]
                    if (q in dict):
                        keydict[l].append(q)

for line in infile:

    outfile.write(line +','+ str(len(keydict[line]))+'\n')
outfile.close()
