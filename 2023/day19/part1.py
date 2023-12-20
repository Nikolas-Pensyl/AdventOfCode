rawWork, rawInput = [op.splitlines() for op in open("text.txt").read().split('\n\n')]

objVals = [{item.split('=')[0]: int(item.split('=')[1]) for item in val[1:-1].split(',')} for val in rawInput]
workFlows = {flow.split('{')[0]: [[rule[0], rule[1], int(rule[2:].split(':')[0]), rule.split(':')[1]] if ':' in rule else rule for rule in flow[:-1].split('{')[1].split(',')] for flow in rawWork}
accepted = []

for obj in objVals:
    flow = 'in'
    while flow != 'R' and flow != 'A':
        broke = False
        for rule in workFlows[flow][:-1]:
            if (obj[rule[0]]>rule[2] and rule[1] == '>') or (obj[rule[0]]<rule[2] and rule[1] == '<'):
                flow = rule[3]
                broke = True
                break
        
        if not broke:
            flow = workFlows[flow][-1]
        
    
    if flow == 'A':
        accepted.append(obj)


total = 0
for obj in accepted:
    for s in 'xmas':
        total += obj[s]

print(total)
