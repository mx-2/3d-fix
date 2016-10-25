#!/usr/bin/python

import re
import sys

regs = \
{
	'r0': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r1': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r2': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r3': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r4': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r5': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r6': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r7': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r8': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r9': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r10': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r11': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r12': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r13': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r14': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r15': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r16': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r17': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r18': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r19': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r20': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r21': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r22': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r23': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r24': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r25': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r26': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r27': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r28': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r29': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r30': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0},
	'r31': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0}
}

# Applies input swizzels to register and returns the
# resulting four element vector.
# reg: string r + [0-31] + {.<xyzw>{4}}
def swizzle(reg):
	parts = reg.split(".")
	sign = 1;
	if parts[0].startswith("-"):
		sign = -1;
		parts[0] = parts[0][1:]

	if len(parts) == 1:
		coords = "xyzw"
	else:
		coords = parts[1]

	for i in range(len(coords), 4):
		coords = coords + coords[-1]
	return {'x': float(regs[parts[0]][coords[0]] * sign),
			'y': float(regs[parts[0]][coords[1]] * sign),
			'z': float(regs[parts[0]][coords[2]] * sign),
			'w': float(regs[parts[0]][coords[3]] * sign)}

# Performs mathematical operations with two registers
# and returns the result.
def math(op, r1, r2):
	if op == "add":
		return {'x': r1['x'] + r2['x'],
				'y': r1['y'] + r2['y'],
				'z': r1['z'] + r2['z'],
				'w': r1['w'] + r2['w']}
	elif op == "sub":
		return {'x': r1['x'] - r2['x'],
				'y': r1['y'] - r2['y'],
				'z': r1['z'] - r2['z'],
				'w': r1['w'] - r2['w']}
	elif op == "mul":
		return {'x': r1['x'] * r2['x'],
				'y': r1['y'] * r2['y'],
				'z': r1['z'] * r2['z'],
				'w': r1['w'] * r2['w']}
	elif op == "div":
		return {'x': r1['x'] / r2['x'],
				'y': r1['y'] / r2['y'],
				'z': r1['z'] / r2['z'],
				'w': r1['w'] / r2['w']}
	else:
		raise Exception("Invalid math")

# Assigns value "val" to register "reg" observing output swizzles.
# reg: string r + [0-31]
# val: dictionary with x, y, z, w
def assign(reg, val):
	parts = reg.split(".")

	if len(parts) == 1:
		coords = "xyzw"
	else:
		coords = parts[1]

	try:
		x = coords.index("x")
		regs[parts[0]]["x"] = val["x"]
	except:
		pass

	try:
		x = coords.index("y")
		regs[parts[0]]["y"] = val["y"]
	except:
		pass

	try:
		x = coords.index("z")
		regs[parts[0]]["z"] = val["z"]
	except:
		pass

	try:
		x = coords.index("w")
		regs[parts[0]]["w"] = val["w"]
	except:
		pass

# Print register contents to screen
def printRegs():
	for n in range(0, 32):
		sys.stdout.write("r" + str(n) + ": ")
		sys.stdout.write("[" + str(regs["r" + str(n)]["x"]) + ", ")
		sys.stdout.write(str(regs["r" + str(n)]["y"]) + ", ")
		sys.stdout.write(str(regs["r" + str(n)]["z"]) + ", ")
		sys.stdout.write(str(regs["r" + str(n)]["w"]) + "]\n")
		if (n+1) % 4 == 0:
			print("")

condStack = [];

# Checks if current op shall be executed
def Execute():
	exec_ = 1
	for x in condStack:
		if x == 0:
			exec_ = 0
	return exec_

# Get filenames from arguments
try:
	asmFilename = sys.argv[1]
except:
	print("Error: Invalid argument count")
	print("Usage: ./shaderVM.py <input asm file>")
	sys.exit(1)

asmfile = open(asmFilename, "r")
content = asmfile.read()
asmfile.close()

# Prepare input:
# - Remove comments, leading spaces, empty lines and add a ','
#   as delimiter between op and first parameter.
# - Convert the special PRINT comment to a pseudo op
# - Convert the special SETR comment to a pseudo op
# - Split string into lines
regex = re.compile(r"^\s*?//\s*?PRINT", re.MULTILINE)
content = regex.sub(r"PRINT", content)
regex = re.compile(r"^\s*?//\s*?SETR", re.MULTILINE)
content = regex.sub(r"SETR", content)
regex = re.compile(r"//.*?$", re.MULTILINE)
content = regex.sub(r"", content)
regex = re.compile(r"^\s*", re.MULTILINE)
content = regex.sub(r"", content)
regex = re.compile(r"^(.*? )", re.MULTILINE)
content = regex.sub(r"\1, ", content)
regex = re.compile(r"^\s*$", re.MULTILINE)
content = regex.sub(r"", content)
content = re.sub("\s*$", "", content);
content = content.split("\n")

for line in content:
	tokens = line.split(",")
	for x in range(0, len(tokens)):
		tokens[x] = tokens[x].replace(" ", "")

	if tokens[0] == "def":
		regs[tokens[1]] = { 'x': float(tokens[2]),
							'y': float(tokens[3]),
							'z': float(tokens[4]),
							'w': float(tokens[5])}
	elif tokens[0] == "PRINT":
		if Execute() == 1:
			print(tokens[1])
			printRegs()
			try:
				input("")
			except:
				pass
	elif tokens[0] == "SETR":
		regs[tokens[1]] = { 'x': float(tokens[2]),
							'y': float(tokens[3]),
							'z': float(tokens[4]),
							'w': float(tokens[5])}
	elif tokens[0] == "mov":
		if Execute() == 1:
			assign(tokens[1], swizzle(tokens[2]))
	elif tokens[0] == "mul":
		if Execute() == 1:
			assign(tokens[1], math("mul", swizzle(tokens[2]), swizzle(tokens[3])))
	elif tokens[0] == "add":
		if Execute() == 1:
			assign(tokens[1], math("add", swizzle(tokens[2]), swizzle(tokens[3])))
	elif tokens[0] == "sub":
		if Execute() == 1:
			assign(tokens[1], math("sub", swizzle(tokens[2]), swizzle(tokens[3])))
	elif tokens[0] == "rcp":
		if Execute() == 1:
			assign(tokens[1], math("div", {'x': 1, 'y': 1, 'z': 1, 'w': 1}, swizzle(tokens[2])))
	elif tokens[0] == "if_eq":
		if math("sub", swizzle(tokens[1]), swizzle(tokens[2]))["x"] != 0:
			condStack.append(0)
		else:
			condStack.append(1)
	elif tokens[0] == "else":
		if condStack[-1] == 1:
			condStack[-1] = 0
		else:
			condStack[-1] = 1		
	elif tokens[0] == "endif":
		condStack.pop()
	else:
		raise Exception("Invalid op found:" + tokens[0])

printRegs()
		
