def check(sides):
    t = sorted(sides)
    return t[0] + t[1] > t[2]

rows = []
with open('day03/input.txt') as h:
    for line in h:
        sides = [int(x) for x in line.strip().split()]
        rows.append(sides)

tot = 0
for i in range(len(rows)//3):
    for j in range(3):
        sides = (rows[i*3][j], rows[i*3+1][j], rows[i*3+2][j])
        tot += check(sides)
print(tot)
