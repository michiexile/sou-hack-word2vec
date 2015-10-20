#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Run this script direclty in the terminal to get the logging output:
# write "python word2vec_souhack.py"
# NOTE! Download textfile to run on from 
# http://www.christopherkullenberg.se/sorlet-fran-statens-offentliga-utredningar/


import regex
import logging
import gensim
from gensim import corpora, models
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="""
Name for the file you want to analyze e.g. "SOUtxtAllBigFile.txt" 
The file is supposed to be stored in the current folder if not specified
specificly.""",default="",required=True)
parser.add_argument("-o","--output", help="""
Name for the model file you create e.g. "20talet.model" 
The file is stored in the current folder if not specified
specificly.""",default="./my_model.model",required=True)

args = parser.parse_args()

outfile = args.output
infile = args.input

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences:
	def __init__(self, infile):
		self.infile = infile
	def __iter__(self):
		for line in open(self.infile):
			cleaned = regex.sub(r"[\:\!\?\.\,]","",line)
			tokens = cleaned.split()
			yield tokens

sentences = MySentences("/Users/mos/Downloads/SOUtxtAllBigFile.txt")
model = models.Word2Vec(sentences,size=200,window=5,min_count=30,workers=4)

model.save(outfile)