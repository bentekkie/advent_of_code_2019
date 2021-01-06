

def valid(n):
    d = str(n)
    return d[0]<=d[1]<=d[2]<=d[3]<=d[4]<=d[5] and any(d[i]==d[i+1] and d.count(d[i])==2 for i in range(5))

print(valid(111122))
print(sum(1 for x in range(197487,673252) if valid(x)))