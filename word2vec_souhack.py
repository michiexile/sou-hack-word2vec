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

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, fname):
        self.fname = fname
    def __iter__(self):
        for line in open(self.fname):
            cleaned = regex.sub(r"[\:\!\?\.\,]","",line)
            tokens = cleaned.split()
            yield tokens

sentences = MySentences("/Users/mos/Downloads/SOUtxtAllBigFile.txt")
model = models.Word2Vec(sentences,size=200,window=5,min_count=30,workers=4)