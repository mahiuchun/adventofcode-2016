# regs[4] is pc
regs = [0 for _ in range(5)]
regs[2] = 1
insts = []

def reg_or_val(token):
    if token[0] in '0123456789':
        return int(token)
    else:
        return regs[ord(token)-ord('a')]

with open('day12/input.txt') as h:
    for line in h:
        line = line.strip()
        insts.append(line)

while regs[4] < len(insts):
    inst = insts[regs[4]]
    tokens = inst.split()
    if tokens[0] == 'cpy':
        regs[ord(tokens[2])-ord('a')] = reg_or_val(tokens[1])
    elif tokens[0] == 'inc':
        regs[ord(tokens[1])-ord('a')] += 1
    elif tokens[0] == 'dec':
        regs[ord(tokens[1])-ord('a')] -= 1
    elif tokens[0] == 'jnz':
        if reg_or_val(tokens[1]) != 0:
            regs[4] += int(tokens[2])
            continue
    else:
        raise ValueError(f'invalid instruction ${inst}')
    regs[4] += 1
print(regs[0])
