program = [int(l.strip()) for l in next(open('i')).split(',')]
program[1]=12
program[2]=2

print(program)

curr_pos = 0
while curr_pos < len(program):
    op_code = program[curr_pos]
    if op_code == 1:
        program[program[curr_pos+3]] = program[program[curr_pos+2]]+program[program[curr_pos+1]]
    elif op_code == 2:
        program[program[curr_pos+3]] = program[program[curr_pos+2]]*program[program[curr_pos+1]]
    elif op_code == 99:
        break
    curr_pos += 4

print(program[0])