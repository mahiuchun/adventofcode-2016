from collections import Counter
import re

room = re.compile(r'^([a-z-]+)([0-9]+)\[([a-z]{5})\]$')

with open('day04/input.txt') as h:
    for line in h:
        line = line.strip()
        m = room.match(line)
        encrypted = m.group(1)
        rot = int(m.group(2)) % 26
        buf = []
        for c in encrypted:
            if c != '-':
                d = chr(ord('a') + (ord(c)-ord('a')+rot)%26)
                buf.append(d)
            else:
                buf.append(' ')
        name = ''.join(buf)
        if 'northpole' in name:
            print(m.group(2))
            
