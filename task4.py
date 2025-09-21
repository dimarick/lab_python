from input_parser import parseInput
a = parseInput(sep='.')

b = []
for i in range(len(a)):
    b.append(a[len(a) - 1 - i])

print(b)
