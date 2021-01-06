def p(x):
    #print(x)
    return x

fuel=lambda mass:-mass if p(mass)<=0 else mass//3-2+fuel(mass//3-2)
print(fuel(1969))
print(sum(fuel(int(l.strip())) for l in open('i')))