INP = 3014603

def josephus(x):
    y = 1
    while 2 * y <= x:
        y *= 2
    return 2 * (x - y) + 1

print(josephus(INP))
