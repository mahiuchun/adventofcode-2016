x, y, dx, dy = 0, 0, 0, 1
vis = {(0, 0)}

with open('day01/input.txt') as h:
    inp = h.read().strip()
    for ins in inp.split(', '):
        if ins[0] == 'R':
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        n = int(ins[1:])
        twice = False
        for i in range(n):
            x, y = x+dx, y+dy
            if (x, y) in vis:
                twice = True
                break
            vis.add((x, y))
        if twice:
            break
    print(abs(x) + abs(y))
