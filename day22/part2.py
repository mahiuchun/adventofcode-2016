from collections import deque, namedtuple
import re

PATT = re.compile(r'^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$')
MOVES = ((-1, 0), (1, 0), (0, -1), (0, 1))

Node = namedtuple('Node', ['x', 'y', 'size', 'used', 'kind'])

with open('day22/input.txt') as h:
    lines = h.readlines()
    lines = [x.strip() for x in lines[2:]]

nodes = []
xm, ym = 0, 0
for line in lines:
    m = PATT.match(line)
    if m is None:
        raise ValueError('invalid line: ' + line)
    x, y, size, used = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    nodes.append(Node(x, y, size, used, '?'))
    xm, ym = max(xm, x), max(ym, y)
mat = [[None] * (xm + 1) for _ in range(ym + 1)]
emp_size = -1
emp_loc = None
for node in nodes:
    mat[node.y][node.x] = node
    if node.x == xm and node.y == 0:
        mat[node.y][node.x] = node._replace(kind='G')
    elif node.used == 0:
        mat[node.y][node.x] = node._replace(kind='_')
        emp_size = node.size
        emp_loc = (node.x, node.y)
for y in range(ym+1):
    for x in range(xm+1):
        u = mat[y][x]
        if u.kind != '?':
            continue
        nbs = []
        if x > 0:
            nbs.append((x-1, y))
        if x < xm:
            nbs.append((x+1, y))
        if y > 0:
            nbs.append((x, y-1))
        if y < ym:
            nbs.append((x, y+1))
        full = u.used > emp_size
        if full:
            mat[y][x] = u._replace(kind = '#')
        else:
            mat[y][x] = u._replace(kind = '.')

def shortest(loc1, loc2):
    queue = deque([(loc1, 0)])
    seen = set([loc1])
    while len(queue) > 0:
        loc, steps = queue.popleft()
        if loc == loc2:
            return steps
        for move in MOVES:
            nloc = (loc[0] + move[0], loc[1] + move[1])
            if nloc[0] < 0 or nloc[0] > xm or nloc[1] < 0 or nloc[1] > ym:
                continue
            if mat[nloc[1]][nloc[0]].kind != '.':
                continue
            if nloc in seen:
                continue
            seen.add(nloc)
            queue.append((nloc, steps+1))
    raise ValueError('path between ' + repr(loc1) + ' & ' + repr(loc2) + ' not found')

# TODO: The straight line path works in sample and my input.
# A more correct solution should find the shortest path avoiding # first.
tot = 0
for x in range(xm - 1, -1, -1):
    tot += shortest(emp_loc, (x, 0)) + 1
    mat[emp_loc[1]][emp_loc[0]] = mat[emp_loc[1]][emp_loc[0]]._replace(kind='.')
    emp_loc = (x+1, 0)
    mat[0][x] = mat[0][x]._replace(kind='G')
    mat[0][x+1] = mat[0][x+1]._replace(kind='_')
print(tot)
