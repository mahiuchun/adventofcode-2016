screen = [['.'] * 50 for _ in range(6)]

with open('day08/input.txt') as h:
    for line in h:
        line = line.strip()
        tokens = line.split()
        if tokens[0] == 'rect':
            ab = tokens[1].split('x')
            a, b = int(ab[0]), int(ab[1])
            for i in range(b):
                for j in range(a):
                    screen[i][j] = '#'
        elif tokens[1] == 'row':
            a, b = int(tokens[2][2:]), int(tokens[4])
            newrow = [None] * 50
            for i in range(50):
                newrow[(i+b)%50] = screen[a][i]
            screen[a] = newrow
        else:
            a, b = int(tokens[2][2:]), int(tokens[4])
            newcol = [None] * 6
            for i in range(6):
                newcol[(i+b)%6] = screen[i][a]
            for i in range(6):
                screen[i][a] = newcol[i]
[print(''.join(s)) for s in screen]
