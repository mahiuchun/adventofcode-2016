def decompress(line):
    tot = 0
    n = len(line)
    i = 0
    while i < n:
        if line[i] == '(':
            j = i + 1
            while j < n:
                if line[j] == ')':
                    break
                j += 1
            mark = line[i+1:j]
            parts = mark.split('x')
            a, b = int(parts[0]), int(parts[1])
            tot += decompress(line[j+1:j+a+1]) * b
            i = j + a + 1
        else:
            tot += 1
            i += 1
    return tot


with open('day09/input.txt') as h:
    for line in h:
        line = line.strip()
        print(decompress(line))
