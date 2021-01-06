program = [int(l.strip()) for l in next(open('i')).split(',')]
def run_program(program,id):
    output = []
    program=program[:]
    curr_pos = 0
    get = [lambda pos: program[program[pos]],lambda pos: program[pos]]
    while curr_pos < len(program):
        raw_op_code = program[curr_pos]
        op_code = raw_op_code % 100
        modes = list(reversed([int(i) for i in str(raw_op_code)[:-2]]))+[0]*4
        print(curr_pos,raw_op_code,op_code,modes)
        if op_code == 1:
            program[program[curr_pos+3]] = get[modes[0]](curr_pos+1)+get[modes[1]](curr_pos+2)
            curr_pos += 4
        elif op_code == 2:
            program[program[curr_pos+3]] = get[modes[0]](curr_pos+1)*get[modes[1]](curr_pos+2)
            curr_pos += 4
        elif op_code == 99:
            break
        elif op_code == 3:
            program[program[curr_pos+1]]=id
            curr_pos += 2
        elif op_code == 4:
            output.append(get[modes[0]](curr_pos+1))
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
            program[program[curr_pos+3]] = 1 if get[modes[0]](curr_pos+1) < get[modes[1]](curr_pos+2) else 0
            curr_pos += 4
        elif op_code == 8:
            program[program[curr_pos+3]] = 1 if get[modes[0]](curr_pos+1) == get[modes[1]](curr_pos+2) else 0
            curr_pos += 4

    return output


print(run_program(program,1))
print(run_program(program,5))