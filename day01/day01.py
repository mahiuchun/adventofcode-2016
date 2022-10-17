x, y, dx, dy = 0, 0, 0, 1

with open('day01/input.txt') as h:
    inp = h.read().strip()
    for ins in inp.split(', '):
        if ins[0] == 'R':
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        n = int(ins[1:])
        x, y = x+n*dx, y+n*dy
    print(abs(x) + abs(y))
