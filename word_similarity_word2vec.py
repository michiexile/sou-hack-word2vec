#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import regex
import logging
import gensim
from gensim import corpora, models
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m","--model_file", help="""
Name for the model file you want to use e.g. "20tal.model" 
The file is supposed to be stored in the current folder if not specified
specificly.""",default="",required=True)
parser.add_argument("-w","--word", help="""
Word to run similarity for. returns 10 related terms. 
specificly.""",default="",required=True)


args = parser.parse_args()
input = args.model_file

model = models.Word2Vec.load(input)
word = args.word

print(model.similarity(word))