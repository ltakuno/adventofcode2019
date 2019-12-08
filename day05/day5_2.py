def read_code():
    with open("input.txt", "r") as filestream:
        for line in filestream:
            code = line.split(",")
    return [int(c) for c in code]

if __name__ == "__main__":
    code = read_code()

    i = 0
    opcode = code[i] % 100
               
    while (opcode < 99):
        if (opcode == 1):
            mode1 = (code[i] // 100) % 10
            mode2 = (code[i] // 1000) % 10
            op1 = code[i+1]
            op2 = code[i+2]
            op3 = code[i+3]

            if mode1 == 0:
                val1 = code[op1]
            else:
                val1 = op1

            if mode2 == 0:
                val2 = code[op2]
            else:
                val2 = op2

            code[op3] = val1 + val2
            #print('add %d, %d, %d'%(op1, op2, op3))
            i += 4
        elif (opcode == 2):
            mode1 = (code[i] // 100) % 10
            mode2 = (code[i] // 1000) % 10
            op1 = code[i+1]
            op2 = code[i+2]
            op3 = code[i+3]

            if mode1 == 0:
                val1 = code[op1]
            else:
                val1 = op1

            if mode2 == 0:
                val2 = code[op2]
            else:
                val2 = op2

            code[op3] = val1 * val2
            #print('mul %d, %d, %d'%(op1, op2, op3))
            i += 4
        elif (opcode == 3):
            op1 = code[i+1] 
            code[op1] = int(input())
            #print('read %d' % (op1))
            i += 2
        elif (opcode == 4):
            op1 = code[i+1]
            mode1 = (code[i] // 100) % 10
            if mode1 == 0:
                val1 = code[op1]
            else:
                val1 = op1
            
            #print('print %d' % (val1))
            print(val1)
            i += 2
        elif (opcode == 5):
            op1 = code[i+1]
            op2 = code[i+2]

            mode1 = (code[i] // 100) % 10
            mode2 = (code[i] // 1000) % 10

            if mode1 == 0:
                val1 = code[op1]
            else:
                val1 = op1

            if mode2 == 0:
                val2 = code[op2]
            else:
                val2 = op2
            
            if val1 <> 0:
                i = val2
            else:
                i += 3
            #print('jmp %d, %d' % (op1, op2))
        elif (opcode == 6):
            op1 = code[i+1]
            op2 = code[i+2]

            mode1 = (code[i] // 100) % 10
            mode2 = (code[i] // 1000) % 10

            if mode1 == 0:
                val1 = code[op1]
            else:
                val1 = op1

            if mode2 == 0:
                val2 = code[op2]
            else:
                val2 = op2
            
            if val1 == 0:
                i = val2 
            else:
                i += 3
            #print('jnz %d, %d' % (op1, op2))
        elif (opcode == 7):
            mode1 = (code[i] // 100) % 10
            mode2 = (code[i] // 1000) % 10
            op1 = code[i+1]
            op2 = code[i+2]
            op3 = code[i+3]

            if mode1 == 0:
                val1 = code[op1]
            else:
                val1 = op1

            if mode2 == 0:
                val2 = code[op2]
            else:
                val2 = op2

            if val1 < val2:
                code[op3] = 1
            else: 
                code[op3] = 0
            i += 4
            #print('slt %d, %d, %d' % (val1, val2, op3))
        elif (opcode == 8):
            mode1 = (code[i] // 100) % 10
            mode2 = (code[i] // 1000) % 10
            op1 = code[i+1]
            op2 = code[i+2]
            op3 = code[i+3]

            if mode1 == 0:
                val1 = code[op1]
            else:
                val1 = op1

            if mode2 == 0:
                val2 = code[op2]
            else:
                val2 = op2

            if val1 == val2:
                code[op3] = 1
            else: 
                code[op3] = 0
            i += 4
            #print('seq %d, %d, %d' % (val1, val2, op3))
        else:
            print('Invalid opcode %d' % (opcode))
            break 
        opcode = code[i] % 100
        #print(opcode)       
