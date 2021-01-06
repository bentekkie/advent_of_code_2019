

def intersections(s1,s2):
    s1_p1,s1_p2,s1_dir = s1
    s2_p1,s2_p2,s1_dir = s2
    if s1_dir == "X" and s1_dir == "X" and s1_p1[1]== s2_p2[1]:
        _,a,b,_ = sorted(p[0] for p in s1[:2]+s2[:2])
        if abs(a) < abs(b):
            yield ((a,s1_p1[1]),s1,s2)
        else:
            yield ((b,s1_p1[1]),s1,s2)
    elif s1_dir == "Y" and s1_dir == "Y" and s1_p1[0]== s2_p2[0]:
        _,a,b,_ = sorted(p[1] for p in s1[:2]+s2[:2])
        if abs(a) < abs(b):
            yield ((s1_p1[0],a),s1,s2)
        else:
            yield ((s1_p1[0],b),s1,s2)
    elif s1_dir == "X" and s1_dir == "Y":
        ymin,ymax=sorted([s2_p1[1],s2_p2[1]])
        xmin,xmax=sorted([s1_p1[0],s1_p2[0]])
        if ymin<=s1_p1[1]<=ymax and xmin<=s2_p1[0]<=xmax:
            yield ((s2_p1[0],s1_p1[1]),s1,s2)
    else:
        ymin,ymax=sorted([s1_p1[1],s1_p2[1]])
        xmin,xmax=sorted([s2_p1[0],s2_p2[0]])
        if ymin<=s2_p1[1]<=ymax and xmin<=s1_p1[0]<=xmax:
            yield ((s1_p1[0],s2_p1[1]),s1,s2)



def translate(p,instruction):
    if instruction[0]=="R":
        return (p,(p[0]+int(instruction[1:]),p[1]),"X")
    elif instruction[0]=="L":
        return (p,(p[0]-int(instruction[1:]),p[1]),"X")
    elif instruction[0]=="U":
        return (p,(p[0],p[1]+int(instruction[1:])),"Y")
    elif instruction[0]=="D":
        return (p,(p[0],p[1]-int(instruction[1:])),"Y")

def segments(curr_pos, instructions):
    if len(instructions) == 0:
        return
    seg =  translate(curr_pos, instructions[0])
    yield seg
    yield from segments(seg[1],instructions[1:])

def all_points(p, instructions, steps=0):
    if len(instructions) > 0:
        instruction = instructions[0]
        val=int(instruction[1:])
        restRange = range(1,val+1)
        if instruction[0]=="R":
            yield from map(lambda x: ((p[0]+x,p[1]),steps+x), restRange)
            yield from all_points((p[0]+val,p[1]),instructions[1:],steps+val)
        elif instruction[0]=="L":
            yield from map(lambda x: ((p[0]-x,p[1]),steps+x), restRange)
            yield from all_points((p[0]-val,p[1]),instructions[1:],steps+val)
        elif instruction[0]=="U":
            yield from map(lambda x: ((p[0],p[1]+x),steps+x), restRange)
            yield from all_points((p[0],p[1]+val),instructions[1:],steps+val)
        elif instruction[0]=="D":
            yield from map(lambda x: ((p[0],p[1]-x),steps+x), restRange)
            yield from all_points((p[0],p[1]-val),instructions[1:],steps+val)

wires = [list(all_points((0,0),l.strip().split(','))) for l in open('i')]
wire1,wire2 = wires
wire1Pts,wire2Pts = [{(x,y) for (x,y),_ in wire} for wire in wires]
wire1Dict,wire2Dict = [{(x,y):s for (x,y),s in wire} for wire in wires]
#intersections = {p for w1_sec in wire1 for w2_sec in wire2 for p in intersections(w1_sec,w2_sec)}

#print(wire1)
#print(wire2)
print(min(abs(x)+abs(y) for x,y in wire1Pts & wire2Pts))

print(min(wire1Dict[p]+wire2Dict[p] for p in wire1Pts & wire2Pts))

'''
for i in intersections:
    print(i)


print(sorted(abs(x)+abs(y) for (x,y),_,_ in intersections)[:5])
'''