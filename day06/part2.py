from collections import Counter

messages = []
with open('day06/input.txt') as h:
    for line in h:
        messages.append(line.strip())

m = len(messages)
n = len(messages[0])
res = []
for i in range(n):
    c = Counter()
    for j in range(m):
        c.update(messages[j][i])
    res.append(c.most_common()[-1][0][0])
print(''.join(res))
