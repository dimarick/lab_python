from input_parser import parseInput

s, i = parseInput(sep=',')

r = 0

for c in s:
    if c != i:
        break
    r += 1

print(r)