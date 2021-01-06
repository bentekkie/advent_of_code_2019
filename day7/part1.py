from itertools import product
from collections import defaultdict

def run_amp(raw_program):
    relative_base = 0
    program = defaultdict(int)
    for i,cmd in enumerate(raw_program):
        program[i]=cmd
    curr_pos = 0
    get = [lambda pos: program[program[pos]],lambda pos: program[pos], lambda pos: program[pos+relative_base]]
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
            #print(modes, relative_base)
            #print(program[curr_pos+1])
            #print(set_pos[modes[0]](curr_pos+1))
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

def start_amp(program,phase):
    amp = run_amp(program)
    next(amp)
    amp.send(phase)
    return amp

def test_seq(phases):
    signal = 0
    amps = [start_amp(program,phase) for phase in phases]
    curr_amp = 0
    while True:
        signal = amps[curr_amp].send(signal)
        if next(amps[curr_amp]) == "HALT" and curr_amp == len(amps) - 1:
            return signal
        curr_amp = (curr_amp + 1) % len(amps)

m = max(test_seq(x) for x in product(range(5,10),range(5,10),range(5,10),range(5,10),range(5,10)) if len(set(x)) == len(x))

print(m)