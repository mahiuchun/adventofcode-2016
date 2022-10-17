from collections import deque

inp = 1362
memo = dict()

def nbits(n):
    return bin(n)[2:].count('1')

def wall(x, y):
    key = (x, y)
    if key in memo:
        return memo[key]
    z = x*x + 3*x + 2*x*y + y + y*y + inp
    memo[key] = (nbits(z) % 2 == 1)
    return memo[key]

initial = (1,1)
goal = (31,39)

que = deque([(initial, 0)])
seen = set([initial])
try:
    while len(que) > 0:
        pos, steps = que.popleft()
        x, y = pos
        cands = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        for cand in cands:
            if cand == goal:
                print(steps+1)
                raise StopIteration
            x, y = cand
            if x < 0 or y < 0:
                continue
            if wall(x, y):
                continue
            if cand in seen:
                continue
            seen.add(cand)
            que.append((cand, steps+1))
except StopIteration:
    pass
