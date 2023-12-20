import copy

rawWork, rawInput = [op.splitlines() for op in open("text.txt").read().split('\n\n')]

workFlows = {flow.split('{')[0]: [[rule[0], rule[1], int(rule[2:].split(':')[0]), rule.split(':')[1]] if ':' in rule else rule for rule in flow[:-1].split('{')[1].split(',')] for flow in rawWork}

accepted = []
flows = [['in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}]]

while flows:
    flow, obj = flows.pop(0)
    while flow != 'R' and flow != 'A':
        broke = False
        for rule in workFlows[flow][:-1]:
            
            if (obj[rule[0]][0]>rule[2] and rule[1] == '>') or (obj[rule[0]][1]<rule[2] and rule[1] == '<'):
                flow = rule[3]
                broke = True
                break
            
            if obj[rule[0]][0]<rule[2] and obj[rule[0]][1]>rule[2]:
                if rule[1] == '>':
                    newObj = copy.deepcopy(obj)
                    newObj[rule[0]] = (rule[2]+1, newObj[rule[0]][1])
                    flows.append([rule[3], newObj])

                    obj[rule[0]] = (obj[rule[0]][0], rule[2])
                else:
                    
                    newObj = copy.deepcopy(obj)
                    newObj[rule[0]] = (newObj[rule[0]][0], rule[2]-1)
                    flows.append([rule[3], newObj])
                    obj[rule[0]] = (rule[2], obj[rule[0]][1])

        if not broke:
            flow = workFlows[flow][-1]
    
    if flow == 'A':
        accepted.append(obj)


total = 0
for obj in accepted:
    diffs = []
    for s in 'xmas':
        diffs.append(obj[s][1]-obj[s][0]+1)
    
    total += diffs[0]*diffs[1]*diffs[2]*diffs[3]

print(total)
