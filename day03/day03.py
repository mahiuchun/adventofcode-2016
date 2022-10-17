tot = 0
with open('day03/input.txt') as h:
    for line in h:
        sides = [int(x) for x in line.strip().split()]
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            tot += 1
    print(tot)
