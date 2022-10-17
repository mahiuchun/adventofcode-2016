# regs[4] is pc
regs = [0 for _ in range(5)]
insts = []

def reg_or_val(token):
    if token[0] in '-0123456789':
        return int(token)
    else:
        return regs[ord(token)-ord('a')]

with open('day23/input.txt') as h:
    for line in h:
        line = line.strip()
        insts.append(line)

def toggle(s):
    tokens = s.split()
    if len(tokens) == 2:
        if tokens[0] == 'inc':
            tokens[0] = 'dec'
        else:
            tokens[0] = 'inc'
    elif len(tokens) == 3:
        if tokens[0] == 'jnz':
            tokens[0] = 'cpy'
        else:
            tokens[0] = 'jnz'
    return ' '.join(tokens)

regs[0] = 7
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
    elif tokens[0] == 'tgl':
        off = regs[4] + reg_or_val(tokens[1])
        if 0 <= off < len(insts):
            insts[off] = toggle(insts[off])
    else:
        raise ValueError('invalid instruction: ' + inst)
    regs[4] += 1
print(regs[0])
