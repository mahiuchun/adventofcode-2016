import sys

ranges_ = []

with open('day20/input.txt') as h:
    for line in h:
        line = line.strip()
        ranges_.append(tuple(sorted(map(int, line.split('-')))))
ranges_.sort()

def merge(r1, r2):
    if r1 is None:
        return r2
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))

blocked = 0
curr = ranges_[0]
n = len(ranges_)
for i in range(1, n):
    rr = ranges_[i]
    if curr[1] < rr[0]:
        blocked += curr[1] - curr[0] + 1
        curr = rr
    else:
        curr = merge(curr, rr)
blocked += curr[1] - curr[0] + 1
print(2**32-blocked)
