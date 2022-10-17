from collections import deque
import hashlib

def is_open(x):
    return x in 'bcdef'

CODE = 'hhhxzeay'
# CODE = 'ulqzkmiv'
INIT = (1, 1)
GOAL = (4, 4)
DIRS = 'UDLR'
MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))

queue = deque([(INIT, '', 0)])
best = 0
while len(queue) > 0:
    pos, path, steps = queue.popleft()
    if pos == GOAL:
        best = max(best, steps)
        continue
    h = hashlib.md5((CODE + path).encode('ascii')).hexdigest()[:4]
    for i, m in enumerate(MOVES):
        npos = (pos[0]+m[0], pos[1]+m[1])
        if not is_open(h[i]):
            continue
        if npos[0] < 1 or npos[0] > 4 or npos[1] < 1 or npos[1] > 4:
            continue
        queue.append((npos, path + DIRS[i], steps + 1))
print(best)
