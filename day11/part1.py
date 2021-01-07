from collections import defaultdict
def run(raw_program):
    relative_base = 0
    program = defaultdict(int)
    for i,cmd in enumerate(raw_program):
        program[i]=cmd
    curr_pos = 0
    get = [lambda pos: program[program[pos]],lambda pos: program[pos], lambda pos: program[program[pos]+relative_base]]
    set_pos = [lambda pos: program[pos],lambda pos: pos, lambda pos: program[pos]+relative_base]
    while True:
        raw_op_code = program[curr_pos]
        op_code = raw_op_code % 100
        modes = list(reversed([int(i) for i in str(raw_op_code)[:-2]]))+[0]*4
        #print(program)
        if op_code == 1:
            program[set_pos[modes[2]](curr_pos+3)] = get[modes[0]](curr_pos+1)+get[modes[1]](curr_pos+2)
            curr_pos += 4
        elif op_code == 2:
            program[set_pos[modes[2]](curr_pos+3)] = get[modes[0]](curr_pos+1)*get[modes[1]](curr_pos+2)
            curr_pos += 4
        elif op_code == 99:
            break
        elif op_code == 3:
            program[set_pos[modes[0]](curr_pos+1)]= yield
            curr_pos += 2
        elif op_code == 4:
            yield get[modes[0]](curr_pos+1)
            curr_pos += 2
        elif op_code == 5:
            if get[modes[0]](curr_pos+1) > 0:
                curr_pos = get[modes[1]](curr_pos+2)
            else:
                curr_pos += 3
        elif op_code == 6:
            if get[modes[0]](curr_pos+1) == 0:
                curr_pos = get[modes[1]](curr_pos+2)
            else:
                curr_pos += 3
        elif op_code == 7:
            program[set_pos[modes[2]](curr_pos+3)] = 1 if get[modes[0]](curr_pos+1) < get[modes[1]](curr_pos+2) else 0
            curr_pos += 4
        elif op_code == 8:
            program[set_pos[modes[2]](curr_pos+3)] = 1 if get[modes[0]](curr_pos+1) == get[modes[1]](curr_pos+2) else 0
            curr_pos += 4
        elif op_code == 9:
            relative_base += get[modes[0]](curr_pos+1)
            curr_pos += 2
    yield "HALT"
program = [int(l.strip()) for l in next(open('i')).split(',')]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def paint():
    robot = run(program)
    next(robot)
    painted = set()
    robot_loc = tuple([0,0])
    board = {robot_loc}
    direction = 0
    print(board)
    while True:
        color = robot.send(1 if robot_loc in board else 0)
        turn = next(robot)
        if color == 1:
            board.add(robot_loc)
        elif robot_loc in board:
            board.remove(robot_loc)
        direction = (direction + (1 if turn == 1 else -1)) % len(dirs)
        dx,dy = dirs[direction]
        robot_loc = (robot_loc[0]+dx,robot_loc[1]+dy)
        if next(robot) == "HALT":
            return board

board = paint()
min_x = min(x for x,_ in board)
max_x = max(x for x,_ in board)
min_y = min(x for _,x in board)
max_y = max(x for _,x in board)

for y in reversed(range(min_y,max_y+1)):
    print("".join("#" if (x,y) in board else " " for x in range(min_x,max_x+1)))