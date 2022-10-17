import re

OP_RES = {
    'SWAP1': re.compile(r'^swap position (\d+) with position (\d+)$'),
    'SWAP2': re.compile(r'^swap letter (.) with letter (.)$'),
    'ROT1': re.compile(r'^rotate (left|right) (\d+) steps?$'),
    'ROT2': re.compile(r'^rotate based on position of letter (.)$'),
    'REV': re.compile(r'^reverse positions (\d+) through (\d+)$'),
    'MOVE': re.compile(r'^move position (\d+) to position (\d+)$'),
}
INIT = 'fbgdceah'

def swap(s, x, y):
    l = list(s)
    l[x], l[y] = l[y], l[x]
    return ''.join(l)

def rev(s, x, y):
    l = list(s)
    while x < y:
        l[x], l[y] = l[y], l[x]
        x += 1
        y -= 1
    return ''.join(l)

def rotr(s, d):
    n = len(s)
    s = rev(s, 0, n-d-1)
    s = rev(s, n-d, n-1)
    s = rev(s, 0, n-1)
    return s

ops = []
with open('day21/input.txt') as h:
    for line in h:
        line = line.strip()
        ops.append(line)
rrot2 = [None] * len(INIT)
for i, _ in enumerate(INIT):
    d = 1 + i
    if i >= 4:
        d += 1
    j = (i + d) % len(INIT)
    d %= len(INIT)
    d = len(INIT) - d
    d %= len(INIT)
    rrot2[j] = d
s = INIT[:]
for op in reversed(ops):
    for n, r in OP_RES.items():
        m = r.match(op)
        if m is None:
            continue
        if n == 'SWAP1':
            x = int(m.group(1))
            y = int(m.group(2))
            s = swap(s, x, y)
        elif n == 'SWAP2':
            x = m.group(1)
            y = m.group(2)
            s = s.replace(x, '#')
            s = s.replace(y, x)
            s = s.replace('#', y)
        elif n == 'ROT1':
            kind = m.group(1)
            d = int(m.group(2))
            d %= len(s)
            if kind == 'right':
                d = len(s) - d
            s = rotr(s, d)
        elif n == 'ROT2':
            x = m.group(1)
            index = s.index(x)
            d = rrot2[index]
            s = rotr(s, d)
        elif n == 'REV':
            x = int(m.group(1))
            y = int(m.group(2))
            s = rev(s, x, y)
        elif n == 'MOVE':
            x = int(m.group(1))
            y = int(m.group(2))
            x, y = y, x
            l = list(s)
            ch = l[x]
            l = l[:x] + l[x+1:]
            l.insert(y, ch)
            s = ''.join(l)
        else:
            raise  ValueError('unsupported op: ' + op)
        break
print(s)
