#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import regex
import logging
import gensim
from gensim import corpora, models
import argparse
from collections import defaultdict
import json

parser = argparse.ArgumentParser()
parser.add_argument("-m","--model_file", help="""
Name for the model file you want to use e.g. "20tal.model" 
The file is supposed to be stored in the current folder if not specified
specificly.""",required=True)
parser.add_argument("-w","--word", help="""
Word to run similarity for. returns 10 related terms. 
specificly.""",required=True)
parser.add_argument("-N", help="""
# neighbors to compute for each step.""",default=5,required=True)


args = parser.parse_args()
input = args.model_file
N = int(args.N)

model = models.Word2Vec.load(input)
word = args.word


neighbors = model.most_similar(word, topn=N)
nbrs = dict()
nbrs[word] = {nbr[0] for nbr in neighbors}

for nbr in neighbors:
	nextdoor = model.most_similar(nbr[0], topn=N)
	if nbr[0] not in nbrs: nbrs[nbr[0]] = set()
	nbrs[nbr[0]] |= {nd[0] for nd in nextdoor}

#print(nbrs)
words = list({w for w in nbrs}.union({w for k in nbrs for w in nbrs[k]}))
#print(words)

ret = {
	"nodes" : [
		{"name": name} for name in words
	],
	"links" : [
		{"source": words.index(source), "target": words.index(target)} 
		for source in nbrs for target in nbrs[source]
	]
}

print(json.dumps(ret))
