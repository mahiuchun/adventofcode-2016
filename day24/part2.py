from collections import deque

MOVES = ((-1, 0), (1, 0), (0, -1), (0, 1))

map_ = []
with open('day24/input.txt') as h:
    for line in h:
        map_.append(line.strip())

def backtrack(dmat, loc, rem):
    best = 987654321
    last = True
    for i, cand in enumerate(rem):
        if cand is None:
            continue
        rem[i] = None
        d = dmat[loc][cand] + backtrack(dmat, cand, rem)
        best = min(best, d)
        rem[i] = cand
        last = False
    if last:
        return dmat[loc][0]
    return best

def dist(loc1, loc2):
    queue = deque([(loc1, 0)])
    seen = set([loc1])
    while len(queue) > 0:
        loc, steps = queue.popleft()
        if loc == loc2:
            return steps
        for move in MOVES:
            nloc = (loc[0] + move[0], loc[1] + move[1])
            if map_[nloc[1]][nloc[0]] == '#':
                continue
            if nloc in seen:
                continue
            seen.add(nloc)
            queue.append((nloc, steps+1))
    raise ValueError('dist between ' + repr(loc1) + ' & ' + repr(loc2) + ' not found')

locs = [None] * 10
h = len(map_)
w = len(map_[0])
for y in range(h):
    for x in range(w):
        if map_[y][x] in "0123456789":
            locs[int(map_[y][x])] = (x, y)
while locs[-1] is None:
    locs.pop()

n = len(locs)
dmat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        d = dist(locs[i], locs[j])
        dmat[i][j] = dmat[j][i] = d

print(backtrack(dmat, 0, list(range(1, n))))
