#!/usr/bin/env python

'''Takes as input one .fasta file and one .ids file and extracts from the fasta those specified IDs'''

import sys

def get_seqs(fileseq, pos=0):
    dseq = {}
    f = open(fileseq)
    for line in f:
        if line[0] == '>':
            k = line[1:].rstrip().split('|')[pos]
            dseq[k] = ''
            continue
        dseq[k] = dseq[k] + line.rstrip()
    return dseq


if __name__ == '__main__':
    fileids = sys.argv[1]
    fileseq = sys.argv[2]
    pos = 0 
    if len(sys.argv)>3: 
        pos = int(sys.argv[3]) - 1

    dseq = get_seqs(fileseq, pos)
    ids = open(fileids).read().rstrip().split('\n')
    for i in ids:
        if dseq.get(i, 0) != 0:
            print('>' + i + '\n' + dseq[i])
 