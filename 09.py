import random

def randams(cs):
    r = random.sample(cs[1:-1], len(cs) - 2)
    return (cs[0] + "".join(r) + cs[-1])


S = input().split(" ")
rs = []

for s in S:
    if len(s) > 4:
        rs.append(randams(s))
    else:
        rs.append(s)

print(" ".join(rs))