nums = [int(i) for i in next(open('i','r'))]

rows = [nums[i*25:(i+1)*25] for i in range(len(nums)//25)]

layers = [rows[i*6:(i+1)*6] for i in range(len(rows)//6)]

picture = [[next(layer[row][col] for layer in layers if layer[row][col]<2) for col in range(25)] for row in range(6)]

for row in picture:
    print("".join("X" if i==1 else " " for i in row))