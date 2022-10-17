def has_aba(s):
    n = len(s)
    if n < 3:
        return []
    choices = []
    for i in range(n-2):
        t = s[i:i+3]
        if t[0] == t[2] and t[0] != t[1]:
            choices.append((t[0], t[1]))
    return choices

def has_bab(s, a, b):
    n = len(s)
    if n < 3:
        return False
    for i in range(n-2):
        t = s[i:i+3]
        if t[0] == b and t[1] == a and t[2] == b:
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
        choices = []
        for tok in outside:
            choices.extend(has_aba(tok))
        for tok in inside:
            found = False
            for ab in choices:
                if has_bab(tok, ab[0], ab[1]):
                    found = True
                    break
            if found:
                tot += 1
                break
print(tot)
