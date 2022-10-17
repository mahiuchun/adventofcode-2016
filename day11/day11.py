from collections import deque

floors = [[] for _ in range(4)]
elev = 0
tot = 0

def is_safe(arrangement):
    floors, _ = arrangement
    for floor in floors:
        chips = set()
        hasg = False
        for e in floor:
            if e[1] == 'microchip':
                chips.add(e[0])
        for e in floor:
            if e[1] == 'generator':
                if e[0] in chips:
                    chips.remove(e[0])
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
                res.append((tuple(cand), nelev))
    return res

def is_goal(arrangement):
    floors, elev = arrangement
    return len(floors[3]) == tot and elev == 3

with open('day11/input.txt') as h:
    for i, line in enumerate(h):
        line = line.strip('.\n')
        words = line.split()
        for j, word in enumerate(words):
            word = word.strip(',')
            if word == 'generator':
                floors[i].append((words[j-1], word))
            elif word == 'microchip':
                floors[i].append((words[j-1][:-11], word))
        floors[i].sort()
        floors[i] = tuple(floors[i])
        tot += len(floors[i])
floors = tuple(floors)

inital = (floors, elev)
queue = deque([(inital, 0)])
seen = set([inital])
while len(queue) > 0:
    arr, steps = queue.popleft()
    if is_goal(arr):
        print(steps)
        break
    for narr in moves(arr):
        if narr in seen:
            continue
        seen.add(narr)
        if not is_safe(narr):
            continue
        queue.append((narr, steps+1))
