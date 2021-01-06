from collections import defaultdict
d = defaultdict(set)

lines = [tuple(l.strip().split(')')) for l in open("j","r")]

for left,right in lines:
    d[left].add(right)


def orbits(curr, steps):
    return steps + sum(orbits(moon,steps+1) for moon in d[curr])

print(orbits("COM",0))


