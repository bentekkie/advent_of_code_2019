from typing import NamedTuple
from itertools import combinations
import math



class Moon(NamedTuple):
    x:int
    y:int
    z:int
    dx:int=0
    dy:int=0
    dz:int=0

    def energy(self):
        return (abs(self[0])+abs(self[1])+abs(self[2]))*(abs(self.dx)+abs(self.dy)+abs(self.dz))

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

pairs = list(combinations(range(4),2))
def find_period(orig_pos,orig_vel):
    pos = orig_pos[:]
    vel = orig_vel[:]
    period = 0
    step = 0
    while True:
        for a,b in pairs:
            if pos[a] > pos[b]:
                vel[a] -= 1
                vel[b] += 1
            elif pos[a] < pos[b]:
                vel[a] += 1
                vel[b] -= 1
        for i in range(4):
            pos[i] += vel[i]
        period += 1
        if pos==orig_pos and vel==orig_vel:
            return period
        step += 1
    
    


def step(moons):
    new_moons : set[Moon] = set()
    for moon in moons:
        x,y,z,dx,dy,dz = moon
        for other in moons:
            if other[0]!=x:
                dx+=1 if other[0]>x else -1
            if other[1]!=y:
                dy+=1 if other[1]>y else -1
            if other[2]!=z:
                dz+=1 if other[2]>z else -1
        new_moons.add(Moon(x+dx,y+dy,z+dz,dx,dy,dz))
    return new_moons

moons={
Moon(x=1, y=4, z=4),
Moon(x=-4, y=-1, z=19),
Moon(x=-15, y=-14, z=12),
Moon(x=-17, y=1, z=10)}

x_period = find_period([m.x for m in moons],[0]*4)
y_period = find_period([m.y for m in moons],[0]*4)
z_period = find_period([m.z for m in moons],[0]*4)
res = lcm(lcm(x_period,y_period),z_period)
print(x_period,y_period,z_period,res)

for _ in range(1000):
    moons  = step(moons)
print(sum(m.energy() for m in moons))
