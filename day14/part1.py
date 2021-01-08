from collections import defaultdict
from functools import lru_cache
from math import ceil
def parse_ingredient(ingredient):
    result_n,result_t = ingredient.split(' ')
    return result_t, int(result_n)
def parse_line(line):
    ingredients,result = line.strip().split(" => ")
    result_t, result_n = parse_ingredient(result)
    return (result_t,(result_n,dict(parse_ingredient(i) for i in ingredients.split(', '))))
class hashabledict(dict):
  def __key(self):
    return tuple((k,self[k]) for k in sorted(self))
  def __hash__(self):
    return hash(self.__key())
  def __eq__(self, other):
    return self.__key() == other.__key()
formulas = dict(parse_line(l) for l in open('i','r'))

have = {i:0 for i in formulas}
have["ORE"] = 0
have["FUEL"] = -1
steps=0
while any(v<0 for k,v in have.items() if k!="ORE"):
    for i,val in have.items():
        if i == "ORE":
            continue
        elif val < 0:
            quantity,ingredients = formulas[i]
            for new_i,new_v in ingredients.items():
                have[new_i] -= new_v
            have[i] += quantity
    steps += 1
ore_per_fule = -have["ORE"]
print(ore_per_fule)
left_overs = have
del left_overs["ORE"]
del left_overs["FUEL"]
have = {i:0 for i in formulas}
have["ORE"] = 1000000000000
while have["ORE"] > ore_per_fule:
    fuels = have["ORE"]//ore_per_fule
    have["ORE"] -= fuels*ore_per_fule
    have["FUEL"] += fuels
    for i,v in left_overs.items():
        have[i] += v*fuels
    deconstruct = True
    while(deconstruct):
        deconstruct = False
        for i,v in have.items():
            if i not in {"ORE","FUEL"}:
                quantity,ingredients = formulas[i]
                groups = v//quantity
                if groups > 0:
                    have[i] -= groups*quantity
                    for new_i,new_v in ingredients.items():
                        deconstruct = True
                        have[new_i] += new_v*groups
print(have["FUEL"])