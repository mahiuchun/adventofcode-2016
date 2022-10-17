import re

INPUT = re.compile(r'^Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).$')

disks_ = []

with open('day15/input.txt') as h:
    for line in h:
        line = line.strip()
        m = INPUT.match(line)
        npos = int(m.group(2))
        pos = int(m.group(3))
        disks_.append([npos, pos])

t = 0
while True:
    all_zero = True
    for i, _ in enumerate(disks_):
        pos = (disks_[i][1] + t + i + 1) % disks_[i][0]
        if pos != 0:
            all_zero = False
            break
    if all_zero:
        print(t)
        break
    t += 1
