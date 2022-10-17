class Robot:
    def __init__(self, rule, robots, outs):
        self.chips = []
        self.rule = rule
        self.robots = robots
        self.outs = outs

    def add_chip(self, x):
        self.chips.append(x)
        self.chips.sort()
    
    def trigger(self):
        if len(self.chips) == 2:
            tokens = self.rule.split()
            lo = int(tokens[6])
            hi = int(tokens[11])
            if tokens[5] == 'bot':
                self.robots[lo].add_chip(self.chips[0])
            else:
                self.outs[lo] = self.chips[0]
            if tokens[10] == 'bot':
                self.robots[hi].add_chip(self.chips[1])
            else:
                self.outs[hi] = self.chips[1]
            self.chips = []
            return True
        return False

insts = []
robots = dict()
outs = dict()

with open('day10/input.txt') as h:
    for line in h:
        line = line.strip()
        insts.append(line)

for inst in insts:
    tokens = inst.split()
    if len(tokens) == 6:
        continue
    robot = Robot(inst, robots, outs)
    robots[int(tokens[1])] = robot
for inst in insts:
    tokens = inst.split()
    if len(tokens) == 12:
        continue
    robots[int(tokens[5])].add_chip(int(tokens[1]))


while True:
    triggered = False
    for k, v in robots.items():
        triggered = triggered or v.trigger()
    if not triggered:
        break
print(outs[0] * outs[1] * outs[2])
