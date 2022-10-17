from collections import deque

GENERATOR = 0
MICROCHIP = 1

floors = [[] for _ in range(4)]
elev = 0
elems = dict()

def is_safe(arrangement):
    floors, _ = arrangement
    for floor in floors:
        chips = set()
        hasg = False
        for e in floor:
            if e & 1 == MICROCHIP:
                chips.add(e >> 1)
        for e in floor:
            if e & 1 == GENERATOR:
                if e >> 1 in chips:
                    chips.remove(e >> 1)
                hasg = True
        if len(chips) > 0 and hasg:
            return False
    return True

def moves(arrangement):
    res = []
    floors, elev = arrangement
    nelevs = []
    if elev > 0:
        nelevs.append(elev-1)
    if elev < 3:
        nelevs.append(elev+1)
    for nelev in nelevs:
        ne = len(floors[elev])
        for i in range(ne):
            for j in range(i, ne):
                cand = [list(x) for x in floors]
                cand[nelev].append(floors[elev][i])
                cand[elev][i] = None
                if j != i:
                    cand[nelev].append(floors[elev][j])
                    cand[elev][j] = None
                    cand[elev].remove(None)
                cand[elev].remove(None)
                for k, _ in enumerate(cand):
                    cand[k].sort()
                    cand[k] = tuple(cand[k])
                narr = (tuple(cand), nelev)
                if is_safe(narr):
                    res.append(narr)
    return res

def append(lst, e):
    e0, e1 = e
    if not e0 in elems:
        elems[e0] = len(elems)
    e0 = elems[e0]
    if e1 == 'generator':
        e1 = GENERATOR
    else:
        e1 = MICROCHIP
    lst.append(2*e0+e1)

with open('day11/input.txt') as h:
    for i, line in enumerate(h):
        line = line.strip('.\n')
        words = line.split()
        for j, word in enumerate(words):
            word = word.strip(',')
            if word == 'generator':
                append(floors[i], (words[j-1], word))
            elif word == 'microchip':
                append(floors[i], (words[j-1][:-11], word))
        if i == 0:
            append(floors[i], ('elerium', 'generator'))
            append(floors[i], ('elerium', 'microchip'))
            append(floors[i], ('dilithium', 'generator'))
            append(floors[i], ('dilithium', 'microchip'))
        floors[i].sort()
        floors[i] = tuple(floors[i])
floors = tuple(floors)

initial = (floors, elev)
final = [[list(x) for x in floors], 3]
for i in range(3):
    final[0][3].extend(final[0][i])
    final[0][i] = []
for i in range(4):
    final[0][i].sort()
    final[0][i] = tuple(final[0][i])
final[0] = tuple(final[0])
final = tuple(final)

qfront = deque([(initial, 0)])
qback = deque([(final, 0)])
sfront, sback = {initial: 0}, {final: 0}
dfront, dback = 0, 0
cont = True
while cont:
    while len(qfront) > 0 and qfront[0][1] == dfront:
        arr, _ = qfront.popleft()
        for narr in moves(arr):
            if narr in sback:
                print(dfront + sback[narr] + 1)
                cont = False
                break
            if narr in sfront:
                continue
            sfront[narr] = dfront + 1
            qfront.append((narr, dfront + 1))
        if not cont:
            break
    if not cont:
        break
    dfront += 1
    while len(qback) > 0 and qback[0][1] == dback:
        arr, _ = qback.popleft()
        for narr in moves(arr):
            if narr in sfront:
                print(sfront[narr] + dback + 1)
                cont = False
                break
            if narr in sback:
                continue
            sback[narr] = dback + 1
            qback.append((narr, dback + 1))
        if not cont:
            break
    dback += 1
