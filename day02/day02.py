x, y = 1, 1
with open('day02/input.txt') as h:
    for line in h:
        line = line.strip()
        for c in line:
            if c == 'U':
                y = max(y-1, 0)
            elif c == 'D':
                y = min(y+1, 2)
            elif c == 'L':
                x = max(x-1, 0)
            elif c == 'R':
                x = min(x+1, 2)
        print(3*y+x+1, end='')
    print()
