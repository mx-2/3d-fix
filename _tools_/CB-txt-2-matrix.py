#!/usr/bin/env python3
#
# This python script extracts all constants and matrices 
# from a 3Dmigoto constant buffer dump and converts them to
# an Octave .m file
#
# For the mapping between the raw CB output and the named
# objects in the .m file a map file is used. This map file
# just contains all objects in the same format as in HLSL
# or ASM shaders dumped from 3Dmigoto so they can simply
# copied over.
#
# If the map file is shorter than the input data, the map
# file will repeated.
#
# Example for a very simple map file:
#   # This is a comment
#   float4x4 matrix2;
#   float3 some_data[2];
#   # ignore 3 32bit words of data
#   IGNORE ignore_data[3];
#   ... 
#

import argparse
import re
import sys

# Writes one object from raw data to destination.
def writeMatrix(dst, name, x, y, data, pos):
	count = x*y;
	if y == 1:
		dst.write(name + " = [ ")
	else:
		dst.write(name + " = [ ...\n  ")

	for i in range(0, count):
		if i != 0 and (i % x) != 0:
			dst.write(", ")
		try:
			dst.write(data[pos+i])
		except IndexError:
			dst.write("NaN")
		if i != 0 and (i % x) == x-1 and i != count-1:
			dst.write("; ...\n  ")
	dst.write(" ];\n")

	if y != 1:
		dst.write("\n")

# Analyze command line
parser = argparse.ArgumentParser(description="Constant buffer to matrix converter.")
parser.add_argument("--input", help="Input dump txt file", required=True)
parser.add_argument("--output", help="Output .m file", required=True)
parser.add_argument("--map", help="Input map file", required=True)
parser.add_argument("--prefix", help="Name prefix to be added to all names")
args = vars(parser.parse_args())

if args["input"] != None:
	inputFilename = args["input"]
if args["output"] != None:
	outputFilename = args["output"]
if args["map"] != None:
	mapFilename = args["map"]
if args["prefix"] != None:
	prefix = args["prefix"]
else:
	prefix = ""
	
print("Converting constant buffer...")

# Open files and read strings.
try:
	txtFile = open(inputFilename, 'r')
	if outputFilename == "-":
		outputFile = sys.stdout
	else:
		outputFile = open(outputFilename, 'w')
	lines = txtFile.readlines()
	mapFile = open(mapFilename, 'r')
	cbmap = mapFile.readlines()

except:
	print("Error: Can't open one or more files!")
	sys.exit(2)

# Extract values from raw data
regexCB = re.compile(r"cb[0-9]*?\[[0-9]*?\]\.[xyzw]: (\-?[0-9\.]*e?-?[0-9]*).*$", re.DOTALL)
lines = [regexCB.sub("\\1", x) for x in lines]

# Perpare map file
cbmap = list(filter(lambda a: a != "\n", cbmap))
cbmap = list(filter(lambda a: not a.startswith("#"), cbmap))
regexMap = re.compile((
	r"\/{0,2}[ \t]*?(float[234x]{0,3}) "
	r"([a-zA-Z0-9_]*)(\[?[0-9]*?\]?)( : packoffset\(.*\))?;.*$"), re.DOTALL)
cbmap = [regexMap.sub("\\1\\3 \\2", x) for x in cbmap]

# Get multiplicities
regexArray1 = re.compile(r"^([a-zA-Z0-9_]*?)(x([0-9]*))")
regexArray2 = re.compile(r"^([a-zA-Z0-9_]*?)(\[([0-9]*)\])")
cbmap = [regexArray1.sub("\\1 \\3", x) for x in cbmap]
cbmap = [regexArray2.sub("\\1 \\3", x) for x in cbmap]
cbmap = [x.split() for x in cbmap]

for x in cbmap:
	if len(x) != 3:
		x.insert(1, "1")

# Process data
pos = 0
loop = 0
while pos < len(lines):
	for i,x in enumerate(cbmap):
		if pos >= len(lines):
			break

		name = prefix + x[2]
		if loop > 0:
			name += "_" + str(loop)

		if x[0] == "float":
			writeMatrix(outputFile, name, 1, int(x[1]), lines, pos)
			pos += 1 * int(x[1])
		elif x[0] == "float2":
			writeMatrix(outputFile, name, 2, int(x[1]), lines, pos)
			pos += 2 * int(x[1])
		elif x[0] == "float3":
			writeMatrix(outputFile, name, 3, int(x[1]), lines, pos)
			pos += 3 * int(x[1])
		elif x[0] == "float4":
			writeMatrix(outputFile, name, 4, int(x[1]), lines, pos)
			pos += 4 * int(x[1])
		elif x[0] == "IGNORE":
			pos += 1 * int(x[1])
		else:
			print("Error: Unknown type " + x[0] + "!")
			sys.exit(3)
	loop += 1

