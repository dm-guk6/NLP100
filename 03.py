S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".split(" ")

length = []

for s in S:
    if s[-1] == ',' or s[-1] == '.':
        length.append(len(s[:-1]))
    else:
        length.append(len(s))

print(length)
