from collections import namedtuple
import re

PATT = re.compile(r'^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$')

Node = namedtuple('Node', ['x', 'y', 'used', 'avail'])

with open('day22/input.txt') as h:
    lines = h.readlines()
    lines = [x.strip() for x in lines[2:]]

def connected(a, b):
    if a.used == 0:
        return False
    if a.used > b.avail:
        return False
    return True

nodes = []
for line in lines:
    m = PATT.match(line)
    if m is None:
        raise ValueError('invalid line: ' + line)
    x, y, used, avail = int(m.group(1)), int(m.group(2)), int(m.group(4)), int(m.group(5))
    nodes.append(Node(x, y, used, avail))
tot = 0
n = len(nodes)
for i in range(n):
    for j in range(i+1, n):
        a, b = nodes[i], nodes[j]
        if connected(a, b) or connected(b, a):
            tot += 1
print(tot)
