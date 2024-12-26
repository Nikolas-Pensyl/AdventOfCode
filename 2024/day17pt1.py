data = [line.split() for line in open('./Inputs/day17.txt').read().splitlines()]


instruct = 0
ops = [0, 1, 2, 3, int(data[0][-1]), int(data[1][-1]), int(data[2][-1])]
program = list(map(int, data[4][-1].split(',')))
print(ops)

out = ""
while instruct<len(program):
    opc = program[instruct]
    opd = program[instruct+1]

    if opc==0:
        ops[4] = ops[4]//pow(2, ops[opd])

    elif opc==1:
        ops[5] = ops[5]^opd

    elif opc==2:
        ops[5] = ops[opd]%8

    elif opc==3:
        if ops[4]!=0:
            instruct = opd
            continue

    elif opc==4:
        ops[5] ^=ops[6]

    elif opc==5:
        out += str(ops[opd]%8)+","

    elif opc==6:
        ops[5] = ops[4]//pow(2, ops[opd])

    elif opc==7:
        ops[6] = ops[4]//pow(2, ops[opd])


    instruct +=2

print(out)