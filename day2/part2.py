program = [int(l.strip()) for l in next(open('i')).split(',')]
def run_program(program, noun, verb):
    program=program[:]
    program[1]=noun
    program[2]=verb

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

    return program[0]

for noun in range(100):
    for verb in range(100):
        if run_program(program,noun,verb) ==19690720:
            
            print(noun,verb,100*noun+verb)