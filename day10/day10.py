class Robot:
    def __init__(self, rule, robots):
        self.chips = []
        self.rule = rule
        self.robots = robots

    def add_chip(self, x):
        self.chips.append(x)
        self.chips.sort()
    
    def trigger(self):
        if len(self.chips) == 2:
            tokens = self.rule.split()
            if self.chips[0] == 17 and self.chips[1] == 61:
                print(tokens[1])
                raise StopIteration
            lo = int(tokens[6])
            hi = int(tokens[11])
            if tokens[5] == 'bot':
                self.robots[lo].add_chip(self.chips[0])
            if tokens[10] == 'bot':
                self.robots[hi].add_chip(self.chips[1])
            self.chips = []

insts = []
robots = dict()

with open('day10/input.txt') as h:
    for line in h:
        line = line.strip()
        insts.append(line)

for inst in insts:
    tokens = inst.split()
    if len(tokens) == 6:
        continue
    robot = Robot(inst, robots)
    robots[int(tokens[1])] = robot
for inst in insts:
    tokens = inst.split()
    if len(tokens) == 12:
        continue
    robots[int(tokens[5])].add_chip(int(tokens[1]))

try:
    while True:
        for k, v in robots.items():
            v.trigger()
except StopIteration:
    pass
