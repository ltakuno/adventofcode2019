def read_code():
	with open("input.txt", "r") as filestream:
		for line in filestream:
			code = line.split(",")
	return [int(c) for c in code]


if __name__ == "__main__":
	code = read_code()

	i = 0
	opcode = code[i]
	code[1] = 12
	code[2] = 2
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

	for c in code:
		print(c)
