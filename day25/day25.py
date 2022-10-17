TESTLEN = 10000

insts = []

def reg_or_val(token):
    if token[0] in '-0123456789':
        return int(token)
    else:
        return regs[ord(token)-ord('a')]

with open('day25/input.txt') as h:
    for line in h:
        line = line.strip()
        insts.append(line)

def run(insts, regs):
    # regs[4] is pc
    bit = 0
    nout = 0
    while regs[4] < len(insts):
        inst = insts[regs[4]]
        tokens = inst.split()
        if tokens[0] == 'cpy':
            if tokens[2] not in '-0123456789':
                regs[ord(tokens[2])-ord('a')] = reg_or_val(tokens[1])
        elif tokens[0] == 'inc':
            if tokens[1] not in '-0123456789':
                regs[ord(tokens[1])-ord('a')] += 1
        elif tokens[0] == 'dec':
            if tokens[1] not in '-0123456789':
                regs[ord(tokens[1])-ord('a')] -= 1
        elif tokens[0] == 'jnz':
            if reg_or_val(tokens[1]) != 0:
                regs[4] += reg_or_val(tokens[2])
                continue
        elif tokens[0] == 'out':
            x = reg_or_val(tokens[1])
            if x != bit:
                return False
            bit = 1 - bit
            nout += 1
            if nout >= TESTLEN:
                return True
        else:
            raise ValueError('invalid instruction: ' + inst)
        regs[4] += 1
    return False

a = 0
while True:
    regs = [0 for _ in range(5)]
    regs[0] = a
    if run(insts, regs):
        print(a)
        break
    a += 1
