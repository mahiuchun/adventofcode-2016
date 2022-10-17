init_ = None
NROWS = 400000

with open('day18/input.txt') as h:
    init_ = h.read().strip()

count_ = init_.count('.')

def at(s, i):
    if i < 0 or i >= len(s):
        return '.'
    return s[i]

curr = init_
for _ in range(NROWS-1):
    nrow = []
    for i, _ in enumerate(curr):
        l, c, r = at(curr, i-1), at(curr, i), at(curr, i+1)
        if l == '^' and r == '^':
            nrow.append('.')
        elif l == '.' and r == '.':
            nrow.append('.')
        else:
            nrow.append('^')
    count_ += nrow.count('.')
    curr = ''.join(nrow)
print(count_)
