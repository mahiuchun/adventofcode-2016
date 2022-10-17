def has_abba(s):
    n = len(s)
    if n < 4:
        return False
    for i in range(n-3):
        t = s[i:i+4]
        if t[0] == t[3] and t[1] == t[2] and t[0] != t[1]:
            return True
    return False

tot = 0
with open('day07/input.txt') as h:
    for line in h:
        line = line.strip()
        inside = []
        outside = []
        n = len(line)
        buf = []
        for i in range(n):
            if line[i] == '[':
                outside.append(''.join(buf))
                buf = []
                continue
            elif line[i] == ']':
                inside.append(''.join(buf))
                buf = []
                continue
            else:
                buf.append(line[i])
        if len(buf)>0:
            outside.append(''.join(buf))
        if any(map(has_abba, outside)) and all(map(lambda s: not has_abba(s), inside)):
            tot += 1
print(tot)
