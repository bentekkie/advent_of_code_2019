from fractions import Fraction
from math import gcd,atan2,pi,sqrt
from collections import defaultdict
from sortedcontainers import SortedList
asteroids = {(x,y) for y,row in enumerate(open("i","r")) for x,c in enumerate(row.strip()) if c=="#"}

def simplify(x,y):
    if x==0:
        return (0,y//abs(y))
    if y==0:
        return (x//abs(x),0)
    g = gcd(x,y)
    #print(x,y,x//g,y//g)
    return (x//g,y//g)

def to_deg(x,y):
    return (atan2(y, x) * (180 / pi) + 450)%360

def seen(asteroid):
    x,y = asteroid
    return len({simplify(ox-x,oy-y) for ox,oy in asteroids - {asteroid}})
max_x,max_y = max(asteroids,key=seen)

degs = {to_deg(ox-max_x,oy-max_y) for ox,oy in asteroids - {(max_x,max_y)}}

slopes = {simplify(ox-max_x,oy-max_y) for ox,oy in asteroids - {(max_x,max_y)}}

buckets = {deg:SortedList([],key=lambda p: sqrt((p[0]-max_x)**2+(p[1]-max_y)**2)) for deg in degs}
for ox,oy in asteroids - {(max_x,max_y)}:
    deg = to_deg(ox-max_x,oy-max_y)
    buckets[deg].add((ox,oy))

order = []
direction = 0
dirs = sorted(degs)
while len(order) < len(asteroids) -1:
    if len(buckets[dirs[direction]]) > 0:
        order.append(buckets[dirs[direction]].pop(0))
    direction = (direction+1)%len(dirs)

print(order[199])