from collections import Counter
import re

room = re.compile(r'^([a-z-]+)([0-9]+)\[([a-z]{5})\]$')
tot = 0

with open('day04/input.txt') as h:
    for line in h:
        line = line.strip()
        m = room.match(line)
        c = Counter(sorted(m.group(1)))
        del c['-']
        checksum = ''.join(e[0] for e in c.most_common(5))
        if checksum == m.group(3):
            tot += int(m.group(2))
    print(tot)
