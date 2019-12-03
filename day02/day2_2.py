def read_code():
	with open("input.txt", "r") as filestream:
		for line in filestream:
			code = line.split(",")
	return [int(c) for c in code]

def execute_code_for(v1, v2):
	code = read_code()

	i = 0
	opcode = code[i]
	code[1] = v1
	code[2] = v2
	while (opcode < 99):
		op1 = code[i+1]
		op2 = code[i+2]
		op3 = code[i+3]
		if (opcode == 1):
			code[op3] = code[op1] + code[op2]
		elif (opcode == 2):
			code[op3] = code[op1] * code[op2]
		i += 4
		opcode = code[i]

	return code[0]

if __name__ == '__main__':
	for noum in range(99):
		for verb in range(99):
			r = execute_code_for(noum, verb)
			if (r == 19690720):
				print('noum: %d, verb: %d, result:%d' % (noum, verb, r))
