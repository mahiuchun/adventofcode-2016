x, y = 0, 2
xy_min = [2, 1, 0, 1, 2]
xy_max = [2, 3, 4, 3, 2]
shape = [
    '  1',
    ' 234',
    '56789',
    ' ABC',
    '  D',
]
with open('day02/input.txt') as h:
    for line in h:
        line = line.strip()
        for c in line:
            if c == 'U':
                y = max(y-1, xy_min[x])
            elif c == 'D':
                y = min(y+1, xy_max[x])
            elif c == 'L':
                x = max(x-1, xy_min[y])
            elif c == 'R':
                x = min(x+1, xy_max[y])
        print(shape[y][x], end='')
    print()
