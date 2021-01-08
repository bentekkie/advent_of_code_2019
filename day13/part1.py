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
            yield "INPUT"
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
    return
program = [int(l.strip()) for l in next(open('i')).split(',')]


def run_game(game):
    while True:
        try:
            n = next(game)
            if n=="INPUT":
                next(game)
                return
            yield (n,next(game),next(game))
        except StopIteration:
            return

def move(game,m):
    yield (game.send(m),next(game),next(game))
    while True:
        try:
            n = next(game)
            if n=="INPUT":
                next(game)
                return
            yield (n,next(game),next(game))
        except StopIteration:
            return
    
def display(tiletypes):
    types = [" ","w","B","p","b"]
    for y in range(min(y for _,y in tiletypes),max(y for _,y in tiletypes)+1):
        print("".join(types[tiletypes[(x,y)]] if (x,y) in tiletypes  else " " for x in range(min(x for x,_ in tiletypes),max(x for x,_ in tiletypes)+1)))   

program[0]=2

game = run(program)
score = 0
board = {(x,y):b for x,y,b in run_game(game)}
moves = 0
print(f"Blocks: {sum(b==2 for b in board.values())}")
while sum(b==2 for b in board.values()) > 0:
    #display(board)
    #print(f"Blocks Left: {sum(b==2 for b in board.values())}, score: {score}")
    paddle = next(k for k in board if board[k]==3)
    ball = next(k for k in board if board[k]==4)
    direction = 0
    if paddle[0]<ball[0]:
        direction = 1
    elif paddle[0]>ball[0]:
        direction = -1
    for x,y,b in  move(game,direction):
        if (-1,0) == (x,y):
            score = b
        else:
            board[(x,y)] = b
    moves += 1
print(f"Done score:{score}")