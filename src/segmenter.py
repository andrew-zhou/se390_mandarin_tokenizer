#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from nltk.tokenize.stanford_segmenter import StanfordSegmenter as Segmenter
from sys import stdout
from codecs import getwriter, getreader
segmenter = Segmenter(path_to_model="../resources/data/pku.gz", 
											path_to_dict="../resources/data/dict-chris6.ser.gz",
											path_to_sihan_corpora_dict="../resources/data") # Make sure to unzip resources.zip into current directory first
stdout = getwriter("utf8")(stdout) # Enable utf8 encoding for stdout

# Get input
lines = []
while True:
	line = raw_input().decode('utf8')
	if len(line.strip()) == 0:
		break
	lines.append(line)
print 'Beginning segmentation'

# Test for now
segments = [segmenter.segment(line) for line in lines]

for index in xrange(len(segments)):
	print 'Line: ' + lines[index]
	print 'Segments for line ' + str(index)
	for segment in segments[index].split(' '):
		print segment