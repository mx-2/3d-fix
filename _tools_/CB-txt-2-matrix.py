#!/usr/bin/env python

import re
import sys

# get filenames from arguments
try:
	inputFilename =  sys.argv[1]
	outputFilename = sys.argv[2]
except:
	print("Error: Invalid argument count!")
	print("Usage: CB-txt-2-m.py 'input_txt_file' 'output_m_file'")
	sys.exit(1)
	
print("Converting constant buffer...\n")

# open files and read strings
try:
	txtFile = open(inputFilename, 'r')
	if outputFilename == "-":
		outputFile = sys.stdout
	else:
		outputFile = open(outputFilename, 'w')
	lines = txtFile.readlines()
except:
	print("Error: Can't open one or more files!")
	sys.exit(2)

regex = re.compile(r"cb[0-9]*?\[[0-9]*?\]\.[xyzw]: (\-?[0-9\.]*).*$", re.DOTALL)
lines = [regex.sub("\\1", x) for x in lines]

outputFile.write("cb = [ ...\n  ")

for pos, line in enumerate(lines):
	if pos != 0 and (pos % 4) != 0:
		outputFile.write(", ")
	outputFile.write(line)
	if pos != 0 and (pos % 4) == 3 and pos != len(lines)-1:
		outputFile.write("; ...\n  ")

outputFile.write(" ];\n")

