import sys

ranges_ = []

with open('day20/input.txt') as h:
    for line in h:
        line = line.strip()
        ranges_.append(tuple(sorted(map(int, line.split('-')))))
ranges_.sort()

for i, r in enumerate(ranges_):
    lo, hi = r
    cands = [lo-1, hi+1]
    for c in cands:
        if c < 0:
            continue
        if c >= 2**32:
            continue
        ok = True
        for rr in ranges_:
            if rr[0] <= c <= rr[1]:
                ok = False
                break
            elif c < rr[0]:
                break
        if ok:
            print(c)
            sys.exit(0)
